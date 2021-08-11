import asyncio
import re
import time

import httpx
import pandas as pd
from bs4 import BeautifulSoup

names = {
    '001410': '信达澳银新能源产业股票',
    '180012': '银华富裕主题混合',
    '161903': '万家行业优选混合(LOF)',
    '005911': '广发双擎升级混合A',
    '001938': '中欧时代先锋股票A',
    '260108': '景顺长城新兴成长混合',
    '110022': '易方达消费行业股票',
    '000083': '汇添富消费行业混合',
    '003095': '中欧医疗健康混合A',
    '000831': '工银医疗保健股票',
}

dates = pd.date_range(start='2001-01-01', end='2021-08-10')

df = pd.DataFrame(index=dates, columns=names.values())


class Crawler:
    client: httpx.AsyncClient(http2=True)

    def __init__(self, code):
        self.code = code
        self.name = names[code]
        self.client = httpx.AsyncClient(http2=True, params={
            'type': 'lsjz',
            'per': 49,
            'code': self.code
        })

    async def get_pages(self):
        r = await self.client.get('https://fundf10.eastmoney.com/F10DataApi.aspx')
        pages = re.search(r'pages:\d+,', r.text).group()[6:-1]
        return int(pages)

    async def parse_data(self, page):
        r = await self.client.get('https://fundf10.eastmoney.com/F10DataApi.aspx', params={'page': page})
        while r.status_code == 514:
            await asyncio.sleep(0.1)
            r = await self.client.get('https://fundf10.eastmoney.com/F10DataApi.aspx', params={'page': page})
        text = re.search(r'<.+>', r.text).group()
        soup = BeautifulSoup(text, 'lxml')
        for tr in soup.tbody.children:
            tds = list(tr.children)
            date = tds[0].get_text()
            value = float(tds[1].get_text())
            df.loc[date, self.name] = value

    async def close(self):
        await self.client.aclose()


async def get_data(code):
    print('start crawler', code)
    crawler = Crawler(code=code)
    try:
        pages = await crawler.get_pages()
        tasks = []
        for page in range(1, pages + 1):
            # tasks.append(crawler.parse_data(page))
            await crawler.parse_data(page)
        # await asyncio.gather(*tasks)
    finally:
        await crawler.close()
        print('end crawler', code)


async def main():
    start = time.time()

    tasks = []
    for code in names:
        tasks.append(get_data(code))
    await asyncio.gather(*tasks)

    now = time.time()
    print("Time Consumed: ", now - start, ' s')


if __name__ == '__main__':
    asyncio.run(main())
    df.to_csv('funds.full.csv')
    df.dropna(axis=0, how='any', inplace=True)
    df.to_csv('funds.csv')

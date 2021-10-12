import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Strategy:
    name = 'strategy'

    def __init__(self, step=30):
        self.step = step
        self.index = 0
        self.cost = 1.0
        self.revenue = 0.0
        self.num = len(df.columns)
        self.price = df.iloc[0]
        self.amount = np.full(self.num, self.cost / self.num) / self.price

    def buy(self, index, percentage=None, money=None, amount=None):
        price = self.price[index]
        if amount is not None:
            assert amount >= 0
            pass
        elif percentage is not None:
            amount = self.amount[index] * percentage
        elif money is not None:
            assert money >= 0
            amount = money / price
        assert amount >= 0

        delta_money = price * amount
        if self.revenue >= delta_money:
            self.revenue -= delta_money
        else:
            self.cost += delta_money
        self.amount[index] += amount

    def sell(self, index, percentage=None, money=None, amount=None):
        price = self.price[index]
        if amount is not None:
            assert amount >= 0
            pass
        elif percentage is not None:
            amount = self.amount[index] * percentage
        elif money is not None:
            assert money >= 0
            amount = money / price
        assert 0 <= amount <= self.amount[index]

        delta_money = price * amount
        if delta_money < self.cost - 1:
            self.cost -= delta_money
        else:
            self.revenue += delta_money
        self.amount[index] -= amount

    def profit(self):
        profit = np.sum(self.amount * self.price) + self.revenue - self.cost
        return profit

    def to_results(self):
        if self.name not in results.columns:
            results[self.name] = np.zeros(len(df))
        results.loc[results.index[self.index], self.name] = self.profit()

    def calculate(self):
        pass

    def main(self):
        for i in range(len(df)):
            self.index = i
            self.price = df.iloc[i]
            if i % self.step == 0 and i >= self.step:
                self.calculate()
            self.to_results()
        print('profit of strategy {} is {:.1%}'.format(self.name, self.profit()))


class Lazy(Strategy):
    def __init__(self):
        super().__init__()
        self.name = 'lazy'


class Limit(Strategy):
    def __init__(self, limit=0.3, percentage=0.3, step=30):
        self.limit = limit
        self.percentage = percentage
        self.step = step
        self.name = 'limit(limit={}, step={})'.format(limit, step)
        super().__init__()

    def calculate(self):
        up_down = df.iloc[self.index] / df.iloc[self.index - self.step]
        avg_up_down = np.mean(up_down)
        for j in range(self.num):
            deviation = up_down[j] / avg_up_down
            percentage = min(abs(deviation - 1) * 1, 1)
            if deviation >= 1:
                self.sell(index=j, percentage=percentage)
            else:
                self.buy(index=j, percentage=percentage)


class Balance(Strategy):
    def __init__(self, step=30):
        super().__init__(step=step)
        self.name = 'balance(step={})'.format(self.step)

    def calculate(self):
        avg_money = np.mean(self.price * self.amount)

        for j in range(self.num):
            money = self.price[j] * self.amount[j]
            delta = money - avg_money
            if delta >= 0:
                self.sell(index=j, money=delta)
            else:
                self.buy(index=j, money=-delta)


if __name__ == '__main__':
    df = pd.read_csv('funds.csv', index_col=0)
    results = pd.DataFrame(index=df.index)

    Lazy().main()
    # Balance().main()
    # Limit().main()
    for i in range(1, 13):
        Balance(step=i * 30).main()
    # for i in range(0, 50):
    #     Limit(limit=i / 100).main()

    results.plot()
    plt.show()

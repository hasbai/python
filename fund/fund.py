import numpy as np
import pandas as pd


class Strategy:
    name = 'strategy'

    def __init__(self, percentage=30):
        self.cost = 1.0
        self.revenue = 0.0
        value = np.full(len(df.columns), self.cost / len(df.columns))
        self.amount = value / df.iloc[0]
        self.percentage = percentage

    def buy(self, index, price):
        delta_money = price * self.amount[index]
        if self.revenue >= delta_money:
            self.revenue -= delta_money
        else:
            self.cost += delta_money
        self.amount[index] *= 1 + self.percentage / 100

    def sell(self, index, price):
        delta_money = price * self.amount[index]
        self.revenue += delta_money
        self.amount[index] *= 1 - self.percentage / 100

    def profit(self):
        value = self.amount * df.iloc[-1]
        profit = (value.sum() + self.revenue) / self.cost - 1
        return profit

    def main(self, profit=None):
        if not profit:
            profit = self.profit()
        print('profit of strategy {} is {:.1%}'.format(self.name, profit))
        return profit


class Lazy(Strategy):
    def __init__(self):
        super().__init__()
        self.name = 'lazy'


class Mean(Strategy):
    def __init__(self, limit=0.3, step=30):
        super().__init__()
        self.name = 'mean(limit={}, step={})'.format(limit, step)
        self.limit = limit
        self.step = step

    def calculate(self, start):
        for i in range(start + self.step, len(df), self.step):
            up_down = df.iloc[i] / df.iloc[i - self.step] - 1
            for j in range(len(up_down)):
                if up_down[j] >= self.limit:
                    self.sell(index=j, price=df.iloc[i, j])
                if -up_down[j] >= self.limit:
                    self.buy(index=j, price=df.iloc[i, j])
        profit = self.profit()
        super().__init__()
        return profit

    def main(self, profit=None):
        results = []
        for i in range(self.step):
            results.append(self.calculate(start=i))
        profit = np.mean(results)
        super().main(profit=profit)


if __name__ == '__main__':
    df = pd.read_csv('funds.csv', index_col=0)

    Lazy().main()
    for i in range(0, 50):
        Mean(limit=i / 100).main()

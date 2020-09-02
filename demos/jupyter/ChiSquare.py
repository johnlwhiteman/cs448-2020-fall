import csv
import numpy as np
import pandas as pd
import pprint

class ChiSquare():

    def __init__(self, path='chisqare.csv'):
        self.table = None
        self.probs = None
        self.x2 = None
        self.dof = None
        self.cv = None
        self.p = None
        self.good = None
        self.observed = None
        self.expected = None
        self.path = 'chisquare.csv'

    def calculate(self, o, e, dof, cv):
        self.observed = o
        self.expected = e
        self.dof = dof
        self.cv = cv
        self.p = self.getP(self.dof, self.cv)
        self.x2 = 0

        for i in range(0, len(o)):
            o = self.observed[i]
            e = self.expected[i]
            print(f'[{i}]:', o, e)
            self.x2 += ((o - e)**2) / e

        self.good = self.x2 < self.p
        print(self.x2, self.p, self.good)

    def getP(self, dof, cv):
        p = None
        try:
            p = self.table[dof][cv]
        except KeyError as e:
            print(f'Error: dof={dof} / cv={cv}')
            print("Valid DoFs:")
            print(list(self.table.keys()))
            print("Valid Probabilities:")
            print(self.probs)
            return None
        return p

    def init(self):
        self.loadTable()

    def loadTable(self):
        i = -1
        self.table = {}
        self.probs = []
        with open(self.path) as fd:
            csvReader = csv.reader(fd, delimiter=',')
            for row in csvReader:
                i += 1
                if 0 == i:
                    self.probs  = [float(row[j]) for j in range(1, len(row))]
                    continue
                dof = int(row[0])
                self.table[dof] = {}
                for j in range(1, len(self.probs) + 1):
                    self.table[dof][self.probs[j-1]] = float(row[j])

    def showP(self, dof, cv):
        p = self.getP(dof, cv)
        print(f'The P value is: {p}')

    def showTable(self):
        pprint.pprint(self.table)

if __name__ == "__main__":
    results = [[4, 3, 1, 2, 2, 4, 1, 4, 6, 2, 5, 2],
               [5, 1, 4, 3, 1, 2, 4, 2, 4, 4, 3, 5],
               [6, 4, 6, 3, 1, 3, 4, 3, 3, 1, 4, 1],
               [6, 3, 2, 4, 5, 1, 6, 4, 4, 6, 4, 4],
               [1, 5, 2, 3, 4, 6, 3, 5, 1, 2, 4, 6]]
    bins =  [[], [], [], [], []]

    rows = len(results)
    cols1 = len(results[0])

    df1 = pd.DataFrame(data=np.array(results).transpose(),
                       index=np.arange(1, cols1+1),
                       columns=[chr(i) for i in range(ord('a'),ord('a')+rows)])
    #print(df1.describe())
    #print(df1)

    for i in range(0, rows):
        for j in range(1, 7):
            bins[i].append(results[i].count(j))
    cols2 = len(bins[0])
    df2 = pd.DataFrame(data=np.array(bins).transpose(),
                       index=np.arange(1, cols2+1),
                       columns=[chr(i) for i in range(ord('a'),ord('a')+rows)])
    #print(df2.describe())
    #print(df2)

    eMean = np.arange(1, cols2+1).mean()
    expected = [cols1 / cols2 for i in range(0, cols2)]
    dof = cols2 - 1
    cv = 0.05

    cs = ChiSquare()
    cs.init()

    print(expected)
    for observed in bins:
        cs.calculate(observed, expected, dof, cv)








    chi_square = 0

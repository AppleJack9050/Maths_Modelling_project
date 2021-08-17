import pandas as pd
import test2

df = pd.read_csv('season-1819_csv.csv')
# extract match information
data = df.iloc[:, 2:4]

team = pd.unique(data['HomeTeam'])
rank_data = pd.DataFrame({'Pts': [0] * team.size}, index=team)

import random

random.seed(19209554)
random.uniform(0, 1)


def res():
    a = test2.res()
    if a[0] > a[1]:
        return 'win'
    elif a[0] == a[1]:
        return 'even'
    else:
        return 'lose'


steps = 0

for i in range(data.shape[0]):
    if i % 10 == 0:
        print("Round %d:" % (i // 10 + 1))
    match_res = res()
    if match_res == "win":
        rank_data.loc[data['HomeTeam'][i],] += 3
    elif match_res == "even":
        rank_data.loc[data['HomeTeam'][i],] += 1
        rank_data.loc[data['AwayTeam'][i],] += 1
    else:
        rank_data.loc[data['AwayTeam'][i],] += 3

print(rank_data.sort_values(by=['Pts'], ascending=False))

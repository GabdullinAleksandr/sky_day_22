import pandas as pd
import pathlib
from pathlib import Path


def quick_sort(items):
    if len(items) <= 1:
        return items
    elem = items[0][1]
    left = list(filter(lambda x: x[1] < elem, items))
    mid = [i for i in items if i[1] == elem]
    right = list(filter(lambda x: x[1] > elem, items))
    return quick_sort(left) + mid + quick_sort(right)


def select_sorted(sort_columns='high', limit=10, order='desc', filename='dump.csv'):
    file = Path(pathlib.Path.home(), 'PycharmProjects', 'isa_sky_2.0', 'day_22', 'all_stocks_5yr.csv')
    df = pd.read_csv(file, sep=',')
    items = list(enumerate(df[sort_columns]))
    list_ = quick_sort(items)
    if order == 'asc':
        list_ = list_[: limit]
    else:
        list_ = list_[-limit:]
    with open(filename, 'w') as f:
        pass
    list_in = [i[0] for i in list_]
    df.iloc[list_in].to_csv(filename, index=False)


select_sorted(sort_columns="low", order='desc', limit=20)

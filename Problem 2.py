# Biggest Single Number

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers = my_numbers.groupby('num').size().reset_index().rename(columns={0: 'num_count'})
    my_numbers = pd.DataFrame(my_numbers[my_numbers['num_count'] == 1][['num']].max()).rename(columns={0: 'num'})
    print(my_numbers)
    return my_numbers

data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})

biggest_single_number(my_numbers)
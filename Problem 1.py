# Not Boring Movies

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    print(cinema[(cinema['id'] % 2 != 0) & (cinema['description'] != 'boring')].sort_values('rating', ascending=False))
    return cinema[(cinema['id'] % 2 != 0) & (cinema['description'] != 'boring')].sort_values('rating', ascending = False)

data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype({'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})

not_boring_movies(cinema)
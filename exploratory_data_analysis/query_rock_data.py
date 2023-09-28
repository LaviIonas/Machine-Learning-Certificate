import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

path = '../data/classic_rock.db'
con = sq3.Connection(path)

# query = ''' SELECT * FROM rock_songs; '''
#
# observations = pds.read_sql(query,con)
# print(observations.head())

query = ''' SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) AS avg_plays
            FROM rock_songs
            GROUP BY Artist, Release_Year
            ORDER BY num_songs desc;
        '''

observations = pds.read_sql(query,
                            con,
                            coerce_float=True,
                            parse_dates=['Release_Year'],
                            chunksize=5)

for index, obs in enumerate(observations):
    if index < 5:
        print(f'Observation Index: {index}'.format(index))
        print(obs)

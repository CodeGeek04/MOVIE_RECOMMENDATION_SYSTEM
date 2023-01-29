import imdb
import csv
import pandas as pd

ia = imdb.IMDb()
dict1={}

pd_dict={'Action': [], 'Adventure': [], 'Fantasy': [], 'Sci-Fi': [],
         'Animation': [], 'Comedy': [], 'Family': [], 'Mystery': [],
         'Romance': [],'Drama': [],'Crime': [], 'Thriller': [],
         'War': [], 'Musical': [], 'Biography': []}

with open("movies.csv", 'r') as file:
  csvreader = csv.reader(file)
  j=0
  for row in csvreader:
    if j==250:
        break
    if j==0:
        j=1
        continue
    name=row[1]
    items = ia.search_movie(name)
    j+=1
    print(j)
    for i in pd_dict:
        pd_dict[i].append(0)
    code = items[0].getID()
    series = ia.get_movie(code)
    genre = series.data['genres']
    for i in genre:
        if i in pd_dict:
            pd_dict[i][-1]=1


print(pd_dict)
df=pd.DataFrame(pd_dict)
df.to_csv("movies3.csv")

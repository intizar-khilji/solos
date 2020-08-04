from bs4 import BeautifulSoup
import requests, csv,datetime
import subprocess
r = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
s1 = BeautifulSoup(r,'html.parser')
n = s1.find_all('td',class_='titleColumn')
rt = s1.find_all('td',class_='ratingColumn imdbRating')
names = [name.text.replace('\n',' ').strip() for name in n]
ratings = [rating.text.strip() for rating in rt]
movie_ratings = zip(names,ratings)
movie_ratings = list(movie_ratings)
date = datetime.datetime.now().strftime('%Y%m%d')
filename = f'imdb_top_250_movies_{date}.csv'
f = open(filename,'w',newline='')
writer = csv.writer(f)
writer.writerow([datetime.datetime.now()])
writer.writerow(['Serial Number','Movie Name', 'Rating'])
k = 0
for movie_rating in movie_ratings:
    sno = movie_rating[0][0:4].replace('.','').strip()
    movie_name = movie_rating[0][6:-6].strip()
    year = movie_rating[0][-5:-1].strip()
    rating = movie_rating[1].strip()
    writer.writerow([sno,movie_name,year,rating])
    if k<10:
        print(f'{sno:5} {movie_name:50} {year:6} {rating:3}')
    k+=1
f.close()
try:
    subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',filename])
except:
    subprocess.Popen(['notepad',filename])
import requests
import pandas as pd

url = 'https://api.themoviedb.org/3/genre/movie/list?'

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NWMyYWIxODQzYTM0Y2QyMTExNTE0Y2I1Y2Y0ZjZlZCIsInN1YiI6IjY1ZDIxMjgzZGI3MmMwMDE4NjNhMDI4ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7yt6ZJxl3u-ypj_KbwbVuGbJ5rsRbuLFIiwzcVcVdUk'
}


data = []
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print('Data is crawled successfully!')
    genres = response.json().get('genres')
    for genre in genres:
        data.append(genre)
except Exception as e:
    print(f'An error occured: {str(e)}')


df = pd.DataFrame(data)
df.to_csv('genre_list.csv', index=False)
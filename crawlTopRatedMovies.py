import requests
import pandas as pd

url = 'https://api.themoviedb.org/3/movie/top_rated?'

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NWMyYWIxODQzYTM0Y2QyMTExNTE0Y2I1Y2Y0ZjZlZCIsInN1YiI6IjY1ZDIxMjgzZGI3MmMwMDE4NjNhMDI4ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7yt6ZJxl3u-ypj_KbwbVuGbJ5rsRbuLFIiwzcVcVdUk'
}

params = {
    'page': '1'
}


data = []
for i in range(1,501,1):
    params['page'] = i
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status() #raise an exception for non-200 status codes

        # process the successful response here
        print(f'Data of page {i} is crawled successfully!')
        movies = response.json().get('results')
        for movie in movies:
            data.append(movie)
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# create a DataFrame object from the data and convert it into a CSV file
df = pd.DataFrame(data)
df.to_csv('tmdb.csv', index=False)
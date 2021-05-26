
"""
    Project is in pending as the website data got converted in JS.
    Will reach back soon with required skills
"""
import bs4
import requests

# response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
# print(response.status_code)

data = open('data.html')

soup = bs4.BeautifulSoup(data, 'html.parser')
# print(soup.prettify())
#
# movies = soup.find_all(name='h3', class_='title')
# print(movies)

check = soup.find_all(name='script', id='__NEXT_DATA__')
print(check[0])





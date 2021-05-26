
import bs4
import requests

url = "https://news.ycombinator.com/show"

response = requests.get(url).text
# print(response.text)

# content = open('news.html')

soup = bs4.BeautifulSoup(response, 'html.parser')
# print(soup)

title = soup.title.text

print(title)

articles = soup.find_all('a', class_='storylink')
article_texts = []
article_links = []

for article in articles:
    article_text = article.text
    article_texts.append(article_text)
    article_link = article['href']
    article_links.append(article_link)

upvotes = [int(vote.text.split()[0]) for vote in soup.find_all('span', class_='score')]
# print(upvote_tag)

# upvotes = soup.find_all('span', class_='score')
# for vote in upvotes:
#     print(vote)

print(upvotes)
print(len(upvotes))

large_num = max(upvotes)
print(large_num)

num_index = upvotes.index(large_num)
print(num_index)

print(article_texts[num_index])
print(article_links[num_index])
#
# print(article_links)
# print(len(article_links))
#
# print(article_texts)
# print(len(article_texts))






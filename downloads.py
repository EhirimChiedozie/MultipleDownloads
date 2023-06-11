import requests
import bs4
url = 'https://www.w3schools.com/css/css_intro.asp'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:109.0) Gecko/20100101 Firefox/110.0'}
source = requests.get(url,headers=headers)
soup = bs4.BeautifulSoup(source.text,'lxml')
topics = soup.find('div',id='leftmenuinnerinner')
a_tags = topics.find_all('a')
links = [link['href'] for link in a_tags]
for topic in links:
    content = requests.get('https://www.w3schools.com/css/'+topic,headers=headers)
    html_file = open(f'{topic[:-4]}.html','w')
    html_file.write(content.text)
    html_file.close()
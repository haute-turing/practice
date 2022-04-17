import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page=response.text

soup=BeautifulSoup(rating_page,'html.parser')

program_title_tags=soup.select('td.program')

for tag in (program_title_tags):
  print(tag.get_text())

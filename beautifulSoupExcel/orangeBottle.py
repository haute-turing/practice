import requests
from bs4 import BeautifulSoup

response = requests.get('https://workey.codeit.kr/orangebottle/index')
soup = BeautifulSoup(response.text, 'html.parser')

branch_infos=[]
for branchTag in soup.select('div.branch'):
  branch = list((branchTag.select_one('div.branch')).stripped_strings)
  branch_infos.append([branch[0],branch[1],branch[2],branch[3]])

print(branch_infos)
'GHOST'

import requests
from bs4 import BeautifulSoup

def  login(uid, password):
    headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    login_data={'username':uid,'password':password}
 
    with requests.Session() as s:
        url=url='http://172.16.2.1:1000/login?'
        r=s.get(url,headers=headers)
        soup=BeautifulSoup(r.content,'lxml')
        login_data['magic']=soup.find('input',attrs={'name':'magic'})['value']
        r=s.post(url,data=login_data,headers=headers)

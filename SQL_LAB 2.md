Link: https://portswigger.net/web-security/sql-injection/lab-login-bypass

![image](https://github.com/user-attachments/assets/f108bdb9-608c-487e-8dde-eaae3c658741)

Backend_query= SELECT username FROM users WHERE username="admin" and password="admin"

Given_user = administrator 

Goal= We have to login using sql injection on login page.

![image](https://github.com/user-attachments/assets/f7c64ac5-93f3-4814-9dfd-cec749c15cfe)


We have to perfrom sql injection on above page

Note : In this way user_name should be already know to us (given by lab).


![image](https://github.com/user-attachments/assets/da424a0b-f11c-4d9c-a9fd-bd00aba66a3f)

![image](https://github.com/user-attachments/assets/656229d7-068d-4786-9579-184d1f564821)

Another Sql injection
 
 Note: this way is much easier and we dont need user_name and password to login becuase of   “ OR ” operator 
 because , in OR operator if any one condition becomes true whole query becomes true.
 
 i.e   1=1     always True

 ![image](https://github.com/user-attachments/assets/f1bac559-38b8-48c1-a24d-602fe43ce9a7)

![image](https://github.com/user-attachments/assets/ca9396fa-8b35-4b07-98f5-d268de96f252)


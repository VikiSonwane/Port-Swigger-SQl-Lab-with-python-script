Link: https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column

![image](https://github.com/user-attachments/assets/8bc55a8f-f844-4a33-a877-742a679cb18c)


Goal: Retrieving multiple values in a single column. and find credentials of all users and login  as a administrator.
Given : 
table_name= users
column_name= username, password

we will learn in this lab contamination of strings  and and what is the sql database we are using.

as the previous labs we will divide our work in step for easy to learn process.

step 1 : Finding number of columns.

We can find number of columns by using  ORDER BY   query by inserting in to vulnerable field.

query = ' order by 1 --

![image](https://github.com/user-attachments/assets/8d685f83-75b4-4092-9b60-abc1cf26e6b5)

but this column is not show in the browser it must is most likely that is use for id or any type of ordering system for database.

query = ' order by 2 --

![image](https://github.com/user-attachments/assets/3290403e-c7a0-4fca-ae05-ce9dbd06f11b)

![image](https://github.com/user-attachments/assets/bdccb67b-2001-4bbe-aaf1-278da7fa54af)


when we use our query it order the data by alphabetical order. means it is display on browser.

query = ' order by 3 --

![image](https://github.com/user-attachments/assets/0e39f0da-dd6a-4d53-bc4b-43359300d49a)


when try to order by third column we got <error> means that there is no 3rd column.

number_of_column =  3-1 = 2




step 2 : finding which column support string/text datatype.



In previous step we got number of column = 2 then next step is to find which column supports string / text data type.

we can do that using  UNION SELECT  query.

query = 'union select null,null -- 

![image](https://github.com/user-attachments/assets/92c0873e-98de-467b-9ca3-db98b41e4a6e)


In order to find which column returns string/text datatype we need to replay null value with any string if it does not throw error and data display on browser then we have find out the column.

query = 'union select 'text1',null -- 

![image](https://github.com/user-attachments/assets/a12b503e-d467-4f3f-a53d-7184fe21238d)
![image](https://github.com/user-attachments/assets/e9a690b2-87e1-4d27-84fe-d5712a0eaa2a)


Note *** it was pretty dumb to check first column because not show on browser if it also support string value this will not helpful to us **** 

query = 'union select null,'text2' -- 

![image](https://github.com/user-attachments/assets/e3eef946-ca34-4b3f-b54d-cacebf59e6ed)

![image](https://github.com/user-attachments/assets/42c7c553-c1a4-4121-b3ac-a8e1e26ead51)


and we found or column which support string value.


step 3 : retrieving data from column.

since we have only one column which support string value. 
Here we have two ways to retrieve data from column 

1st way : retrieve data column by column one by one (means retrieve username first and then find password  column .

**** note table_name and column is given in the lab we did not find that ****

query: 'union select null,username from users -- 

![image](https://github.com/user-attachments/assets/fef55c00-ef9b-48bc-9f01-a9de60725677)

retrieve username:

![image](https://github.com/user-attachments/assets/3fe359bc-3569-4fe2-9dfd-9347c608d1c2)


same thing we will do for password as well.

![image](https://github.com/user-attachments/assets/79d15901-d5fa-409a-80b9-aa1a5c85af11)

retrieved password :

![image](https://github.com/user-attachments/assets/6b5a2459-e652-4852-9113-b623e70f2b97)


2nd way (preferred way ) : concatenating both column in to a single column and then retrieve data .

this is the different ways to concatenate string depending on which data base you are using.
**** here our problem arises i.e we don't know what's our data base is ***

![image](https://github.com/user-attachments/assets/c223a82d-4ebe-4d9d-804d-586d0e415484)

we can also find which type of data base we are working on by using below cheat sheet.
![image](https://github.com/user-attachments/assets/56afa7c3-b768-4eaa-9d8f-3c53c7cf8911)


lets try some of query.
first i will try Microsoft.

query : 'union select null,@@version -- 

![image](https://github.com/user-attachments/assets/d4b44949-6fbd-47af-b4cc-480270da476a)


and we got error which means Microsoft is not our database type.


now will try with postgreSQL 
query= ' union select null, version() -- 


![image](https://github.com/user-attachments/assets/27da2897-d911-435b-9797-3b33da4b0278)


and we found the database and version and other useful information.
*** this helped use in long run now we know which type query we have to use instead trying all query ***

now we know that we are using postgreSQL database we can use string concatenation to retrieve the data.

![image](https://github.com/user-attachments/assets/0e111790-4e29-4422-a390-c0d2a6f92cf0)

query =' union select null,username ||':'|| password from users -- 

![image](https://github.com/user-attachments/assets/326b5033-1ba0-4286-aaee-35a7d749346d)
![image](https://github.com/user-attachments/assets/2edd412e-2dc5-4070-8307-5d63dc10e5b9)



step 4 : login as a administrator with retrieved credentials .

using above credentials we login as administrator 

Note *** this lab in real life password is hashed  we can not directly login with hashed password *** 

![image](https://github.com/user-attachments/assets/3c6ea968-73af-470d-a1cd-875ea0d609d1)


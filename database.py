import pymysql
from tkinter import messagebox 
##command for the crud operations inside the mysql database
def connect_database():
  global mycursor,conn
  try:
#connecting with the database
    conn=pymysql.connect(host='localhost',user='root',password='rajdeeps@2003')
    mycursor=conn.cursor()
  except:
    messagebox.showerror(title='Error',message='Something went wrong,Please open mysql app before running again')
    return 
##execute the sql code 
  mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
  mycursor.execute('USE employee_data')
  mycursor.execute('CREATE TABLE IF NOT EXISTS data(Id VARCHAR(20),Name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(50),Gender VARCHAR(20),Salary DECIMAL(10,2))')
#decimal(10,2) means 10 is the size and it can store upto 2 decimal places 
#if not is used because we doesnot want to create database and table again and again during each execution
  
def insert(id,name,phone,role,gender,salary):
  mycursor.execute('INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))  
#variable defined in the next tuple will replace the %s 
  conn.commit()
#after the conn.commit data will be inserted only it's mandatory

def id_exists(id):
  mycursor.execute('SELECT COUNT(*) FROM data WHERE id= %s',id)
  result=mycursor.fetchone()
  return result[0]>0

def fetch_employees():
  mycursor.execute('SELECT * from data')
  result=mycursor.fetchall()
  return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
  mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s where id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
  conn.commit()

def delete(id):
  mycursor.execute("DELETE FROM data WHERE id=%s",id)
  conn.commit()

def search(option,value):
  mycursor.execute(f"SELECT * FROM data WHERE {option}=%s",value)
  result=mycursor.fetchall()
  return result

def deleteall_records():
  mycursor.execute('TRUNCATE TABLE data') 
  conn.commit()
connect_database()

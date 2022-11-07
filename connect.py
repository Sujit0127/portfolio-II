#!C:\Users\Personal\AppData\Local\Programs\Python\Python37
print("Content-Type:text/html")
print()
import cgi

print("<h1>Welcome to Python<h1>")
print("<hr/>")
print("<h1>Using input tag</h1>")
print("<body bgcolor='red'>")

form=cgi.FieldStorage()

name=form.getvalue("name")
email=form.getvalue("email")
phone=form.getvalue("phone")
project=form.getvalue("project")
message=form.getvalue("message")

import mysql.connector

con=mysql.connector.connect(user='root',password='',host='localhost',database='test')
cur=con.cursor()

cur.execute("insert into porfolio values(%s,%s,%i,%s,%s)",(name,email,phone,project,message))
con.commit()

cur.close()
con.close()
print("<h3>Message INserted Successfully</h3>")
print("<a href='index.html'> click here to go back</a>")
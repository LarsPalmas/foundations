#!/usr/bin/env python3
 
#A simple script to accept input from an HTML form,
#parse the information and do something.
#In this case is to give user feedback with a simple HTML page.
 
#use python´s Common Gateway Interface
import cgi
 
#get the outpuut of the form
form = cgi.FieldStorage()
 
#get an input from the form called 'name'
#and assign it´s value to a local variable called v_name
v_name = form.getvalue('name')
#v_name = "Test"
 
#send an HTML response
print("""
<html>
<head>
  <title>Hey, there! Thanks for submitting!</title>
</head>
<body>
  <h1>Hello, {}!</h1>
</body>
</html>""".format(v_name))

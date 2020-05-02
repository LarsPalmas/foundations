def makePage():
    file = open("myUsernamePage.html", "wt")
    file.write(""" <!DOCTYPE html>
    
<html>
<head>
<title>my first blog page</title>
</html>
</head>
<body>
    <h1>Hello {}</h1>

    <form>
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname">
        <input type="submit" value="Submit">
    </form>

</body>
</html>""")
#.format(inputName))
    file.close()

#inputName = input("Enter your name:")
makePage()
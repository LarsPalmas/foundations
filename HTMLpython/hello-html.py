import webbrowser

f = open('username.html','wb')

inputName = input("Enter your name:")
print("Hello, " + inputName)

message = """<html>
<head></head>
<body><p>Hello {username}!</p></body>
</html>""".encode()

new_message = message.format(username=inputName)
f.write(new_message)
f.close()
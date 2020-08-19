from socket import *

sockfd = socket()
sockfd.bind(("0.0.0.0",8889))
sockfd.listen(5)
connfd,addr = sockfd.accept()

data = connfd.recv(1024)
print(data.decode())

html = "HTTP/1.1 200 OK\r\n"
html += "Content-Type:text/html\r\n"
html += "\r\n"
with open("132.html") as a:
    html += a.read()
connfd.send(html.encode())

sockfd.close()
connfd.close()
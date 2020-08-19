from socket import *
from select import select

"""主要功能 ： 【1】 接收客户端（浏览器）请求

【2】 解析客户端发送的请求

【3】 根据请求组织数据内容

【4】 将数据内容形成http响应格式返回给浏览器

特点 ： 【1】 采用IO并发，可以满足多个客户端同时发起请求情况

【2】 通过类接口形式进行功能封装

【3】 做基本的请求解析，根据具体请求返回具体内容，同时处理客户端的非网页请求行为"""


class WebServer:
    def __init__(self, host="0.0.0.0", port=8080, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    def main(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)

            for r in rs:
                if r is self.sock:
                    connfd, addr = rs[0].accept()
                    print("Connect from", addr)
                    connfd.setblocking(False)
                    self.rlist.append(connfd)
                else:
                    data = r.recv(1024*10).decode()
                    print(data)



if __name__ == '__main__':
    ws = WebServer(host="0.0.0.0", port=8888, html="./static")
    ws.main()

import socket
import multiprocessing


class DataTreating(object):

    def __init__(self):
        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定并复用端口
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server_socket.bind(("", 8080))

        # 监听
        self.tcp_server_socket.listen(128)

    def client_accept(self):
        # 等待用户连接
        self.client_socket, self.ip_port = self.tcp_server_socket.accept()
        print("新连接的客户端:", self.ip_port)

    def server_recv(self):
        while True:
            # 循环接收数据
            self.recv_data = self.client_socket.recv(1024).decode("gbk")
            if self.recv_data:  # 判断接收数据是否为空
                print("来自%s的数据:%s" % (self.ip_port, self.recv_data))
            else:
                print("%s已断开连接!" % (self.ip_port,))
                self.client_socket.close()
                self.tcp_server_socket.close()
                return

    def server_send(self):
        while True:
            try:
                send_input = input().encode("UTF-8")
                self.client_socket.send(send_input)
            except Exception as exc:
                pass

    def run(self):
        while True:
            self.client_accept()
            multiprocessing.Process(target=self.server_recv).start()
            multiprocessing.Process(target=self.server_send).start()


def main():

    class_data = DataTreating()
    class_data.run()


if __name__ == '__main__':
    main()

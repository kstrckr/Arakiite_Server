import socketserver

class ArakiiteHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        self.request.sendall(self.data.upper())

        if self.data == "stop":
            self.server().stop()


if __name__ == "__main__":
    HOST_IP, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST_IP, PORT), ArakiiteHandler) as server:
        server.serve_forever()


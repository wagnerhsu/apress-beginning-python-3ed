import socket

s = socket.socket()

# host = socket.gethostname()
host = "0.0.0.0"
port = 1234
print(f"{host} : {port}")
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send(b"Thank you for connecting")
    c.close()

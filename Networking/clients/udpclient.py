import socket

target_host = "127.0.0.1"
target_port = 9997

#creation of a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#connecting the client

client.connect((target_host,target_port))

# send some data
client.sendto(b"Here's some data", (target_host, target_port))

#receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
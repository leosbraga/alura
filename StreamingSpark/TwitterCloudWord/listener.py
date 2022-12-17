import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.bind((HOST, PORT))
print(f'Waiting conection on {PORT} port')

s.listen(5)
conn, address = s.accept()

print(f'Receiving request from {address}')

messages = [
    'message a',
    'message b',
    'message c',
    'message d',
    'message e',
    'message f',
    'ctrl+c to finish'
]

for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(4)

conn.close()
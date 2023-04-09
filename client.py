import socket

host = 'localhost'
port = 8000

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.connect((host, port))

arr = input("Enter the array (space-separated): ")
print("Enter the sorting type:")
sort_type = input("bubble/selection/merge/quick: ")

with open('input.txt', 'w+') as f:
    f.write(sort_type)
    f.write('\n')
    f.write(arr)
    f.close()

with open('input.txt', 'r') as f:
    data = f.read()
    c.send(data.encode('utf-8'))
    f.close()

with open('output.txt', 'w+') as f:
    while True:
        data = c.recv(1024)
        l = data.decode('utf-8')
        f.write(l)
        if not data:
            break
    f.close()

with open('output.txt', 'r') as f:
    sorted_array = f.read()
print('Sorted array:', sorted_array)

c.close()
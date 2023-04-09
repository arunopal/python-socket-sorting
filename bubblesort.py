import socket
b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b.bind(('localhost', 8001))
print('Bubble sort server created')
print('Waiting for connection...')
b.listen(1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def handle_connection(server, addr):
    data = server.recv(1024).decode('utf-8')
    array = list(map(int, data.split(' ')))
    print('Received array:', array)
    sorted_array = bubble_sort(array)
    print('Sorted array:', sorted_array)
    sorted_array_str = ' '.join(map(str, sorted_array))
    print('Sending sorted array to server', addr, '...')
    server.send(sorted_array_str.encode('utf-8'))
    print('Sent')

while True:
    server_socket, server_addr = b.accept()
    print('Server with address', server_addr, 'connected')
    handle_connection(server_socket, server_addr)
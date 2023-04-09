import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8002))
print('Selection sort server created')
print('Waiting for connection...')
s.listen(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def handle_connection(server, addr):
    data = server.recv(1024).decode('utf-8')
    array = list(map(int, data.split(' ')))
    print('Received array:', array)
    sorted_array = selection_sort(array)
    print('Sorted array:', sorted_array)
    sorted_array_str = ' '.join(map(str, sorted_array))
    print('Sending sorted array to server', addr, '...')
    server.send(sorted_array_str.encode('utf-8'))
    print('Sent')

while True:
    server_socket, server_addr = s.accept()
    print('Server with address', server_addr, 'connected')
    handle_connection(server_socket, server_addr)
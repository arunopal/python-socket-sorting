import socket
q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
q.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
q.bind(('localhost', 8004))
print('Quick sort server created')
print('Waiting for connection...')
q.listen(1)

def partition(array, low, high):
    pivot = array[high]
    i = low-1
    for j in range(low, high):
        if(array[j] <= pivot):
            i = i+1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i+1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi+1, high)

def handle_connection(server, addr):
    data = server.recv(1024).decode('utf-8')
    array = list(map(int, data.split(' ')))
    print('Received array:', array)
    quick_sort(array, 0, len(array)-1)
    print('Sorted array:', array)
    sorted_array_str = ' '.join(map(str, array))
    print('Sending sorted array to server', addr, '...')
    server.send(sorted_array_str.encode('utf-8'))
    print('Sent')

while True:
    server_socket, server_addr = q.accept()
    print('Server with address', server_addr, 'connected')
    handle_connection(server_socket, server_addr)
import socket
import threading

host = 'localhost'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen()
print(f'Server created and listening at {port}')

def handle_client(client_socket, client_addr):
    data = client_socket.recv(1024)
    sorting_type, array_str = data.decode('utf-8').split('\n')
    array = list(map(int, array_str.split(' ')))
    print('Sorting type:', sorting_type)
    print('Given array:', array, "Length:", len(array))
    print('Connection closed to', client_addr)
    sorted_array = send_to_sorting_server(sorting_type, array_str)
    print('Sorted array:', sorted_array)
    print('Array sorted. Sending to client', client_addr, '...')
    client_socket.sendall(sorted_array.encode('utf-8'))
    client_socket.close()
    print('Connection closed to', client_addr)


def send_to_sorting_server(sort_type, array_str):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sort_type == 'bubble':
        s1.connect(('localhost', 8001))
        print('Connected to bubble sort server')
        print('Sending given array...')
        s1.send(array_str.encode('utf-8'))
        sorted_array = s1.recv(1024).decode('utf-8')
        return sorted_array
    elif sort_type == 'selection':
        s1.connect(('localhost', 8002))
        print('Connected to selection sort server')
        print('Sending given array...')
        s1.send(array_str.encode('utf-8'))
        sorted_array = s1.recv(1024).decode('utf-8')
        return sorted_array
    elif sort_type == 'merge':
        s1.connect(('localhost', 8003))
        print('Connected to merge sort server')
        print('Sending given array...')
        s1.send(array_str.encode('utf-8'))
        sorted_array = s1.recv(1024).decode('utf-8')
        return sorted_array
    elif sort_type == 'quick':
        s1.connect(('localhost', 8004))
        print('Connected to quick sort server')
        print('Sending given array...')
        s1.send(array_str.encode('utf-8'))
        sorted_array = s1.recv(1024).decode('utf-8')
        return sorted_array
    else:
        print('Invalid choice') 

while True:
    client_socket, client_addr = s.accept()
    print('Client with address', client_addr, 'connected')
    thread = threading._start_new_thread(handle_client, (client_socket, client_addr))
import socket
m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
m.bind(('localhost', 8003))
print('Merge sort server created')
print('Waiting for connection...')
m.listen(1)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

def handle_connection(server, addr):
    data = server.recv(1024).decode('utf-8')
    array = list(map(int, data.split(' ')))
    print('Received array:', array)
    sorted_array = merge_sort(array)
    print('Sorted array:', sorted_array)
    sorted_array_str = ' '.join(map(str, sorted_array))
    print('Sending sorted array to server', addr, '...')
    server.send(sorted_array_str.encode('utf-8'))
    print('Sent')

while True:
    server_socket, server_addr = m.accept()
    print('Server with address', server_addr, 'connected')
    handle_connection(server_socket, server_addr)
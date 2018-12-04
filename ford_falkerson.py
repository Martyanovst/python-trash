import collections
import queue


def read_int():
    return int(input())


def read_adjancency_array(x_size):
    array_size = read_int()
    array = list(map(int, input().split()))
    indexes = array[:x_size]
    lengths = []
    for i in range(x_size - 1):
        if array[i] == 0:
            lengths.append(0)
            continue
        j = i + 1
        while array[j] == 0:
            j += 1
        lengths.append(array[j] - array[i])
    lengths.append(array_size - array[x_size - 1] + 1)
    tmp_array = []
    for i in range(x_size):
        tmp_array.append(array[indexes[i] - 1:indexes[i] - 1 + lengths[i]])
    return tmp_array


def build_graph(adjancency_array, x_size, y_size):
    matrix = collections.defaultdict(list)
    matrix['s'] = ['x' +str(i + 1) for i in range(x_size)]
    for i in range(len(adjancency_array)):
        x_node = adjancency_array[i]
        x = 'x' + str(i+1)
        y_nodes = list(map(lambda y: 'y' + str(y), x_node))
        matrix[x] = y_nodes
    for y in range(1, y_size):
        matrix['y' + str(y)] = ['t']
    return matrix


def bfs(graph, frm, to, source):
    q = queue.Queue()
    q.put(frm)
    previous = {}
    visited = {frm}
    while q.qsize() > 0:
        current_node = q.get()
        if current_node == to:
            break
        for node in graph[current_node]:
            if node not in visited:
                q.put(node)
                previous[node] = current_node
                visited.add(node)
    current = previous[to]
    chain = [to, current]
    while current != frm:
        current = previous[current]
        chain.append(current)
    return reversed(chain)


def ford_falkerson(graph):
    bfs(graph, 's', 't'))


if __name__ == '__main__':
    x_size = read_int()
    y_size = read_int()
    adjancency_array = read_adjancency_array(x_size)
    print(adjancency_array)
    graph = build_graph(adjancency_array, x_size, y_size)
    print(graph)
    greatest_stream = ford_falkerson(graph)

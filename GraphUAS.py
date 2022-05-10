graph = {'A': ['B', 'C'] , 'B': ['C'] , 'C': ['A','D'] , 'D': ['B','A']}



def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:

        return path

    if start not in graph:

        return None

    for node in graph[start]:

        if node not in path:

            newpath = find_path(graph, node, end, path)

            if newpath:

                return newpath

    return None



def find_all_paths(graph, start, end, path=[]):

    path = path + [start]

    if start == end:

        return [path]

    if start not in graph:

        return []

    paths = []

    for node in graph[start]:

        if node not in path:

            newpaths = find_all_paths(graph, node, end, path)

            for newpath in newpaths:

                paths.append(newpath)

    return paths



def find_shortest_path(graph, start, end, path=[]):

    path = path + [start]

    if start == end:

        return path

    if start not in graph:

        return None

    shortest = None

    for node in graph[start]:

        if node not in path:

            newpath = find_shortest_path(graph, node, end, path)

            if newpath:

                if not shortest or len(newpath) < len(shortest):

                    shortest = newpath

    return shortest



def find_longest_path(graph, start, end, path=[]):

    path = path + [start]

    if start == end:

        return path

    if start not in graph:

        return None

    longest = None

    for node in graph[start]:

        if node not in path:

            newpath = find_longest_path(graph, node, end, path)

            if newpath:

                if not longest or len(newpath) > len(longest):

                    longest = newpath

    return longest



print(find_path(graph, 'A', 'D'))

print(find_all_paths(graph, 'A', 'D'))

print(find_shortest_path(graph, 'A', 'D'))

print(find_longest_path(graph, 'A', 'D'))




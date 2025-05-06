def bfs(n, m, edges, s):
    # Write your code here
    adj_list = {}
    
    for node in range(1,n+1):
        adj_list[node] = []
        
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    start = s
    
    from collections import deque
    
    to_do_list = deque()
    to_do_list.append(start)
    
    distance = {}
    for node in range(1,n+1):
        distance[node] = -1
        
    distance[start] = 0
    
    visited = {}
    visited[start] = True
    
    while True:
        if len(to_do_list) == 0:
            break
            
        current = to_do_list.popleft()
        
        for neighbor in adj_list[current]:
            if neighbor not in visited:
                visited[neighbor] = True
                to_do_list.append(neighbor)
                distance[neighbor] = distance[current] + 1
                
    result = []
    
    for node in distance:
        if node == start:
            continue
        if distance[node] != -1:
            distance[node] = distance[node] * 6
            
        result.append(distance[node])
        

    return result

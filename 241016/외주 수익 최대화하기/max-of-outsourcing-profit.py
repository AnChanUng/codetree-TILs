n = int(input())
graph = []
for i in range(n):
    n, p = map(int, input().split())
    graph.append([n, p])

max_sum_t = 0
for i in range(len(graph)):
    sum_n = 0
    sum_t = 0
    for j in range(i, len(graph)):
        if sum_n <= n:  
            sum_n += graph[j][0]
            sum_t += graph[j][1]
        #print("sum_n", sum_n)
        #print("sum_t", sum_t)
    max_sum_t = max(max_sum_t, sum_t)

print(max_sum_t)
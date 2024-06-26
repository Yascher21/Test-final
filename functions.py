# Градиентный спуск
import numpy as np

# Пример функции потерь: J = (theta - 3)^2
def cost_function(theta):
    return (theta - 3)**2

# Производная функции потерь
def gradient(theta):
    return 2 * (theta - 3)

# Параметры
theta = 0.0  # Начальное значение параметра
learning_rate = 0.1  # Скорость обучения
num_iterations = 100  # Количество итераций

for i in range(num_iterations):
    grad = gradient(theta)
    theta = theta - learning_rate * grad
    print(f"Iteration {i+1}: theta = {theta}, cost = {cost_function(theta)}")


# Поиск в глубину
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

dfs(graph, 'A')


# Поиск в ширину
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

bfs(graph, 'A')


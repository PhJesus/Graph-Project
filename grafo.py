import numpy as np

with open('grafo.txt', 'r') as f:
  content = f.read()

contentArray = content.split('\n')

qtdVertices = int(contentArray.pop(0))
arestas = contentArray

def criarMatrizAdjacencia(numVertices, arrArestas):
  matriz = np.zeros((numVertices, numVertices), dtype=int)

  for i in arrArestas:
    vertice1 = int(i.split(' ')[0]) - 1
    vertice2 = int(i.split(' ')[1]) - 1
    matriz[vertice1][vertice2] = 1
    matriz[vertice2][vertice1] = 1

  return matriz

representacao = criarMatrizAdjacencia(qtdVertices, arestas)

def grauMinimo(matriz):
  menor = len(matriz) + 1
  for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz)):
      soma += matriz[i][j]

    if (soma < menor):
      menor = soma

  return menor

def grauMaximo(matriz):
  maior = 0
  for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz)):
      soma += matriz[i][j]

    if (soma > maior):
      maior = soma
        
  
  return maior

print("Vertices: ", qtdVertices)
print("Arestas: ", len(arestas))
print("Grau Mínimo: ", grauMinimo(representacao))
print("Grau Máximo: ", grauMaximo(representacao))
print(representacao)

inferno = input("De qual vértice iniciará a busca em largura? ")

graph = dict()
def addEdge(node1, node2):
  if node1 not in graph:
      graph[node1] = []

  if node2 not in graph:
      graph[node2] = []

  graph[node1].append(node2)

for i in arestas:
  node1 = i.split(' ')[0]
  node2 = i.split(' ')[1]
  addEdge(node1, node2)
  addEdge(node2, node1)

def bfs(graph, node): #function for BFS
  visited = []
  queue = []
  visited.append(node)
  queue.append(node)

  resultado = []
  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 
    resultado.append(m)

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return resultado

caminho = bfs(graph, inferno)

if (len(caminho) != qtdVertices):
  print("\nExiste componentes desconexos")
else:
  print("\nNão existe componentes desconexos")
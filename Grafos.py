from heap import HeapMin

class Grafos():
    def __init__(self) -> None:
        print()
        print("=================================")
        print("1 - Criar um a matriz")
        print("2 - Exibir a matriz")
        print("3 - Inserir valor na matriz")
        print("4 - Inserir grafo automaticamente")
        print("5 - Dijkstra")
        print("6 - Sair do programa")
        print("=================================")
        self.opcao = input("Selecione uma opcao acima: ")
        if(self.opcao == "1"):
            self.ordem = int(input("Selecione o valor da matriz: "))
            self.criar_matriz()
        elif(self.opcao == "2"):
            self.exibir_matriz()
        elif(self.opcao == "3"):
            self.lin = int(input("Digite o valor da linha: "))
            self.col = int(input("Digite o valor da coluna: "))
            self.value = int(input("Digite o valor a ser inserido: "))
            self.insert_value()
        elif(self.opcao == "4"):
            self.insert_grafo()
        elif(self.opcao == "5"):
            self.vertices = int(input("Digite a quantidade de vertices: "))
            self.origem = int(input("Digite a origem: "))
            print(self.dijkstra())
            
        elif(self.opcao == "6"):
            quit()
    
    def criar_matriz(self):
        self.matriz = [[0] * self.ordem for i in range(self.ordem)]
        self.__init__()
            
    def exibir_matriz(self):
        list_cab = []
        k = 1
        i = 1
        j = 1
        print("   ", end='')
        for k in range(self.ordem):
            list_cab.append(k)
            print(f"0{list_cab[k] +1}", end=" ")
        print()
        for i in range(self.ordem):
            if i < 10:
                print(f"0{i+1}", end=" ")
            else:
                print(f"{i+1}", end=" ")
            for j in range(self.ordem):
                if(i==j):
                    print('XX', end=' ')
                elif(self.matriz[i][j]<10):
                    print(f"0{self.matriz[i][j]}", end=' ')
                else:
                    print(self.matriz[i][j], end=" ")
            print()
        self.__init__()
    
    def insert_value(self):
        self.matriz[self.lin-1][self.col-1] = self.value
        self.__init__()

    def insert_grafo(self):
        self.adiciona_aresta(1, 2, 5)
        self.adiciona_aresta(1, 3, 6)
        self.adiciona_aresta(1, 4, 10)
        self.adiciona_aresta(2, 5, 13)
        self.adiciona_aresta(3, 4, 3)
        self.adiciona_aresta(3, 5, 11)
        self.adiciona_aresta(3, 6, 6)
        self.adiciona_aresta(4, 5, 6)
        self.adiciona_aresta(4, 6, 4)
        self.adiciona_aresta(5, 7, 3)
        self.adiciona_aresta(6, 7, 8)
        self.__init__()        
    
    def adiciona_aresta(self, u, v, peso):
        self.matriz[u-1][v-1] = peso
        self.matriz[v-1][u-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.matriz[i])

    def dijkstra(self):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[self.origem - 1] = [0, self.origem]
        h = HeapMin()
        h.adiciona_no(0, self.origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.matriz[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.matriz[v-1][i]:
                        custo_vem[i] = [dist + self.matriz[v-1][i], v]
                        h.adiciona_no(dist + self.matriz[v-1][i], i+1)
        return custo_vem
    
if __name__=="__main__":
    Grafos()
            
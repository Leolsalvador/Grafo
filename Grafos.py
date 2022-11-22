class Grafos():
    def __init__(self) -> None:
        print("1 - Criar um a matriz")
        print("2 - Exibir a matriz")
        print("5 - Sair do programa")
        self.opcao = input("Selecione uma opcao acima: ")
        if(self.opcao == "1"):
            self.ordem = int(input("Selecione o valor da matriz: "))
            self.criar_matriz()
        elif(self.opcao == "2"):
            self.exibir_matriz()
        elif(self.opcao == "5"):
            quit()
    
    def criar_matriz(self):
        self.matriz = [[0] * self.ordem for i in range(self.ordem)]
        self.__init__()
            
    def exibir_matriz(self):
        k = 1
        i = 1
        j = 1
        for k in range(self.ordem):
            
        for i in range(self.ordem):
            for j in range(self.ordem):
                if(j == self.ordem - 1):
                    print(f"0{self.matriz[i][j]}")
                else:
                    print(f"0{self.matriz[i][j]}", end = " ")
        print()
        self.__init__()

if __name__=="__main__":
    Grafos()
            
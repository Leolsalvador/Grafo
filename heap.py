class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def mostra_heap(self):
        print('A estrutura heap é a seguinte:')
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end='  ')
                a += 1
            print('')
        for i in range(self.nos-a):
            print(f'{self.heap[a]}', end='  ')
            a += 1
        print('')

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x

    def tamanho(self):
        return self.nos
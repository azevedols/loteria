class Loteria:
    def __init__(self, numero):
        self.numero = numero

    def getNumero(self):
        return self.numero

    def verificaIgualdades(self, sorteio):
        repetido = 0
        digitado = []
        sorteios = []
        digitado = retiraEspVazio(self.numero)
        sorteios = retiraTabulacao(sorteio)

        if int(digitado) == int(sorteios):
            repetido = repetido + 1
        
        return repetido
    
    def __retiraTabulacao(lista):
        # Método utilizado para retirar tabulação do arquivo importado.
        novaLista = []
        dado = lista.strip()
        dado1 = dado.split('\t')
        dado1.sort(key=int)

        for item in dado1:
            novaLista.append(item)

        return novaLista

    def __retiraEspVazio(lista):
        # Método utilizado para retirar espaço vazio dos número informado pelo usuário.
        novaLista = []
        dado = lista.strip()
        dado1 = dado.split(' ')
        dado1.sort(key=int)

        for item in dado1:
            novaLista.append(item)
        
        return novaLista

    def importaArquivo(self):
        arquivo = input('Digite o nome do arquivo que deseja importar: ')

        f = open(arquivo, 'r')

        return f

    def __gravarArquivo(self, jogoSalvo):
        externo = input('Digite o nome do arquvio de deseja criar: ')
        externo + '.txt'
        gravarNumero = open(externo, 'w')
        gravarNumero.write(str(jogoSalvo))
        gravarNumero.close()

    def __testaJogo(self):
        dado = getNumero
        pares = 0
        impares = 0
        dado = dado.strip()

        for item in dado.split(' '):
            if verificaSeEhNumero(item):
                if int(item) % 2 == 0:
                    pares = pares + 1
                else:
                    impares = impares + 1
        
        if pares > 9 or impares > 9:
            return False
        else:
            return True

    def __verificaSeEhNumero(self, dados):
        if type(int(dados)) == int:
            return True
        else:
            return False

    def __removeCaracter(texto):
        if '»¿' in texto:
            novaLinha = texto[3:]
        else:
            novaLinha = texto

        return novaLinha

    def __verificaSeqCresc(self):
        x = 0
        flag = 1
        dado = jogo.strip()
        crescente = dado.split(' ')
        crescente.sort(key=int)

        for i in crescente:
            if int(flag) == int(i):
                flag = flag + 1
                x = x + 1
                if x == 5:
                    return False
            else:
                return True

    def __verificaSeqDecr(self):
        x = 0
        flag = 25
        dado = jogo.strip()
        crescente = dado.split(' ')
        crescente.sort(key=int, reverse=True)

        for i in crescente:
            if int(flag) == int(i):
                flag = flag - 1
                x = x + 1
                if x == 5:
                    return False
            else:
                return True
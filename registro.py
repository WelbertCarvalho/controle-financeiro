class Registro:
    def __init__(self, tipo):
        self.tipo = tipo
        self.descricao = ''
        self.valor = ''


    #Imprime as informações do cabeçalho
    @staticmethod
    def cabecalho(tipo):
        tracej_padrao = '-' * 30
        titulo = (tracej_padrao + tipo.upper() + tracej_padrao)
        linha = '-' * len(titulo)
        print(linha)
        print(titulo)
        print(linha)


    #Leitura da descrição - retorna a string
    def descricao_lanc(self):
        valida = False
        while not valida:
            descricao = input('Informe o nome do registro: ').strip().lower()
            if descricao == '':
                print('É necessário dar um nome ao registro!')
            else:
                valida = True
                self.descricao = descricao


    #Leitura do valor - retorna um float 
    def valor_lanc(self):
        valida = False
        while not valida:
            valor = input('Informe o valor de ' + self.descricao.title() + ': ')
            if valor == '':
                print('É preciso informar um valor para ' + self.descricao.title())
            else:
                try:
                    valor = float(valor)
                    if valor <= 0:
                        print('O valor deve ser maior que 0.')	
                    else:
                        valida = True
                        self.valor = valor
                except:
                    print('Este campo só aceita valores numéricos!')


    #Pergunta se deseja lançar mais registros
    def continuar_lancamentos(self):
        valida = False
        while not valida:
            continuar = input('Deseja lançar mais registros?(s/n): ').lower()
            if continuar == '':
                print('Este campo deve ser preenchido!')
            elif (continuar == 's') | (continuar == 'n'):
                valida = True
                return continuar
            else:
                print('Digite "s" para sim e "n" para não.')


    #Loop para lançar registros
    def lancamento(self):
        import pandas as pd
        Registro.cabecalho(self.tipo)
        desc = []
        val = []
        lancar = True
        while lancar:
            self.descricao_lanc()
            self.valor_lanc()
            desc.append(self.descricao)
            val.append(self.valor)
            print(f'A {self.tipo} chamada {self.descricao} com valor de {self.valor} foi lançada.')
            continuar = self.continuar_lancamentos()
            if continuar == 's':
                continue
            else:
                lancar = False
        tabela = dict(zip(desc, val))
        tabela = pd.DataFrame.from_dict(data=tabela, orient='index')
        tabela.columns = ['Valores']
        tabela.index.names = [self.tipo]
        tot = sum(tabela['Valores'])
        print(tabela)
        print('O total de ' + self.tipo + ' é de: R$ ' + str(tot))
        return tot




    




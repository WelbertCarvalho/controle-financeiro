#Importação dos módulos
from registro import Registro


#Para demonstrar o saldo
def saldo(receitas, despesas):
    Registro.cabecalho('saldo final')
    saldo = round(tot_receita - tot_despesa, 2)
    if saldo > 0:
        comprometido = round((tot_despesa/tot_receita) * 100, 2)
        if comprometido >= 70:
            print('Seu saldo é R$ '+ str(saldo) + ', está positivo! Porém, você está com ' + str(comprometido) + ' % da sua renda comprometida. Tente reduzir custos.')
        elif (comprometido < 70) & (comprometido >= 50):
            print('Seu saldo é R$ '+ str(saldo) + ', está positivo! Você está com ' + str(comprometido) + ' % da sua renda comprometida. Sua saúde financeira está regular.')
        elif (comprometido < 50):
            print('Seu saldo é R$ '+ str(saldo) + ', está positivo e você é um mestre das financas. Está com ' + str(comprometido) + ' % da sua renda comprometida.')
    else:
        print('Seu saldo é negativo. Você está devendo R$ ' + str(saldo*(-1)) + '. Você deve cortar custos imediatamente.')



# Execução do programa
receita = Registro('receita')
tot_receita = receita.lancamento()

despesa = Registro('despesa')
tot_despesa = despesa.lancamento()

saldo(receita, despesa)
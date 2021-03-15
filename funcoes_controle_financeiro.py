def cabecalho(tipo):
	tracej_padrao = '-' * 60
	titulo = (tracej_padrao + tipo.upper() + tracej_padrao)
	linha = '-' * len(titulo)
	print(linha)
	print(titulo)
	print(linha)

#Leitura da descrição - retorna a descrição
def desc():
	valida = False
	while not valida:
		descricao = input('Informe o nome do registro: ').strip().lower()
		if descricao == '':
			print('É necessário dar um nome ao registro!')
		else:
			valida = True
			return descricao


#Leitura do valor - retorna um dicionário
def dicio_desc_val(valores):
	descricao = desc()
	valida = False
	while not valida:
		valor = input('Informe o valor de ' + descricao.title() + ': ')
		if valor == '':
			print('É preciso informar um valor para ' + descricao.title())
		else:
			try:
				valor = float(valor)
				if valor <= 0:
					print('O valor deve ser maior que 0.')	
				else:
					valores[descricao] = valor
					valida = True
			except:
				print('Este campo só aceita valores numéricos')
	return valores


#Pergunta se deseja lançar mais registros
def continuar_lancamentos():
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
def lancamento(tipo):
	cabecalho(tipo)
	lancar = True
	valores = {}
	while lancar:
		dicio_desc_val(valores)
		continuar = continuar_lancamentos()
		if continuar == 's':
			continue
		else:
			lancar = False
	tot = sum(valores.values())
	print('O total de ' + tipo + ' é de: R$ ' + str(tot))
	return tot

#Para demonstrar o saldo
def saldo(receitas, despesas):
	cabecalho('saldo final')
	saldo = round(receitas - despesas, 2)
	if saldo > 0:
		comprometido = round((despesas/receitas) * 100, 2)
		if comprometido >= 70:
			print('Seu saldo é R$ '+ str(saldo) + ', está positivo! Porém, você está com ' + str(comprometido) + ' % da sua renda comprometida. Tente reduzir custos.')
		elif (comprometido < 70) & (comprometido >= 50):
			print('Seu saldo é R$ '+ str(saldo) + ', está positivo! Você está com ' + str(comprometido) + ' % da sua renda comprometida. Sua saúde financeira está regular.')
		elif (comprometido < 50):
			print('Seu saldo é R$ '+ str(saldo) + ', está positivo e você é um mestre das financas. Está com ' + str(comprometido) + ' % da sua renda comprometida. Nos mostre seu segredo, Mr. M.')
	else:
		print('Seu saldo é negativo. Você está devendo R$ ' + str(saldo*(-1)) + '. Você deve Você deve cortar custos imediatamente. Vou te apresentar ao Julius.')

	



	











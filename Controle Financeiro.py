import funcoes_controle_financeiro as func


receitas = func.lancamento('receitas')
despesas = func.lancamento('despesas')
func.saldo(receitas, despesas)

input('Pressione Enter para sair...')
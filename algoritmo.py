# Criação da função "calcular_media_e_aprovacao()", com as variáveis notas, nota_minima_aprovacao dentro dela.
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):

    # Criação de quatro variáveis total_notas(int); num_alunos(int); aprovados e reprovados (array)
    total_notas = 0
    num_alunos = len(notas)
    aprovados = []
    reprovados = []

# Para cada aluno adiciona a nota dele ao total de notas e verifica se está aprovado ou reprovado.
    for aluno, nota in notas.items():
        total_notas += nota
        if nota >= nota_minima_aprovacao:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)

# Calcula a media da turma com o total das notas dividido pelo numero de alunos.
    media_turma = total_notas / num_alunos

# Retorna as variáveis: media_turma, aprovados, reprovados.
    return media_turma, aprovados, reprovados

# Valor das notas e nome de cada aluno.
notas = \
 {
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
 }

# Variável que estabelece a nota mínima para ser aprovado.
nota_minima_aprovacao = 70

# Chama a função, calcula a média da turma, os aprovados e reprovados.
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)


# Escreve a média da turma, os aprovados e reprovados.
print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")

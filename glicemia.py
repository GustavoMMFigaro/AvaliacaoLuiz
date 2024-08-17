# Criação da função "diagnosticar_diabetes"
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:  # Caso a glicemia no jejum for menor ou igual à 126
        return "Diabetes"                                         # ou 200 no caso da pós prandial, retornará "Diabetes"
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:  # Caso no jejum for entr 100 e 126
        return "Pré-diabetes"                                  # ou entre 140 e 200 no pandial, retornará "Pré-diabetes"
    else:                                                      # Qualquer outro caso retornará "Normal"
        return "Normal"


# Perguta para o usuário a glicemia em jejum e pos prandial
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

# chama a função, calcula a glicemia e escreve o resultado.
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
print(f"O diagnóstico é: {resultado}")

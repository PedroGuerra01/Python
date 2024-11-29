# projeto: medidor de velocidade
# levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. crie um programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravissima. levando em consideração que se a pessoa estiver abaixo da velocidade nmaicma seu programa deve exibir "não houve multa", caso esteja ate 10km acima, deve exibit "multa leve", caso esteja entre 11 a 20km acima da velocidade maxima, "multa gravissima"

# Analise criticamente o problema e descubra:
    
# 1. quais são os dados de entrada necesarios?
# 2. O que devo fazer com estes dados ?
# 3. quais são as retrições deste problema ?
# 4. qual é o resultado esperado ?
# 5. qual é sequuencia de passos a ser feito para chegar ao resultado esperado ?

# Gerar o limite 
permitido = (80)
print(f"Velocidade permitida: {permitido} km/h")  # Para referência

# Obter a velocidade do cidadão
velocidade = int(input("Qual foi a velocidade do cidadão? "))

# Avaliar a multa
if velocidade > permitido + 20:
    print("Multa gravíssima! Excedeu mais de 20 km/h do limite permitido.")
elif permitido + 11 <= velocidade <= permitido + 20:
    print("Multa grave! Excedeu o limite permitido em até 20 km/h.")
elif permitido < velocidade <= permitido + 10:
    print("Multa leve! Excedeu o limite permitido em até 10 km/h.")
else:
    print("Dentro do limite permitido! Sem multa.")



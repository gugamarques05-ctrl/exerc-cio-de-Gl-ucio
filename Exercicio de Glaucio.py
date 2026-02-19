pessoas =[]
for i in range(15):
    print(f"Usuario {i+1}")
    
    genero = input("Informe Genero (M/F): ").upper()
    altura = float(input("Informe altura: "))
    
    pessoas.append([genero,altura])
    
menor_masculino = None
menor_feminino = None
quantidade_feminino = 0
quantidade_masculino = 0
soma_alturas = 0

for pessoa in pessoas:
    genero, altura = pessoa
    
    soma_alturas += altura
    
    if genero == "M":
        quantidade_masculino += 1
    
    if genero == "F":
        quantidade_feminino += 1
    
    elif genero == "M":
        if menor_masculino is None or altura < menor_masculino:
            menor_masculino = altura
        
    elif genero == "F":
        if menor_feminino is None or altura < menor_feminino:
            menor_feminino = altura
    
media = soma_alturas / len(pessoas)

print("\nResultados:")
print("Menor altura Masculina: ", menor_masculino)
print("Menor altura Feminina: ", menor_feminino)
print("Quantidade de Usuarios Masculinos: ", quantidade_masculino)
print("Quantidade de Usuarios Feminionos: ", quantidade_feminino)
print("Media de altura dos Usuarios: ", media)
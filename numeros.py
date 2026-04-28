# Programa: Verificar se dois números são iguais ou diferentes

# Pedir o primeiro número ao utilizador com validação
try:
    numero1 = int(input("Introduz um número: "))
    numero2 = int(input("Introduz outro número: "))
    
    # Verificar se os números são iguais ou diferentes
    if numero1 == numero2:
        print("Os números introduzidos são iguais.")
    else:
        print("Os números introduzidos são diferentes.")
        
except ValueError:
    print("Erro: Deve introduzir números inteiros válidos.")
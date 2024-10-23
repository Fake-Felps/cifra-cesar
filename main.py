import etapa1
import functions

#etapa de coleta de entradas de dados
print('Olá! Seja bem vindo ao codificador em "cifra de César"\n\n')
modo = functions.verifyModo()
mensage = functions.verifyMensage()
key = int(input("Qual chave você deseja inserir?\n"))
print(f"Chave inserida: {key}\n")

#criptografia em si
print("Frase codificada:")
mensageCripted = etapa1.cifrador(modo, mensage, key)
print(mensageCripted)


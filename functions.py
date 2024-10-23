#verifica entrada do modo de criptografia
def verifyModo():
    entrada = input("O que você deseja fazer?\n[Codificar]/[Decodificar]\n")
    
    if entrada == "codificar" or entrada == "decodificar":
        print(f"Entrada inserida: {entrada}\n")
        return entrada
    else:
        print('Entrada inválida, insira um comando válido')
        entrada = verifyModo()
        return entrada

#verifica se a mensagem é nula
def verifyMensage():
    entrada = input("Qual mensagem você deseja processar?\n")

    if entrada == "":
        print("Insira um valor válido: ", end='')
        verifyMensage()
    else:
        print(f"Mensagem inserida: {entrada}\n")
        return entrada
    


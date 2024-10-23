def cifrador(modo, mensage, key):
    index = len(mensage)
    cont = 0
    mensageCripted = ''

    if modo == "decodificar":
        key = key * (-1)

    while cont < index: 
        c = ord(mensage[cont])

        # criptografia de letras maiusculas
        if c >= 65 and c <= 90:
            c = c + key
            if c > 90:
                while c > 90:
                    c = c - 26
            elif c < 65:
                while c < 65:
                    c = c + 26
            mensageCripted = mensageCripted + chr(c)
            #print(chr(c), end='')

        #criptografia de letras minusculas
        elif  c >= 97 and c <= 122:
            c = c + key
            if c > 122:
                while c > 122:
                    c = c - 26
            elif c < 97:
                while c < 97:
                    c = c + 26
            mensageCripted = mensageCripted + chr(c)
            #print(chr(c), end='')

        #caso não seja uma letra do alfabeto
        else: 
            mensageCripted = mensageCripted + mensage[cont]
            #print(mensage[cont], end='')
        cont = cont + 1
    
    return mensageCripted


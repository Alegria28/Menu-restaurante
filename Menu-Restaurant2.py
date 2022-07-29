pedido = []
menu = {1: "Hamburguesa", 2: "Refresco", 3: "Hot Dog", 4: "Sushi", 5: "Agua"}
print("------------------------------")
print("""  Buen dia, ¿Deseas ordenar?
    Presiona 'Y' para si 
    Presiona 'N' para no """)
print("------------------------------")
primera = input("--> ")
print("------------------------------")
if primera == "Y":
    print("""Aqui esta el menu: 
    1. Hamburguesa $25
    2. Refresco $15
    3. Hot Dog $20
    4. Sushi $40
    5. Agua $10""")
    print("------------------------------")
    print("""¿Que deseas ordenar? (Usa los numeros para especificar)""")
    pedir = input("--> ")
    pedido.append(menu.get(int(pedir)))
    print("Su pedido es:", pedido)
    print("------------------------------")
    print("¿Deseas agregar algo mas?")
    print("Presiona 'Y' para si")
    print("Presiona 'N' para no")
    print("------------------------------")
    respuesta = input("--> ")
    if respuesta == "Y":
        while(True):
            print("------------------------------")
            print("Continua")
            print("Su pedido es:", pedido)
            seguir = input("--> ")
            pedido.append(menu.get(int(seguir)))  
            print("Su pedido es:", pedido)
            print("------------------------------")
            print("¿Deseas agregar algo mas?")
            print("Presiona 'Y' para si")
            print("Presiona 'N' para no")
            print("------------------------------")
            respuestal = input("--> ")
            if respuestal == "N":
                print("Su pedido es:", pedido)
                print("------------------------------")
                print("Gracias por su compra")
                break  
            elif respuesta == "Y":
                continue  
            else: 
                print("Verifica tu respuesta por favor")
                break
    elif respuesta == "N":
        print("Este es su pedido: ", pedido)
        print("Que tengas un buen dia!")
    else:
        print("Verifica tu respuesta por favor")
elif primera == "N":
    print("Que tengas un buen dia!")
else:
    print("Verifica tu respuesta por favor")


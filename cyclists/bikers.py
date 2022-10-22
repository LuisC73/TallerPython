ciclistas = []
dato = 0
while dato != 5:
    menu = "Ciclistas \n​"
    menu += "1. Agregar ciclista\n"
    menu += "2. Ver resultados\n"
    menu += "3. Salir\n"
    print(menu)
    dato = int(input("Digita la opcion: "))
    ciclista = {}
    if dato == 1:

        nombre = input("Ingrese el nombre del ciclista: ")
        edad = int(input("Ingrese la edad del ciclista: "))
        pais = input("Ingrese el pais del ciclista: ")
        equipo = input("Ingrese el equipo del ciclista: ")
        tiempo = int(input("Ingrese los minutos del ciclista: "))

        ciclista['nombre'] = nombre
        ciclista['edad'] = edad
        ciclista['pais'] = pais
        ciclista['equipo'] = equipo
        ciclista['tiempo'] = tiempo

        ciclistas.append(ciclista)

    elif dato == 2:
        ciclistaMin = ciclistas[0]
        for i in ciclistas:
            if i["tiempo"] < ciclistaMin["tiempo"]:
                ciclistaMin = i
        print(f'El ciclista que se demoro menos en llegar fue: {ciclistaMin}')        
           
    elif dato == 3:
        print("Vuelva pronto!!")
        break
    else:
        print("Numero incorrecto")
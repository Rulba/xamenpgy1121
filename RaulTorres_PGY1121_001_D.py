asistentes=[]
plati=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
gold=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
sil=[51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
ubicaciones=[]
platino=int(120000)
oro=int(80000)
plata=int(50000)
total=int(0)
for i in plati:


    from os import system
    system("cls")



    while True:
        opc=input(f"""Bienvenido a Creativos
        Concierto de Michael Jam/Entradas VIP
        Seleccione una opcion:
        1. Comprar entradas
        2. Mostrar ubicaciones disponibles
        3. Ver listado de asistentes
        4. Mostrar ganancias totales
        5. Salir

        """)
        
        if opc=="1":
            cant=int(input("Ingrese cantidad de entradas (MAX 3): "))
            for i in range(cant):
                if cant<=3:
                    print(f"""
                    |      ESCENARIO      |
                    {plati}
                    {gold} 
                    {sil}
                    """)
                    asi=int(input("Ingrese que asiento: "))
                    if asi!=ubicaciones:
                        if asi<=20:
                            print(f"""El valor de entrada es de:
                            Platino: ${platino}
                            """)
                            total= total + platino
                            for asi in plati:
                                plati.remove(asi) and plati.insert("X")
                        elif asi>20 and asi<=50:
                            print(f"""El valor de entrada es de:
                            Gold: ${oro}
                            """)
                            total= total + oro
                            for asi in gold:
                                gold.remove(asi) and gold.insert("X")
                        elif asi>50 and asi<=100:
                            print(f"""El valor de entrada es de:
                            Silver: ${plata}
                            """)
                            total= total + plata
                            for asi in sil:
                                sil.remove(asi) and sil.insert("X")
                        elif asi>100:
                            print("ingrese opcion valida")
                        run=input("Ingrese su RUN para registro: ")
                        asistentes.append(run)
                        print("Operacion realizada con exito")
                    elif asi==ubicaciones:
                        print("Asiento no disponible.....")
                    input("Presione para continuar.....")
                    
                else:
                    print("Cantidad excede limite...")
                    break
        elif opc=="2":
            ubicaciones(plati,gold,sil)
            print(ubicaciones)
        elif opc=="3":
            asistentes.sort
            print(asistentes)
        elif opc=="4":
            print(total)
        elif opc=="5":
            break
        else:
            print("ingrese una opcion valida...")
        
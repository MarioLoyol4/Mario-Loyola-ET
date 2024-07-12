import random
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = []   
sueldos_asignados = []

def generar_sueldos():
    
    for i in range(0,(len(trabajadores))):
        sueldo = random.randint(300000,2500000)
        sueldos.append(sueldo)
        sueldos_asignados.append([trabajadores[i],sueldo])
    return sueldos_asignados
   
def clasificar_sueldos(): 
   
    if not sueldos_asignados:
        print("No hay sueldos que clasificar.\n")
    else:
        menores800 = []
        entre800y2m = []
        mayores2m = []
        for i in range(len(sueldos_asignados)):
            if (sueldos_asignados[i][1]<800000):
                menores800.append(sueldos_asignados[i]) 
            elif (sueldos_asignados[i][1] >= 800000) and (sueldos_asignados[i][1] <= 2000000):
                entre800y2m.append(sueldos_asignados[i])
            elif (sueldos_asignados[i][1] > 2000000):
                mayores2m.append(sueldos_asignados[i])
        totalsueldo = sum(sueldos)        
                
        print(f"Sueldos menores a $800.000 | Total : {(len(menores800))}")  
        print(f"Nombre empleado\t|Sueldo")
        for i in range (len(menores800)):
            print(f"{menores800[i]}\n")
        print(f"Sueldos entre  $800.000 y $2.000.000 | Total : {(len(entre800y2m))}")
        print(f"Nombre empleado\t|Sueldo")
        for i in range (len(entre800y2m)):
            print(f"{entre800y2m[i]}\n")  
        print(f"Sueldos mayores a $2.000.000 | Total : {(len(mayores2m))}") 
        print(f"Nombre empleado\t|Sueldo")
        for i in range (len(mayores2m)):
            print(f"{mayores2m[i]}\n")  
        print("")  
        print(f"TOTAL SUELDOS : ${totalsueldo}")
    
       
def salir_programa():
    print("Finalizando programa...")
    print("Desarrollado por Mario Loyola.\nRUT: 20.879.968-1")
    
   
def menu(): 
    while True:
        print(f"{"*"*10}Menu{"*"*10}")
       
        opcmenu = input("[1]-Asignar sueldos\n[2]-Clasificar sueldos\n[3]-Ver estadisticas\n[4]-Reporte de sueldos\n[5]-Salir del programa\n\nSeleccione una opción\n-")

        match opcmenu:
            case "1":
                asignaSueldo= generar_sueldos()
                print(asignaSueldo)
            case "2":
                clasificar_sueldos()
            case "3":
                pass
            case "4":
                pass
            case "5":
                salir_programa()
                break
                
menu()
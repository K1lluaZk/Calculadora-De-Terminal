
while True:

 print("------------------------------------")
 print("Calculadora De Terminal Tipo Menu")
 print("------------------------------------")

 var1 = float(input("Ingresa Primer Digito:"))
 var2 = float(input("Ingresa Segundo Digito:"))

 print("1- Suma 2- Resta 3- Multiplicacion 4- Division 5- Salir")

 Op = float(input("Ingresa Un Numero:"))


 if Op == 1:
  print(var1 + var2)

 elif Op == 2:
  print(var1 - var2)

 elif Op == 3:
  print(var1 * var2)

 elif Op == 4:
  print(var1 / var2)
  
 elif Op == 5:
     print("Saliendo...")
     break
 
 else: 
    print("Ingresa un numero valido")
    



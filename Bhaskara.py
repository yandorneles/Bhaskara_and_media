import math

print("Vamos realizar a operação de bhaskara!")

b = float(input("Informe o valor de B:"))
a = float(input("Informe o valor de A:"))
c = float(input("Informe o valor de C:"))


delta = b**2 - 4*a*c

if delta > 0:
   print(f"O valor de delta é: {delta}")

   raiz_delta = math.sqrt(delta)
   x1 = (-b + raiz_delta) / (2*a)
   x2 = (-b - raiz_delta) / (2*a)
    
   print(f"As raízes são: x1 = {x1} e x2 = {x2}")

elif delta == 0:
    x = -b / (2*a)
    print(f"O valor de delta é zero, então existe apenas umas raiz: x = {x}")
 
else:
    print("Não existe solução real, pois delta é menor que zero.")
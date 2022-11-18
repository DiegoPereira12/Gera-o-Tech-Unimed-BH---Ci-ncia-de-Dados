salario = int(input())                               

if (salario <= 600):
   novo_salario = salario + (salario * (17/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 17
   print("Novo salario:", "{:.2f}".format(novo_salario))         
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

elif (salario >=600.01 and salario <=900):
   novo_salario = salario + (salario * (13/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 13
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

elif (salario >=900.01 and salario <=1500):
   novo_salario = salario + (salario * (12/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 12
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

elif (salario >=1500.01 and salario <=2000):
   novo_salario = salario + (salario * (10/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 10
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

else: 
   novo_salario = salario + (salario * (5/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 5
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")
import math
num = float(input("Digite um número real: "))
print("O valor digitado é {} e sua porção inteira é {}".format(num, int(num)))
print("O valor digitado é {} e sua porção inteira é {}".format(num, math.ceil(num)))
print("O valor digitado é {} e sua porção inteira é {}".format(num, math.trunc(num)))
print("O valor digitado é {} e sua porção inteira é {}".format(num, math.floor(num)))


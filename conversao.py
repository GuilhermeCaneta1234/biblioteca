num = int(input("Digite o numero a ser convencido \n "))
base = int(input('''escolha a base da conversao:
para binario digite 1 
para octal digite 2
para hexadecimal digite 3 
sua escolha: \n '''))
if base == 1:
    print("conversao para binario")
    print("{} convertido para binario é: {}. ".format(num, bin(num)[2:]))
elif base == 2:
    print("conversao para octal ")
    print("{} convertido para octal é: {}. " .format(num, bin(num)[2:]))
elif base == 3:
    print("conversao para hexadecimal ")
    print("{} convertido para hexadecimal é: {}. " .format(num, bin(num)[2:]))
else:
    print("escolha apenas uma das 3 opções")
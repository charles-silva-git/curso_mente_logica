pao = 3.50
leite = 4.20
cafe = 2.80
pagamento = int(input("Qual valor que foi pago? "))

troco = pagamento - (pao + leite + cafe)

print("Seu troco é: ", troco)
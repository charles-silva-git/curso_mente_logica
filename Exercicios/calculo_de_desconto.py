
quantidade_de_itens = int(input("Quantos intens vai comprar? "))
valor_total_dos_itens = float(input("Qual valor total dos itens comprados? "))

if (quantidade_de_itens > 10) or (valor_total_dos_itens > 100):{
    print("Cliente tem direito ao desconto")
}
else:{
    print("Cliente não tem direito ao desconto")
}


totalcompra = produtomaismil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    totalcompra += preço
    if preço > 1000:
        produtomaismil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(f'''O total da compra foi de R$ {totalcompra}.
O total de produtos que custam acima de R$ 1000 é de {produtomaismil}.
O produto mais barato foi {barato} que custa R$ {menor:.2f}.''')

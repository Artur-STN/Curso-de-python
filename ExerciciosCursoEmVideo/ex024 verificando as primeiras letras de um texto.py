print('Quer saber se na cidade em que você nasceu começa a palavra Santo?')
city = str(input('Em que cidade você nasceu? ')).upper().strip()
print(city[:5] == 'SANTO')

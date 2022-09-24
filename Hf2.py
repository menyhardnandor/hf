kerdes = input('Jó napja van?: ')
Nem = 'Nem'
nem = 'nem'
Igen = 'Igen'
igen = 'igen'

if kerdes == nem or kerdes == Nem:
    print('Oh sajnálom, jobbulást! :) ')
    
elif kerdes == igen or kerdes == Igen:
    print('De jó, további szép napot!' )
    
else:
    print('Sajnos nem értem a válaszodat :(')
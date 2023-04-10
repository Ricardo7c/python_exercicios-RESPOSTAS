temp = float(input('Digite a temperatura: '))


if temp >= 41:
    print('Hipertermia')
elif temp >= 39.6 and temp <= 40.9:
    print('Febre alta')
elif temp >= 37.8 and temp <= 39.5:
    print('Febre')
elif temp >= 35.1 and temp <= 37.7:
    print('Normal')
else:
    print('Hipotermia')

x = int(input('Digite um numero: '))

a , b = 1 , 1
co = 1

while co <= x - 2:
    a , b =b , a + b
    co = co + 1

print (b)

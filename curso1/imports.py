from random import randrange
import matplotlib.pyplot as plt


notas = []

for i in range(8):
    notas.append(randrange(0,11))

print(notas)

x = list(range(1, 9))
y = notas

plt.plot(x,y)
plt.title('Notas de matematica')
plt.show()

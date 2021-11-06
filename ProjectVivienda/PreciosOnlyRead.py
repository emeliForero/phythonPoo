import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

df = pd.read_csv('ProjectVivienda\data.csv')

x = df.SalePrice.value_counts()
y = df.SalePrice.value_counts().tolist()

plt.pie(x, labels = y, autopct = '%.0f%%')
plt.title('Pastel precios')

plt.show()

x = df.SalePrice.value_counts().tolist()
y = df.SalePrice.unique()

plt.bar(x, y)
plt.title('Precios mas altos y mas bajos')
ax = plt.subplot()
ax.set_xlabel('Cantidad')
ax.set_ylabel('Precio')
plt.show()

#maximo valor

print(f'El valor maximo es: {y.max()}')

print(f'El valor minimo es: {y.min()}')


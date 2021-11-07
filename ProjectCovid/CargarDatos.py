import pandas as pd
import matplotlib.pyplot as plt

class CargarDatos():

    data: str

    def cargarData(self, ruta):
        self.data = pd.read_csv(ruta)
        pass


    def primerosElementos(self, numElementos):
        y = self.data.head(numElementos)
        print(y)
        pass

    def ultimosElementos(self, numElementos):
        y = self.data.tail(numElementos)
        print(y)
        pass

    def agrupacionDatos(self, columnas, tipoFuncion):
        if(tipoFuncion == 'suma'):
            self.suma(columnas)
        if(tipoFuncion == 'promedio'):
            self.promedio(columnas)
        if(tipoFuncion == 'conteo'):
            self.conteo(columnas) 

        x = self.data.Sexo.unique()
        y = self.data.Sexo.value_counts().tolist()

        plt.bar(x, y)
        plt.title('Contagios por Genero')
        ax = plt.subplot()
        ax.set_xlabel('Generos')
        ax.set_ylabel('Numero de contagios')
        plt.show()
        pass


    def suma(self, data):
        datosColum = self.data.groupby(by=data).sum()
        print(datosColum)
        pass

    def promedio(self, data):
        datosColum = self.data.groupby(by=data).mean()
        print(datosColum)
        pass

    def conteo(self, data):
        datosColum = self.data.groupby(by=data).count()
        print(datosColum)
        pass
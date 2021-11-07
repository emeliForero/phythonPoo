from CargarDatos import CargarDatos

datos = CargarDatos()

datos.cargarData("https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD")
datos.primerosElementos(30)
datos.ultimosElementos(15)
datos.agrupacionDatos((['Sexo', 'Estado']), 'suma')
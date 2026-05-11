from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def root():
   markers=[
   {
   'lat':0,
   'lon':0,
   'popup':'This is the middle of the map.'
    }
   ]
   return render_template('index.html',markers=markers )
if __name__ == '__main__':
   app.run(host="localhost", port=8080, debug=True)


#Código Departamento,Nombre Departamento,Código Municipio,Nombre Municipio,Tipo: Municipio / Isla / Área no municipalizada,longitud,Latitud
#CRUD
class departamentos:
   def __init__(self,codigo_departamento, nombre_departamento, codigo_municipio, nombre_municipio,
                tipo, longitud, latitud ):
        self.codigo_departamento = codigo_departamento
        self.nombre_departamento = nombre_departamento
        self.codigo_municipio = codigo_municipio
        self.nombre_municipio = nombre_municipio
        self.tipo = tipo
        self.longitud = longitud
        self.latitud = latitud 
    
    def __str__(self):
        return f"""Código Departamento: {self.codigo_departamento}, Nombre Departamento: {self.nombre_departamento}, 
        Código Municipio: {self.codigo_municipio}, Tipo: {self.tipo}, Longitud: {self.longitud}, Latitud: {self.latitud}
        """
    
    

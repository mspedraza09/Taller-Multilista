
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
    
    def leerArchivo(self, lista_usuarios):
        with open("/workspaces/Taller-Multilista/file_.py", encoding="utf-8") as file:
            contenido = file.read(10)
            
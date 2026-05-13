import csv
from doublelinklist import DoubleLinkedList
from city import City, Country


class Department:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        # Si tus nodos de multilista necesitan punteros nativos, agrégalos aquí 
        # ej: self.next = None, self.sub_list = None
        
    def __str__(self):
        return f"Department Code: {self.code}, Name: {self.name}"



def load_divipola_file(file_path):
    countries = DoubleLinkedList()
    colombia = Country("CO", "Colombia")
    countries.append(colombia)
    
    departments_dict = {}
    
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Extraemos del CSV usando los nombres exactos de las columnas en español
            codigo_dep = row["Código"]
            nombre_dep = row["Nombre Departamento"]
            
            codigo_mun = row["Código Municipio"]
            nombre_mun = row["Nombre Municipio"]
            
            longitud = row["longitud"]
            latitud = row["Latitud"]
            
            if codigo_dep not in departments_dict:
                new_department = Department(codigo_dep, nombre_dep)
                departments_dict[codigo_dep] = new_department
                
                countries.add_child(colombia, new_department)
            
            city = City(codigo_mun, nombre_mun, latitud, longitud)
            
            countries.add_child(departments_dict[codigo_dep], city)
            
    return countries



def get_markers(multilist):
    markers = []
    current_country = multilist.head

    while current_country:
        if hasattr(current_country, 'sub_list') and current_country.sub_list:
            current_department = current_country.sub_list.head

            while current_department:
                if hasattr(current_department, 'sub_list') and current_department.sub_list:
                    current_city = current_department.sub_list.head

                    while current_city:
                        markers.append({
                            "lat": current_city.lat,
                            "lon": current_city.lon,
                            "popup": f"""
                            <b>{current_city.name}</b><br>
                            Departamento: {current_department.name}
                            """
                        })
                        current_city = current_city.next

                current_department = current_department.next

        current_country = current_country.next

    return markers
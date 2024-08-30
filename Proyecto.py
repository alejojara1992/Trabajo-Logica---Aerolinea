import uuid
print("Bienvenido a FBO, Vuele con nosotros hacia sus destinos soñados")
class Avion:
    def __init__(self, pasajeros, peso):
        self.pasajeros = pasajeros
        self.peso = peso
        self.vuelos = []

    async def informacionvuelo(self, destino, origen, fecha, capacidad, pasajeros):
        vuelo = {
            "Id de vuelo" : uuid.uuid4(),
            "Destino" : destino,
            "Origen" : origen,
            "Fecha" : fecha,
            "Capacidad" : capacidad,
            "Pasajeros" : pasajeros,  
        }
        self.vuelos.append(vuelo)
        print(f"El vuelo con destino a {destino} sale desde {origen} con {pasajeros} abordados")

    async def calcularpeso(self, cantidadpeso):
        self.peso = cantidadpeso
    
class Pasajero:
    def __init__(self, nombre, identificacion, nacionalidad, edad, vuelo, asiento, equipaje):
        self.nombre = nombre
        self.identificacion = identificacion
        self.nacionalidad = nacionalidad
        self.edad = edad
        self.vuelo = vuelo
        self.asiento = asiento
        self.equipaje = equipaje

    def __str__(self) -> str:
        return (f"Pasajero: {self.nombre}, Identificación: {self.identificacion}, " 
                f"Nacionalidad: {self.nacionalidad}, Edad: {self.edad}, " 
                f"Vuelo: {self.vuelo}, Asiento: {self.asiento}, "
                f"Equipaje: {self.equipaje} kg")
    
    def actualizar_equipaje(self, nuevo_peso):
        self.nuevo_peso = nuevo_peso

        if nuevo_peso >=0:
            self.equipaje = nuevo_peso
        else:
            raise ValueError("El peso del equipaje no puede ser negativo")
        
    def cambiar_asiento(self, nuevo_asiento):
        self.nuevo_asiento = nuevo_asiento

    def cambiar_vuelo(self, nuevo_vuelo):
        self.nuevo_vuelo = nuevo_vuelo

    def mostrar_equipaje(self):
        return self.equipaje

pasajero1 = Pasajero("Sebastian Calle", "123456", "Colombiano", "21", "V123", "12C", "23.8")
print(pasajero1)
pasajero1.actualizar_equipaje(22)
print(pasajero1)
peso_actual = pasajero1.mostrar_equipaje()
print(f"El peso actual del equipaje del pasajero {pasajero1.nombre} es: {peso_actual} Kg")
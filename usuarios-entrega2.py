#-- estructura simple de cliente con un metodo if de ejemplo.

class cliente():
    def __init__(self, nombre, apellido, edad, mail):
       self.nombre = nombre
       self.apellido = apellido
       self.edad = edad
       self.mail = mail

#-- metodo __str__

    def __str__(self) :
        if self.edad > 18:
            return str(self.nombre + " " + self.apellido + ", su compra fue relizada exitosamente.")

        elif self.edad < 18:
            return str(self.nombre + " " + self.apellido + ", debe ser mayor para realizar la compra")

cliente1 = cliente ('Valentin', 'Moscovich', 19, 'valenmosco@gmail.com')
cliente2 = cliente ('Valen', 'Mosco', 15, 'valenmosco@gmail.com')


print(cliente1)
print(cliente2)      



          



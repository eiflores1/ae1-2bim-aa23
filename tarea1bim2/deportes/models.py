from django.db import models

class Futbol(models.Model):
    equipo = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    seguidores = models.IntegerField()

    def __str__(self):
        return """equipo: %s - apodo: %s \n
                Seguidores: %d\n
                """ % (self.equipo,
                self.apodo,
                self.seguidores)

class Tenis(models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    seguidores = models.IntegerField()

    def __str__(self):
        return """Nombre: %s - nacionalidad: %s \n
                Seguidores: %d\n
                """ % (self.nombre,
                self.nacionalidad,
                self.seguidores)


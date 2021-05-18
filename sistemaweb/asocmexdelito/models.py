from django.db import models

# Create your models here.

class datos_participantes(models.Model):
    id_participante = models.IntegerField(default=0,primary_key=True)
    nombre = models.CharField(max_length=50)
    a_paterno = models.CharField(max_length=20)
    a_materno = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField(default=0)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    motivo = models.CharField(max_length=120)
    form_academica = models.CharField(max_length=50)
    semestre_egresado = models.CharField(max_length=8)

class institucion_procedencia(models.Model):
    nombre = models.CharField(max_length=120),
    tipo_educacion= models.CharField(max_length=8),
    direccion = models.CharField(max_length=120),
    telefono = models.CharField(max_length=50),
    pagina_web = models.CharField(max_length=80),
    tipo_carrera = models.CharField(max_length=50)

class participante_institucion(models.Model):
    id_participante = models.IntegerField(default=0),
    id_institucion = models.IntegerField(default=0),
    id_participante = models.ForeignKey(datos_participantes,on_delete=models.CASCADE),
    id_institucion = models.ForeignKey(institucion_procedencia,on_delete=models.CASCADE)

class proyectos(models.Model):
    nombre_proyecto = models.CharField(max_length=60),
    tipo_proyecto = models.CharField(max_length=30),
    nombre_asesor = models.CharField(max_length=60),
    fecha_inicio = models.DateTimeField(default=0),
    fecha_termino = models.DateTimeField(default=0),
    status = models.DateTimeField(default=0)

class status_aceptado(models.Model):
    id_participante = models.IntegerField(default=0),
    actividad = models.CharField(max_length=30),
    fecha_inicio = models.DateTimeField(default=0),
    fecha_termino = models.DateTimeField(default=0),
    duracion = models.CharField(max_length=30),
    area_asignacion = models.CharField(max_length=30),
    status = models.CharField(max_length=20),
    id_proyecto = models.IntegerField(default=1),
    id_participante = models.ForeignKey(datos_participantes, on_delete=models.CASCADE),
    id_proyecto = models.ForeignKey(proyectos,on_delete=models.CASCADE)

class avances(models.Model):
    id_proyecto = models.IntegerField(default=0),
    fecha_asignacion = models.DateTimeField(),
    fecha_entrega = models.DateTimeField(),
    fecha_limite = models.DateTimeField(),
    archivo = models.CharField(max_length=120),
    observaciones = models.CharField(max_length=120),
    id_proyecto = models.ForeignKey(proyectos,on_delete=models.CASCADE)


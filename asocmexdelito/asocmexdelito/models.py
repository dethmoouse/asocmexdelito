from django.db import models


class datos_participantes(models.Model):
    id_participante = models.IntegerField(default=0,primary_key=true)
    nombre = models.CharField(max_length=50)
    a_paterno = models.CharField(max_length=20)
    a_materno =models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    motivo = models.CharField(max_length=120)
    form_academica = models.CharField(max_length=50)
    semestre_egresado = models.CharField(max_length=8)




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
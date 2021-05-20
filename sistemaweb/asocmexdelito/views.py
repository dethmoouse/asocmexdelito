from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from .models import datos_participantes,institucion_procedencia,status_aceptado,avances,participante_institucion


# Create your views here.

def inicio(request):
    print("ayuda banda")
    doc_index=open("{% static 'html/index.html' %} ")
    plt=Template(doc_index.read())
    doc_index.close()
    contexto=Context()
    documento=plt.render(contexto)
    return HttpResponse(documento)


def registro(request):

    nombre_participante = request.GET['nombre']
    a_paterno_participante = request.GET['a_paterno']
    a_materno_participante = request.GET['a_materno']
    sexo_participante = request.GET['sexo']
    tmp_participante = request.GET['nombre']
    tmp_participante = request.GET['nombre']

    print(nombre_participante,a_paterno_participante)

    participante=datos_participantes("1","Mario","muñoz","falcon")
    doc_registro=open("{% static 'html/registro.html' %} ")
    construct_reg=Template(doc_registro.read())
    doc_registro.close()
    contexto=Context({"nombre_participante":participante.nombre,"a_paterno":participante.a_paterno,"id_participante":participante.id_participante})
    documento=construct_reg.render(contexto)
    return HttpResponse(documento)

def consulta(request):
    doc_consulta=open("C:/Asociacion Mexicana Contra Delitos Ciberneticos/asocmexdelito/asocmexdelito/templates/asocmexdelito/consulta.html")
    construct_consulta=Template(doc_consulta.read())
    doc_consulta.close()
    contexto=Context({"fecha_consulta":fecha})
    documento=construct_consulta.render(contexto)
    return HttpResponse(documento)

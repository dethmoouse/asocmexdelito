from django.http import HttpResponse
import datetime
from django.template import Template,Context

fecha=datetime.datetime.now()

class datos_participantes(object):
    def __init__(self, id_participante, nombre, a_paterno, a_materno):

        self.id_participante=id_participante
        self.nombre=nombre
        self.a_paterno=a_paterno
        self.a_materno=a_materno


def index(request):

    doc_index=open("C:/Asociacion Mexicana Contra Delitos Ciberneticos/asocmexdelito/asocmexdelito/templates/asocmexdelito/index.html")
    plt=Template(doc_index.read())
    doc_index.close()
    contexto=Context({"fecha_consulta":fecha})
    documento=plt.render(contexto)
    return HttpResponse(documento)

def calculaEdad(request,anio):
    edadActual=22
    periodo=anio-2020
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s </body></html>" %(anio,edadFutura)
    return HttpResponse(documento)

def registro(request):
    participante=datos_participantes("1","Mario","muñoz","falcon")
    doc_registro=open("C:/Asociacion Mexicana Contra Delitos Ciberneticos/asocmexdelito/asocmexdelito/templates/asocmexdelito/registro.html")
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

from django.http import HttpResponse
import datetime
from django.template import Template,Context



def index(request):
    fecha=datetime.datetime.now()
    doc_index=open("C:/Asociacion Mexicana Contra Delitos Ciberneticos/asocmexdelito/asocmexdelito/templates/asocmexdelito/index.html")
    plt=Template(doc_index.read())
    doc_index.close()
    contexto=Context({"fecha_consulta":fecha})
    documento=plt.render(contexto)
    return HttpResponse(documento)


    return HttpResponse()

def fechaactual(request):

    fecha_actual=datetime.datetime.now()
    return HttpResponse(fecha_actual)

def calculaEdad(request,anio):
    edadActual=22
    periodo=anio-2020
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s </body></html>" %(anio,edadFutura)
    return HttpResponse(documento)

def registro(request):
    doc_registro=open("C:/Asociacion Mexicana Contra Delitos Ciberneticos/asocmexdelito/asocmexdelito/templates/asocmexdelito/registro.html")
    construct_reg=Template(doc_registro.read())
    doc_registro.close()
    contexto=Context()
    documento=construct_reg.render(contexto)
    return HttpResponse(documento)

def consulta(request):
    doc_consulta=open("C:/Asociacion Mexicana Contra Delitos Ciberneticos/asocmexdelito/asocmexdelito/templates/asocmexdelito/consulta.html")
    construct_consulta=Template(doc_consulta.read())
    doc_consulta.close()
    contexto=Context()
    documento=construct_consulta.render(contexto)
    return HttpResponse(documento)
from django.http import HttpResponse
import datetime
from django.template import Template,Context


def saludo(request):
    doc_saludo=open("C:/Asociacion Mexicana Contra Delitos Ciberneticos/asocmexdelito/asocmexdelito/templates/asocmexdelito/index.html")
    plt=Template(doc_saludo.read())
    doc_saludo.close()
    contexto=Context()

    documento=plt.render(contexto)
    return HttpResponse(documento)


    return HttpResponse()

def despedida(request):
    return HttpResponse("Que te vaya bien amigo")

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

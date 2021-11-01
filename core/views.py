from django import template
from django import http
from django.shortcuts import render
from core.models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

def index(request):

    produtos = Produto.objects.all()
    batata = 'batata'

    context={
        'curso' :  'Programação Web com Django Framework',
        'outro' :  'Django é massa',
        'produtos' : produtos,
        'batata' : batata,
             }
    
    return render(request, 'index.htm',context)

def contato(request):
    return render(request,'contato.htm')


def produto(request, id):
    # print(f'id: {id}')
    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto' : prod
    }
    return(render(request, 'produto.htm', context))

def error404(request, ex):
    template = loader.get_template('404.htm')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.htm')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)



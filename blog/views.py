from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


def starting_page(request):
    return HttpResponse("pagina principal")

def posts(request):
    return HttpResponse("Es la pagina de los posts")

def detailed_post(request):
    return HttpResponse("una sola publicacion aparte")
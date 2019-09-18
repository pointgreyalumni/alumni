from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


def index(request):
    template = get_template('index/index.html')
    context = {
    }

    return HttpResponse(template.render(context, request))


def profiles(request):
    template = get_template('index/profiles.html')
    context = {
    }

    return HttpResponse(template.render(context, request))
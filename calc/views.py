
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

import main
from django import db


def homecalc(request):
    #db.reset_queries()
    #project = Project.objects.all()

    return render(request, 'calc/homecalc.html')#, {'project': project})
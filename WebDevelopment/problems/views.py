from django.shortcuts import render
from django.http import HttpResponse

import datetime # TODO DELETE THIS
# Create your views here.

def index(request):
    now=datetime.datetime.now()
    return HttpResponse("{}".format(now))

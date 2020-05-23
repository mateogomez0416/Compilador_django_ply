from django.http import HttpResponse
from django.shortcuts import render

from django.template import Template, RequestContext
from django.template.loader import get_template

from compiler.cp._parser import *

import sys
import os

def index(request):

    return render(request,'index.html')

def resultado(request): 

    algo= request.GET["pas"]
    VERBOSE = 1
    
    parser.parse(algo, tracking=True)
    
    return render(request,'data.html',{"esto":algo,"aca":valbool()}) 
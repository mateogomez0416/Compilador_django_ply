from django.http import HttpResponse
from django.shortcuts import render

from django.template import Template, RequestContext
from django.template.loader import get_template

from compiler.cp._parser import parser
from compiler.cp._lexer import tokens,lexer

from django.utils.safestring import mark_safe
from django.template import Library

import json

import sys
import os
from os import remove

register = Library()

def index(request):

    return render(request,'index.html')

def documentación(request):
    
    return render(request,'documentación.html')


def resultado(request): 

    textAreaindex= request.GET["pas"]
    tokenResult=[]
    
   
    lexer.input(textAreaindex)
    while True:
        tok=lexer.token()
        if not tok:
            break
        tokenResult.append(tok.type)
        tokenResult.append(tok.value)
        
    
    parser.parse(textAreaindex, tracking=True)

    
    mydic = json.dumps(tokenResult)

    Mensaje__ = open("parseMs.outt","r")
    abrir = Mensaje__.read()
     
    if abrir is'':
        abrir= " Sintaxis aceptada"
    else:
        abrir =  "("+abrir+")" +" Error de sintaxis  "
    
    Mensaje__.close()
    remove("parseMs.outt")      
    open("parseMs.outt","w")    
    
    pasosparser = open("parsePasos.outt","r")
    leer=  pasosparser.read()
    pasosparser.close()
    remove("parsePasos.outt")      
    open("parsePasos.outt","w")    


    return render(request,'data.html',context={"tokere":mydic,"textAreaindex":textAreaindex,"Error":abrir,"resulparser":leer}) 
import json
import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.contrib.auth import authenticate, login

def post_list(request,token):
    #if request.user.is_authenticated:
        return HttpResponseRedirect('https://miniapp-ifnmg.herokuapp.com/usuario/' + token)
    #else:
    #    return HttpResponseRedirect('../login/')

def autentica_token(request, token):
    response = requests.get('https://miniapp-ifnmg.herokuapp.com/usuario/' + token)
    data = response.json()
    if str(data['login']) == 'True':
        user = authenticate(request, username = 'admin', password = 'admin')
        login(request,user)
        return HttpResponseRedirect('../produto/listaWeb/')
    #received_json_data = json.loads(request.POST.get['https://miniapp-ifnmg.herokuapp.com/usuario/' + token])
    return StreamingHttpResponse('it was post request: ' + str(data))

# Create your views here.

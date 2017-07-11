# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
import requests

# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField(label='UserName',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            drone_login = requests.get("http://192.168.1.132:8080/v1/login/",
                                       params={'username': username, 'password': password}).text;
            if drone_login:
                info = 'ok！'
            else:
                info = 'no！'
            return HttpResponse(info)
    else:
        uf = UserForm()
    context = {'uf':uf}
    return render(req, 'login.html', context)


def logout(req):
    response = HttpResponse('logout !!')
    response.delete_cookie('username')
    return response
# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")


def home(request):
    context = {}
    context['index'] = 'Welcome Djiango!'
    return render(request, 'index.html', context)

def submit(request):
    request.encoding = 'utf-8'
    if request.GET:
        print("=====")
        if 'submit' in request.GET:
            message = '你点击了GET请求，内容: ' + request.GET['submit']
        else:
            message = '你点击了GET请求，无内容'
    elif request.POST:
        if 'submit' in request.POST:
            message = '你点击了POST请求，内容: ' + request.POST['submit']
        else:
            message = '你点击了POST请求，无内容'

    return HttpResponse(message)


def login(request):
    num = 'admin'
    pwd = '123456'
    ctx ={}
    if request.POST['num']==num and request.POST['pwd']==pwd:
        ctx['mess'] = '登录成功'
    else:
        ctx['mess'] = '账号或密码不正确'
    return render(request, "index.html", ctx)

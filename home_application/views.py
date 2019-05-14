# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')

def helloworld(request):
    if request.method == 'GET':
        return render(request, 'home_application/helloworld.html')
    elif request.method == 'POST':
        text_content = request.POST['text_input']
        if text_content == "Hello Blueking":
            return render(request, 'home_application/helloworld.html', locals())
        else:
            return render(request, 'home_application/helloworld.html')




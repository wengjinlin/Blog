from django.shortcuts import render


def register(request):
    # 注册
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        pass
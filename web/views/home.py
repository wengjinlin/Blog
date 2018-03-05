from django.shortcuts import render


def index(request):
    """
    博客首页，展示全部博文
    """
    return render(request, 'index.html')

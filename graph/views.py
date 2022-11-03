from django.shortcuts import render


def index(request):
    context = {'text': 'Hello World'}
    return render(request, 'base.html', context)
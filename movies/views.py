from django.shortcuts import render, HttpResponse

# Create your views here.


# def index(request):
#     context = {
#         'movies':['gladiator','anything','test']
#     }
#     return render(request, 'movies/index.html', context)

# app/templates/app/index.html


# def about(request):
#     return render(request, 'movies/about.html')


def index(request):
    return HttpResponse('<h1>hello</hello>')

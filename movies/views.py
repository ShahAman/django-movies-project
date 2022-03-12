from django.http import HttpResponse
from django.shortcuts import render

from .models import Movie

def movies(request):
    # data = {
    #     'movies' : [
    #         {
    #             'id' : 1,
    #             'title' : 'The Batman',
    #             'year' : 2022
    #         },
    #         {
    #             'id' : 2,
    #             'title' : 'Spider-Man: No Way Home',
    #             'year' : 2021
    #         },
    #         {
    #             'id' : 3,
    #             'title' : 'Extraction',
    #             'year' : 2020
    #         }
    #     ]
    # }
    # return HttpResponse("Hello there.")
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {"movies" : data} )

def home(request):
    return HttpResponse("Home page.")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/details.html', {'movie': data})
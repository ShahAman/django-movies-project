from django.http import HttpResponse
from django.shortcuts import render

def movies(request):
    data = {
        'movies' : [
            {
                'id' : 1,
                'title' : 'The Batman',
                'year' : 2022
            },
            {
                'id' : 2,
                'title' : 'Spider-Man: No Way Home',
                'year' : 2021
            },
            {
                'id' : 3,
                'title' : 'Extraction',
                'year' : 2020
            }
        ]
    }
    # return HttpResponse("Hello there.")
    return render(request, 'movies/movies.html', data )

def home(request):
    return HttpResponse("Home page.")

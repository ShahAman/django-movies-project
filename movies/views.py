from shutil import move
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse

from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def delete(request, id):
    try:
       movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exists')
    movie.delete()
    return HttpResponseRedirect('/movies')

@api_view(['GET', 'POST'])
def movie_list(request, format=None):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        # return JsonResponse({"movies" : serializer.data}, safe=False)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id, format=None):

    try:
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
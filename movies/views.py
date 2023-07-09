from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Ajooba',
            'year': '1969'
        },
        {
            'id': 6,
            'title': 'DDLJ',
            'year': '1991'
        },
        {
            'id': 7,
            'title': 'ZMND',
            'year': '2013'
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("this is Home Page")
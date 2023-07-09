from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from movies.forms import UploadForm
from .models import Movie

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("this is Home Page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'detail': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    
    return render(request, 'movies/add.html')

def movieDelete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        return Http404("Movie Does not found")
    movie.delete()
    return HttpResponseRedirect('/movies')

def movieUpload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'movies/upload.html', {'form': UploadForm})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm

# Create your views here.
def demo(request):
    movie= Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,"index.html",context)

def details(request,m_id):
    movie=Movie.objects.get(id=m_id)

    return render(request,"des.html",{'x':movie})

def add_movie(request) :
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie( name= name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,"add.html")

def update(request,id):
    m=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None , request.FILES,instance=m)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':m})

def delete(request,id):

    if request.method=="POST":
        m=Movie.objects.get(id=id)
        m.delete()
        return redirect('/')
    return render(request,'delete.html')

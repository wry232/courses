from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index (request):
    context = {
    'courses': Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)
def add (request):
    name = request.POST['course_name']
    description = request.POST['course_description']
    Course.objects.create(name = name, description  = description)
    return redirect('/')
def destroy  (request, id):
    obj= Course.objects.get(id=id)
    # name =
    fname = obj.name
    fdescription = obj.description
    context = {
    'name': fname,
    'description':fdescription,
    'id':id
    }
    return render(request, 'course_app/choice.html', context)
    # name = Course.objects.filter(id = id)['name']
    # description = Course.objects.filter(id = id)['description']
    # if len(name)>1:
    #     return render(request, 'course_app/choice.html', name = name, description = description)
    # else:
    #     return redirect('/')
# def destroy (request, id):
    # Course.objects.filter(id = id).delete()
    # return redirect('/')
def yes  (request,id):
    # id = request.POST[id]
    Course.objects.filter(id = id).delete()
    return redirect('/')
def no  (request,id):
    # id = request.POST[id]
    # Course.objects.filter(id = id).delete()
    return redirect('/')

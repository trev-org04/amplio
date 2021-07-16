from django.shortcuts import render
from . import models
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')

def forms(request):
    return render(request, 'forms/mainform.html')

def webinar(request):
    if request.method == 'POST':
        name = request.POST['name']
        grade = request.POST['grade']
        email = request.POST['email']
        date = request.POST['date']
        extraInfo = request.POST['extraInfo']
        models.registration.objects.create(
            name=name, grade=grade, email=email, date=date, extraInfo=extraInfo)
        messages.success(
            request, 'Your details have been saved. We\'ll see you soon!')
        return render(request, 'forms/webinar.html')
    else:
        return render(request, 'forms/webinar.html')

def waitlist(request):
    return render(request, 'forms/waitlist.html')

def handler404(request, exception):
    data = {}
    return render(request, 'errors/404.html', data, status=404)

def handler500(request):
    data = {}
    return render(request, 'errors/500.html', data, status=500)
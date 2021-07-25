from django.shortcuts import render
from . import models
from .forms import WebinarForm
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')

def forms(request):
    return render(request, 'forms/mainform.html')

def webinar(request):
    if request.method == 'POST':
        # name = request.POST['name']
        # grade = request.POST['grade']
        # email = request.POST['email']
        # date = request.POST['date']
        # extraInfo = request.POST['extraInfo']
        form = WebinarForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            grade = form.cleaned_data['grade']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            extraInfo = form.cleaned_data['extraInfo']
            models.registration.objects.create(name=name, grade=grade, email=email, date=date, extraInfo=extraInfo)
            messages.success(request, 'Your details have been saved. We\'ll see you soon!')
            webinarForm = WebinarForm()
            return render(request, 'forms/webinar.html', {'webinarForm': webinarForm})
        else: 
            messages.success(request, 'Invalid form data. Please fill out each field properly.')
            webinarForm = WebinarForm()
            return render(request, 'forms/webinar.html', {'webinarForm': webinarForm})
        # models.registration.objects.create(
        #     name=name, grade=grade, email=email, date=date, extraInfo=extraInfo)
        # messages.success(
        #     request, 'Your details have been saved. We\'ll see you soon!')
        # return render(request, 'forms/webinar.html')
    else:
        webinarForm = WebinarForm()
        return render(request, 'forms/webinar.html', {'webinarForm': webinarForm})

def waitlist(request):
    return render(request, 'forms/waitlist.html')

def handler404(request, exception):
    data = {}
    return render(request, 'errors/404.html', data, status=404)

def handler500(request):
    data = {}
    return render(request, 'errors/500.html', data, status=500)
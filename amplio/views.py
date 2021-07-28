import os
import urllib
import json
from django.shortcuts import render
from . import models
from .forms import WebinarForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.templatetags.static import static
from email.mime.image import MIMEImage

def home(request):
    return render(request, 'home/home.html')

def forms(request):
    return render(request, 'forms/mainform.html')

def webinar(request):
    if request.method == 'POST':
        form = WebinarForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                name = form.cleaned_data['name']
                grade = form.cleaned_data['grade']
                email = form.cleaned_data['email']
                date = form.cleaned_data['date']
                extraInfo = form.cleaned_data['extraInfo']
                models.registration.objects.create(name=name, grade=grade, email=email, date=date, extraInfo=extraInfo)
                messages.success(request, 'Your details have been saved. We\'ll see you soon!')
                htmlContent = render_to_string('forms/emailtemplate.html', {'content': 'Thank you, {}! You\'ve been registered for our webinar on {}. See you soon!'.format(name, date)})
                textContent = strip_tags(htmlContent)
                email = EmailMultiAlternatives('Thank you for registering!', textContent, settings.EMAIL_HOST_USER, [email])
                email.mixed_subtype = 'related'
                email.attach_alternative(htmlContent, 'text/html')
                staticPath = 'static'
                amplioPath = 'amplio'
                homePath = 'home'
                imagesPath = 'images'
                instaPath = 'instagram.png'
                file_path = os.path.join(settings.BASE_DIR, amplioPath, staticPath, homePath, imagesPath, instaPath)
                with open(file_path, 'rb') as f:
                    instaData = f.read()
                img = MIMEImage(instaData)
                img.add_header('Content-ID', '<{name}>'.format(name=instaPath))
                email.attach(img)
                twitterPath = 'twitter.png'
                file_path2 = os.path.join(settings.BASE_DIR, amplioPath, staticPath, homePath, imagesPath, twitterPath)
                with open(file_path2, 'rb') as f:
                    twitterData = f.read()
                img2 = MIMEImage(twitterData)
                img2.add_header('Content-ID', '<{name}>'.format(name=twitterPath))
                email.attach(img2)
                webPath = 'web.png'
                file_path3 = os.path.join(settings.BASE_DIR, amplioPath, staticPath, homePath, imagesPath, webPath)
                with open(file_path3, 'rb') as f:
                    webData = f.read()
                img3 = MIMEImage(webData)
                img3.add_header('Content-ID', '<{name}>'.format(name=webPath))
                email.attach(img3)
                email.send()
                webinarForm = WebinarForm()
                return render(request, 'forms/webinar.html', {'webinarForm': webinarForm})
            else:
                messages.success(request, 'Invalid reCAPTCHA. Please try again.')
                webinarForm = WebinarForm()
                return render(request, 'forms/webinar.html', {'webinarForm': webinarForm})
        else: 
            messages.success(request, 'Invalid form data. Please fill out each field properly.')
            webinarForm = WebinarForm()
            return render(request, 'forms/webinar.html', {'webinarForm': webinarForm})
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
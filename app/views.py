from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
from app.forms import *

def registeration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            nsuo=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            nsuo.set_password(password)
            nsuo.save()

            nspo=pfd.save(commit=False)
            nspo.user_name=nsuo
            nspo.save()
            send_mail('Registeration',
                        "Registration is done",
                        'boyamahesh8039@gmail.com',
                        [nsuo.email],
                        fail_silently=False)
            


            return HttpResponse('Data is inserted sucessfully')
        else:
            return HttpResponse('Data is NotValid')


    return render(request,'registeration.html',d)
    

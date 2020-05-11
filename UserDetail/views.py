from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm


#add
def Register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        user=request.POST.get('username')
        phone=request.POST.get('phonenumber')
        qs=User.objects.filter(username=user)
        qs1=User.objects.filter(phonenumber=phone)
        if qs.exists() or qs1.exists():
            #return HttpResponse("User or Phonenumber is registered")
            return render(request,'register.html',{'msg':"user or phonenumber is already registered"})

        else:
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/login/')
                except:
                    return HttpResponse("Something is wrong")

    else:
        form = UserForm()
    return render(request,'register.html',{'form':form})

def Login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username=request.POST['x']
        password=request.POST['y']

        for i in User.objects.all():
            if (i.username==username and i.password==password) or (i.phonenumber==username and i.password==password):
                return HttpResponse(f"Welcome {i.username}")
        else:
            return render(request,'login.html',{'form':"Wrong credentials"})
    return render(request,'login.html',{'form':None})

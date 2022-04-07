from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .forms import Signupform,loginform,Postform
from.models import Book,Contact
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q
# Create your views here.
def home(request):

    return render(request,'myapp/home.html',)

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    if request.method=="POST":
        n=request.POST['name']
        e = request.POST['email']
        f = request.POST['feedback']
        c= Contact(name=n,email=e,feedback=f)
        c.save()
        messages.success(request,'Your details are successfully submitted')

    return render(request,'myapp/contact.html')



def dashboard(request):
    ap=Book.objects.all()
    return render(request,'myapp/dashboard.html',{'ap':ap})


def viewbook(request):
    ap=Book.objects.all()
    return render(request,'myapp/viewbook.html',{'ap':ap})

def usersignup(request):
    if request.method == 'POST':
        f = Signupform(request.POST)
        if f.is_valid():
            f.save()

            return HttpResponseRedirect('/login/')
    else:

        f = Signupform()
    return render(request, 'myapp/signup.html', {'f': f})


def userlogin(request):
    if request.method == 'POST':
        lf = loginform(request=request, data=request.POST)
        if lf.is_valid():
            q = lf.cleaned_data['username']
            r = lf.cleaned_data['password']
            m = authenticate(username=q, password=r)
            if m is not None:
                login(request, m)

                return HttpResponseRedirect('/dashboard/')

    else:

        lf = loginform()
    return render(request, 'myapp/login.html', {'lf': lf})


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def addbook(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            i = form.cleaned_data['isbn']
            a = form.cleaned_data['author']
            c = form.cleaned_data['category']

            b = Book(name=n, isbn=i, author=a, category=c)
            b.save()
            form = Postform()
    else:
        form = Postform()
    return render(request, 'myapp/addbook.html', {'form': form})



def deletebook(request,id):
    if request.method=='POST':
        de=Book.objects.get(pk=id)
        de.delete()

    return HttpResponseRedirect('/dashboard/')


def updatebook(request,id):
    if request.method == 'POST':
        d = Book.objects.get(pk=id)
        f = Postform(request.POST, instance=d)
        if f.is_valid():
            messages.success(request, 'Data is updated successfully')
            f.save()
    else:
        d = Book.objects.get(pk=id)
        f = Postform(instance=d)
    return render(request, 'myapp/updatebook.html', {'f': f})





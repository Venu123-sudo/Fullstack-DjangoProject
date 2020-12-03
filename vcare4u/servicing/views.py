from django.shortcuts import render

# Create your views here.
def home(request):
        return render(request, 'index.html')

def about(request):
        return render(request, 'about.html')

def services(request):
        return render(request, 'services.html')

def blog(request):
        return render(request, 'blog.html')

def contact(request):
        return render(request, 'contact.html')

def cart(request):
        return render(request, 'cart.html')

def washing(request):
        return render(request, 'washing.html')

def washing1(request):
        return render(request, 'washing1.html')

def washing2(request):
        return render(request, 'washing2.html')

def washing3(request):
        return render(request, 'washing3.html')

def fridge(request):
        return render(request,'fridge.html')

def fridge1(request):
        return render(request,'fridge1.html')

def fridge2(request):
        return render(request,'fridge2.html')

def fridge3(request):
        return render(request,'fridge3.html')

def micro(request):
        return render(request,'micro.html')

def micro1(request):
        return render(request,'micro1.html')

def micro2(request):
        return render(request,'micro2.html')

def micro3(request):
        return render(request,'micro3.html')

def air(request):
        return render(request, 'air.html')

def air1(request):
        return render(request, 'air1.html')

def air2(request):
        return render(request, 'air2.html')

def air3(request):
        return render(request, 'air3.html')

def tv(request):
        return render(request, 'tv.html')

def tv1(request):
        return render(request, 'tv1.html')

def tv2(request):
        return render(request, 'tv2.html')

def tv3(request):
        return render(request, 'tv3.html')

def geyser(request):
        return render(request, 'geyser.html')

def geyser1(request):
        return render(request, 'geyser1.html')

def geyser2(request):
        return render(request, 'geyser2.html')

def geyser3(request):
        return render(request, 'geyser3.html')

def plumbing(request):
        return render(request, 'plumbing.html')

def plumbing1(request):
        return render(request, 'plumbing1.html')

def plumbing2(request):
        return render(request, 'plumbing2.html')

def plumbing3(request):
        return render(request, 'plumbing3.html')

def login(request):
        return render(request, 'login.html')

def register(request):
        return render(request, 'register.html')

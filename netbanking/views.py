from django.shortcuts import render

# Create your views here.
# Home view - renders the home page
def login(request):
    return render(request, 'netbanking/login.html')

def online(request):
    return render(request, 'netbanking/online.html')

def otp_page(request):
    return render(request, 'netbanking/otp_page.html')

def landing(request):
    return render(request, 'netbanking/landing.html')

def estatement_page(request):
    return render(request, 'netbanking/estatement_page.html')

def view_estatement_page(request):
    return render(request, 'netbanking/view_estatement_page.html')
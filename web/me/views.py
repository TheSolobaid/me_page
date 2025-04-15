from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'me/index.html')

def about(request):
    return render(request, 'me/about.html')

def contact(request):
    return render(request, 'me/contact.html')

def portfolio(request):
    return render(request, 'me/portfolio.html')


def interest(request):
    return render(request, 'me/interest.html')

def annee(request, annee):
    return render(request, f"me/portfolio/annee_{annee}.html")

def sae(request, annee, sae):
    return render(request, f"me/portfolio/annee_{annee}/{sae}.html")

from django.shortcuts import render

# Create your views here.

def CMR_home(request):
    return render(request,"CMR_Home.html")

def CMR_dashboard(request):
    return render(request,"CMR_dashboard.html")

def CMR_archive(request):
    return render(request,"archive.html")


from django.shortcuts import render

# Create your views here.


def get_dashboard(request):
    return render(request, 'dashboard/main.html')
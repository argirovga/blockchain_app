from django.shortcuts import render

# Create your views here.


def view_available_requests(request):

    return render(request, 'main.html')

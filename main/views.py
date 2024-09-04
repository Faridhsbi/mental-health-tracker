from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152512',
        'name': 'Muhammad Farid Hasabi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
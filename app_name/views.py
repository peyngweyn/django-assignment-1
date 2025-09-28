from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    context = {
        "name": "Nowil Adrian Moscare",
        "student_id": "2024-05839"
    }
    return render(request, "about.html", context)

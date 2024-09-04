from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245466',
        'name': 'Fakhriyah Ghania Putri',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
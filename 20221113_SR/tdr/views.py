from django.shortcuts import render

# Create your views here.
def rec(request):
    context = {
        
    }
    return render(request, 'rec.html', context)
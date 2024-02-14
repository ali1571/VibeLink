from django.shortcuts import render

# Create your views here.
def InterestSearch_view(request):
    return render(request, "startInterests.html", {})


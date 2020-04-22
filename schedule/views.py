from django.shortcuts import render

# Create your views here.
def schedule_view(request):
    return render(request, 'schedule.html')

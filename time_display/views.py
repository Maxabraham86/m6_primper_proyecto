from django.shortcuts import render

# Create your views here.

from time import localtime, strftime
    
def index(request):
    context = {
        "time": strftime("%H:%M %p", localtime()),
        "date" : strftime("%Y-%m-%d", localtime())
    }
    return render(request,'index.html', context)

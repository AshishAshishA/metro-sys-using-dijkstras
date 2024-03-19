from django.shortcuts import render
from .forms import stationForm
from .logic import Metro

# Create your views here.

def select_station(request):
    context={
        "form":stationForm,
    }
    return render(request,"metro/form_page.html",context)


def shortest_path(request):
    if request.method=="POST":
        src=request.POST.get('src')
        dest=request.POST.get('dest')

        metro=Metro()
        shortest_dist,station_list=metro.get_shortest_Dist(src,dest)

        context={
            'src':src,
            'dest':dest,
            'shortest_dist':shortest_dist,
            'station_list':station_list,
        }

        return render(request,'metro/result_page.html',context)
    else:
        return render(request,"metro/form_page.html",{"form":stationForm})

from django.shortcuts import render
from .utils import EditEvent
from .config.params import params

def index(request):
    params["isfree"] = True
    if request.method == "POST":
        if "apply" in request.POST:
            event = EditEvent()
            year = int(request.POST['year'])
            month = int(request.POST['month'])
            day = int(request.POST['day'])
            period = int(request.POST['period'])
            print('before create_event')
            event.create_event(year, month, day, period)
            print('after create_event')
            params["isfree"] = False
        elif "delete" in request.POST:
            event = EditEvent()
            event.delete_all_event()
            params["isfree"] = True
        elif "reset" in request.POST:
            params["isfree"] = True
    return render(request, 'index.html', params)
            
    # event.delete_all_event()  
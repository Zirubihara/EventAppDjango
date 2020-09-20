from django.http import JsonResponse
from django.shortcuts import render

from .models import Event


# Create your views here.
def home_viec(request, *args, **kwargs):
    return render(request, "home.html")


def events_list_view(request, *args, **kwargs):
    querySet = Event.objects.all()
    events_list = [{"id": x.id, "name": x.name, "description": x.description, "text": x.text} for x in querySet]
    data = {
        "response": events_list
    }
    return JsonResponse(data)


def event_detail_view(request, event_id, *args, **kwargs):
    data = {
        "id": event_id,
    }
    status = 200
    try:
        obj = Event.objects.get(id=event_id)
        data['name'] = obj.name
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)

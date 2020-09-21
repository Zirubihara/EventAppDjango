from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import EventForm
from .models import Event

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_viec(request, *args, **kwargs):
    return render(request, "home.html")


def event_create_view(request, *args, **kwargs):
    form = EventForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = EventForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form})


def events_list_view(request, *args, **kwargs):
    querySet = Event.objects.all()
    events_list = [x.serialize() for x in
                   querySet]
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

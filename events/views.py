from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import EventForm
from .models import Event


# Create your views here.
def home_viec(request, *args, **kwargs):
    return render(request, "home.html")


def event_create_view(request, *args, **kwargs):
    form = EventForm(request.POST or None)
    next_url = request.POST.get("next") or None
    print("next url", next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = EventForm()
    return render(request, 'components/form.html', context={"form": form})


def events_list_view(request, *args, **kwargs):
    querySet = Event.objects.all()
    events_list = [{"id": x.id, "name": x.name, "description": x.description, "text": x.text, "likes": 12} for x in
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

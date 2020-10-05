from django.contrib.auth.mixins import LoginRequiredMixin
from .serializer import EventSerializer
from .models import Event
#from .permissions import IsHighPermission
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class EventList(LoginRequiredMixin, generics.ListAPIView):
    raise_exception = True
    permission_classes = []
    queryset = Event.objects.all()
    serializer_class = EventSerializer



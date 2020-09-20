from django.test import TestCase
from events.models import Event
# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name="EventName", description="EventDesc", text="EventText")

    def test_event(self):
        eventSample = Event.objects.get(name="EventName")
        self.assertEqual(eventSample.name, "EventName")
        self.assertEqual(eventSample.description, "EventDesc")
        self.assertEqual(eventSample.text, "EventText")

    def should_find_something(self):
        response = self.client.get("/create-events")
        print(response)
        self.assertContains(response, 'Naeeme', status_code=200)
        #self.assertTemplateUsed(response, 'appropriate_page.html')

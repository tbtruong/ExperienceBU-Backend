from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # fields = (("eventID", "eventName", "content", "eventAffiliation", "eventType", "eventTags", "contact_info",
        #          "already_happened", "banner"))
        fields = (
            "id", "name", "affiliation", "picture", "description", "date", "time", "location", "type", "tags",
            "contact",
            "connection")

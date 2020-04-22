from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("eventID", "eventName", "content", "eventAffiliation", "eventType", "eventTags", "contact_info",
                  "already_happened", "banner")

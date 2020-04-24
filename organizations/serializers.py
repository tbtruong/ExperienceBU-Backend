from rest_framework import serializers
from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        # fields = (("eventID", "eventName", "content", "eventAffiliation", "eventType", "eventTags", "contact_info",
        #          "already_happened", "banner"))
        fields = (
            "id", "name", "picture", "description", "requirements", "eboard", "time", "location", "contact", "tags")

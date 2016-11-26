from rest_framework import serializers
from trackEvent.models import UserModel, EventModel
import md5

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ( 'user_fname', 'user_lname', 'user_email', 'user_passwd' )

    def create( self, validated_data ):
        user = super(UserSerializer, self).create( validated_data )
        user.save()
        return user

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventModel
        fields = ( 'event_title', 'event_desc', 'event_venue' )

    def create( self, validated_data ):
        event = super(EventSerializer, self).create( validated_data )
        event.save()
        return event

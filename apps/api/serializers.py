from rest_framework import serializers
from apps.services.models import ServicePage,ServiceType,ServiceLocation
from django.utils.html import strip_tags

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        depth = 1
        fields = ['id','name']

class ServiceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceLocation
        depth = 1
        fields = ['id','name']

class ServicePageSerializer(serializers.ModelSerializer):
    service_type = ServiceTypeSerializer(many=True)
    location = ServiceLocationSerializer(read_only=True)
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        if obj.text:
            text = strip_tags(obj.text)
        else:
            text = ''
        return text
    class Meta:
        model = ServicePage
        depth = 1
        fields = ['id','preview_text','text','price','phone','address','messenger_link','website','service_type','location']
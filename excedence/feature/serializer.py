from rest_framework.serializers import (

    ModelSerializer,
    SerializerMethodField,ValidationError,
    )
from rest_framework.validators import UniqueValidator
import datetime
if __package__ != None:
    from serializer import *
    from models import *
else:
    from .models import *
    from .serializer import *


from rest_framework import serializers





class FeatureCreateSerializer(ModelSerializer):
    name = serializers.CharField(max_length=200,required=False)
    priority=serializers.IntegerField(required=False)
    class Meta:
        model=FeatureRequest
        fields=['title','description','Date','Product_Area','name','priority']


    def create(self,validated_data):
        try:
            title=validated_data.get("title")
            description=validated_data.get("description")
            Date=validated_data.get("Date")
            Product_Area=int(validated_data.get('Product_Area'))
            name=validated_data.get('name')
            priority=validated_data.get('priority')
            if Client.objects.filter(Name=name):
                client=Client.objects.filter(Name=name)[0]
                client.priority=priority
                client.save()
            else:
                Client.objects.create(Name=name,priority=priority)
            client=Client.objects.filter(Name=name)[0]
            x=FeatureRequest.objects.create(title=title,description=description,Associated_client=client,Date=Date,Product_Area=Product_Area)
            return x

        except Exception as e:
            print e
            raise ValidationError(e)





class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model=Client
        fields=['Name','priority']



class FeatureListSerializer(ModelSerializer):
    Associated_client=ClientDetailSerializer(read_only=False)
    Product=SerializerMethodField()
    class Meta:
        model=FeatureRequest
        fields=["title",'description','Associated_client','Date','Product']

    def get_Product(self,obj):
        return obj.get_Product_Area_display()


from django.shortcuts import render
if __package__ != None:
    from serializer import *
    from models import *
else:
    from .models import *
    from .serializer import *


from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveAPIView,
    CreateAPIView, )

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django.db.models import Q


class CreateFeatureCreateAPIview(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = FeatureCreateSerializer


class ListFeatureAPIview(ListAPIView):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureListSerializer

    def get_queryset(self):
        fr=FeatureRequest.objects.all()
        query = self.request.GET.get("q")
        if query:
            fr=fr.filter(Q(Associated_client__Name__icontains=query)|Q(title=query))
        return fr








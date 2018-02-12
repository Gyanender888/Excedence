from django.conf.urls import patterns, include, url
if __package__ != None:
    from views import *
else:
    from .views import *


urlpatterns = [url(r'^create_feature/$', CreateFeatureCreateAPIview.as_view(), name='createClient'),
               url(r'^get/$', ListFeatureAPIview.as_view(), name='ListFeatureAPIview')
               ]
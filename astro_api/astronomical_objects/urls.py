from django.urls import path
from django.urls import include

from astronomical_objects.views import AstroObjectListView

urlpatterns = [
    path('astro_list/', AstroObjectListView.as_view())
]

from . import views
from django.urls import path,include,re_path
from .views import event_info
urlpatterns = [
    re_path(r'^api/events/$', views.show_events),

]
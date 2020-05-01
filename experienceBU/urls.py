"""experienceBU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from userAccount import views as user_views
from django.conf import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from events import views as event_views
from organizations import views as club_views
from userAccount import views as user_views
from django.conf import settings

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('profile', user_views.UserProfileViewSet)
# from django.contrib.auth.views import logout


urlpatterns = [
    # path('register/', user_views.register, name='register'),
    # path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='userAccount/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userAccount/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('googlelogin/', TemplateView.as_view(template_name='userAccount/googlelogin.html')),
    # path('google/', user_views.GoogleView.as_view(), name='google'),
    path('tokenretrieval/', user_views.tokenretrieval, name='tokenretrieval'),
    # path('exchange1/', user_views.exchange_token, name='tokenexchange'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    # url(r'^gmailAuthenticate', user_views.gmail_authenticate, name='gmail_authenticate'),
    # url(r'^$', user_views.home, name='home'),
    re_path(r'^auth/', include('rest_framework_social_oauth2.urls')),
    re_path(r'^api/events/$', event_views.show_events),
    re_path(r'^api/events/(?P<pk>[0-9]+)/$', event_views.event_info),
    re_path(r'^api/events/(?P<pk>[0-9]+)/$', event_views.events_detail),
    re_path(r'^api/events/by/(?P<connection>\w+)/$', event_views.ClubEvents.as_view()),
    re_path(r'^api/organizations/$', club_views.show_clubs),
    re_path(r'^api/organizations/(?P<pk>[0-9]+)/$', club_views.club_info),
    re_path(r'^api/organizations/(?P<pk>[0-9]+)/$', club_views.clubs_detail),
    re_path(r'^api/profile/$', user_views.show_profiles),
    re_path(r'^api/profile/update$', user_views.update_profile_view, name='update profile'),
    # url(r'auth-social/', include('social_django.urls', namespace='social'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

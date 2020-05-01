from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.conf import settings
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp, SocialAccount
from allauth.socialaccount.providers.google.views import oauth2_login
from allauth.socialaccount.helpers import complete_social_login
from . import models
from events.models import Event
from organizations.models import Club
from django.contrib.auth import logout as auth_logout
from . import serializers as p_serializer
import requests, json
import allauth.account
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from social_django.utils import psa
from django.http import HttpResponse, HttpResponseRedirect


@api_view(['PUT', ])
def update_profile_view(request, slug):
    try:
        page = models.Profile.objects.get(slug=slug)
    except models.Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = p_serializer.ProfileSerializer(page, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# @api_view(http_method_names=['POST'])
# @permission_classes([AllowAny])
# @psa()
# def exchange_token(request, backend):
#     """
#     Exchange an OAuth2 access token for one for this site.
#     This simply defers the entire OAuth2 process to the front end.
#     The front end becomes responsible for handling the entirety of the
#     OAuth2 process; we just step in at the end and use the access token
#     to populate some user identity.
#     The URL at which this view lives must include a backend field, like:
#         url(API_ROOT + r'social/(?P<backend>[^/]+)/$', exchange_token),
#     Using that example, you could call this endpoint using i.e.
#         POST API_ROOT + 'social/facebook/'
#         POST API_ROOT + 'social/google-oauth2/'
#     Note that those endpoint examples are verbatim according to the
#     PSA backends which we configured in settings.py. If you wish to enable
#     other social authentication backends, they'll get their own endpoints
#     automatically according to PSA.
#     ## Request format
#     Requests must include the following field
#     - `access_token`: The OAuth2 access token provided by the provider
#     """
#     print("Test Exchange!")
#
#     serializer = SocialSerializer(data=request.data)
#     print(request.data)
#     if serializer.is_valid(raise_exception=True):
#         # set up non-field errors key
#         # http://www.django-rest-framework.org/api-guide/exceptions/#exception-handling-in-rest-framework-views
#         try:
#             nfe = settings.NON_FIELD_ERRORS_KEY
#         except AttributeError:
#             nfe = 'non_field_errors'
#
#         try:
#             # this line, plus the psa decorator above, are all that's necessary to
#             # get and populate a user object for any properly enabled/configured backend
#             # which python-social-auth can handle.
#             user = request.backend.do_auth(serializer.validated_data['access_token'])
#         except HTTPError as e:
#             # An HTTPError bubbled up from the request to the social auth provider.
#             # This happens, at least in Google's case, every time you send a malformed
#             # or incorrect access key.
#             return Response(
#                 {'errors': {
#                     'token': 'Invalid token',
#                     'detail': str(e),
#                 }},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#
#         if user:
#             if user.is_active:
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key})
#             else:
#                 # user is not active; at some point they deleted their account,
#                 # or were banned by a superuser. They can't just log in with their
#                 # normal credentials anymore, so they can't log in with social
#                 # credentials either.
#                 return Response(
#                     {'errors': {nfe: 'This user account is inactive'}},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#         else:
#             # Unfortunately, PSA swallows any information the backend provider
#             # generated as to why specifically the authentication failed;
#             # this makes it tough to debug except by examining the server logs.
#             return Response(
#                 {'errors': {nfe: "Authentication Failed"}},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


# test = Profile.objects.values('user')[1]['user']
# profile = models.Profile.objects.get(user=request.user)
@api_view(['GET', 'POST'])
def tokenretrieval(request):
    current_user = request.user
    # print(current_user.username)

    # profile = models.Profile.objects.get(user=)
    throwaway = SocialAccount.objects.get(user=2)
    tokenA = SocialToken.objects.get(account=1)
    # print(profile.first_name)
    # print(throwaway.uid)
    # print(tokenA.token)
    return Response({"token": tokenA.token})


@api_view(['GET', 'POST'])
def rsvp_Events(request, id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=id)
        if event.followers.filter(id=request.user.id).exists():
            event.followers.remove(request.user)
        else:
            event.followers.add(request.user)
        return HttpResponseRedirect("http://localhost:3000/")


@api_view(['GET', 'POST'])
def subscribe(request, id):
    if request.method == 'POST':
        club = get_object_or_404(Club, id=id)
        if club.subscribers.filter(id=request.user.id).exists():
            club.subscribers.remove(request.user)
        else:
            club.subscribers.add(request.user)
        return HttpResponseRedirect("http://localhost:3000/")


# @login_required
@api_view(['GET', 'POST'])
def show_profiles(request):
    # request_instance = Event.objects.create()

    if request.method == 'GET':
        data = models.Profile.objects.all()

        serializer = p_serializer.ProfileSerializer(data, context={'request': request}, many=True)
        print("request received! request received!")
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = p_serializer.ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'userAccount/register.html', {'form': form})

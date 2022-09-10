"""EventsApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from allauth.account.views import confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('events.urls')),
    path('api/v1/accounts/',include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  
   
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
    # re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]

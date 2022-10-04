
from django.contrib import admin
from django.urls import path,include,re_path
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from allauth.account.views import confirm_email
from django.conf.urls.static import static
from django.conf import settings

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
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

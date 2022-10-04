from django.urls import path ,re_path
from rest_framework.routers import DefaultRouter
from .views import UserViewset,ProfileViewset,UserProfileViewset
# ,MyEvents,UserEvents
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView
from allauth.account.views import confirm_email as allauthemailconfirmation

router=DefaultRouter()
router.register(r'users',UserViewset)
router.register(r'profiles',ProfileViewset)
router.register('kkkkk/(?P<user_id>\d+)/profiles/',UserProfileViewset,basename='user_profile_api')

urlpatterns = [
# auth urls
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),    
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('verify-email/',VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r"^account-confirm-email/(?P<key>[-:\w]+)/$", allauthemailconfirmation, name='account_confirm_email'),

#     user events url/s
#    path('user-events/<int:user_id>/',UserEvents.as_view()),
#    path('my-events/<int:user_id>/',MyEvents.as_view())
]
urlpatterns += router.urls

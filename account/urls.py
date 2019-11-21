from django.conf.urls import include, url
from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from django.conf import settings

from .views import profile, newapikey, deleteapikey, RatticSessionDeleteView
from .views import RatticTFADisableView, RatticTFABackupTokensView
from .views import RatticTFASetupView, RatticTFALoginView
from .views import RatticTFAGenerateApiKey

from two_factor.views import QRGeneratorView

import django
import account


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', profile, name='profile'),
    path('newapikey/', newapikey, name='newapikey'),
    path('deleteapikey/<int:key_id>/', deleteapikey, name='deleteapikey'),

    path('logout/', auth_views.LogoutView.get_next_page,name='logout'),

    # View to kill other sessions with
    path('killsession/<str:pk>/', RatticSessionDeleteView.as_view(), name='kill_session'),

    # Two Factor Views
    path('login/', RatticTFALoginView.as_view(), name='login'),
    path('generate_api_key', RatticTFAGenerateApiKey.as_view(), name="generate_api_key"),

    path('two_factor/disable/', RatticTFADisableView.as_view(), name='tfa_disable'),
    path('two_factor/backup/', RatticTFABackupTokensView.as_view(), name='tfa_backup'),
    path('two_factor/setup/', RatticTFASetupView.as_view(), name='tfa_setup'),
    path('two_factor/qr/', QRGeneratorView.as_view(), name='tfa_qr'),
]

if settings.GOAUTH2_ENABLED:
    urlpatterns += [
        path('', include('social_auth.urls')),
    ]

# URLs we don't want enabled with LDAP
if not settings.LDAP_ENABLED:
    urlpatterns += [
        path('reset/',
            auth_views.PasswordResetView.as_view(template_name='password_reset.html', success_url='/account/reset/done/'),
            name="password_reset"
            ),

        path('reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
            name="password_reset_done"
            ),

        path('reset/<str:uidb64>-<str:token>)/',
            auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url='/'),
            name="password_reset_confirm"
            ),

        path('changepass/', auth_views.PasswordChangeView.as_view(template_name='account_changepass.html', success_url=reverse_lazy('profile') ), name='password_change')
    ]

# URLs we do want enabled with LDAP
if settings.LDAP_ENABLED and settings.AUTH_LDAP_ALLOW_PASSWORD_CHANGE:
    urlpatterns += [
        path('changepass/', account.views.ldap_password_change, {}, name='password_change')
    ]

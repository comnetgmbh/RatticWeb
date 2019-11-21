from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import LogoutView
from tastypie.api import Api
from cred.api import CredResource, TagResource
from staff.api import GroupResource
from django.conf import settings
from .views import home
from django.urls import include, path, re_path
from . import views


# Configure the error handlers
handler500 = 'ratticweb.views.handle500'
handler404 = 'ratticweb.views.handle404'

# Setup the API
v1_api = Api(api_name='v1')
v1_api.register(CredResource())
v1_api.register(TagResource())
v1_api.register(GroupResource())

# Setup the base paths for applications, and the API
urlpatterns = [
    # Apps:
    path('', home, name='home'),
    #path('/', include('django.contrib.auth.urls')),
    url(r'^account/', include('account.urls')),
    path('cred/', include('cred.urls'),),
    path('staff/', include('staff.urls')),
    url(r'^help/', include('help.urls')),

    #PasswordResetView

    url('password_reset/', PasswordResetView.as_view(), name='password_reset'),

    path('logout/', views.home_logout, name='logout'),

    # API
    url(r'^api/', include(v1_api.urls)),

    # Language
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # two Factor
    # url(r'^', include('two_factor.urls', namespace='two_factor')),
]

# If in debug mode enable the Django admin interface
if settings.DEBUG:
    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += [
        # Uncomment the admin/doc line below to enable admin documentation:
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', admin.site.urls),
    ]

# Strip any leading slash from the RATTIC_ROOT_URL
if settings.RATTIC_ROOT_URL[0] == '/':
    root = settings.RATTIC_ROOT_URL[1:]
else:
    root = settings.RATTIC_ROOT_URL

# Serve RatticDB from an alternate root if requested
# urlpatterns += [
#     url(r'^' + root, include(urlpatterns)),
# ]

# Serve the static files from the right location in dev mode
urlpatterns += staticfiles_urlpatterns()

print('ratticweb:' + str(urlpatterns[0]))




from django.conf.urls import url
from django.urls import path, re_path
from django.conf import settings
from .views import NewUser, UpdateUser
from . import views

urlpatterns = [
    # Views in views.py
    path('', views.home, name='staff'),

    # User/Group Management
    path('userdetail/<int:uid>/',views.userdetail,name='userdetail'),
    path('removetoken/<int:uid>/',views.removetoken,name= 'removetoken'),
    path('groupdetail/<int:gid>/',views.groupdetail, name= 'groupdetail'),

    # Auditing
    path('audit-by-<str:by>/<int:byarg>/',views.audit, name= 'audit'),

    # Importing
    path('import/keepass/',views.upload_keepass,name= 'upload_keepass'),
    path('import/process/',views.import_overview, name= 'import_overview'),
    path('import/process/<int:import_id>/',views.import_process,name= 'import_process'),
    path('import/process/<int:import_id>/ignore/',views.import_ignore,name= 'import_ignore'),

    # Undeletion
    path('credundelete/<int:cred_id>/',views.credundelete,name= 'credundelete'),
]

# URLs we remove if using LDAP groups
if not settings.USE_LDAP_GROUPS:
    urlpatterns += [
        # Group Management
        path('groupadd/', views.groupadd,name='groupadd'),
        path('groupedit/<int:gid>/',views.groupedit,name= 'groupedit'),
        path('groupdelete/<int:gid>/',views.groupdelete,name= 'groupdelete'),
        path('useredit/<int:pk>/', UpdateUser.as_view(), name="user_edit"),
        path('userdelete/<int:uid>/',views.userdelete,name= 'userdelete'),
    ]

# User add is disabled only when LDAP config exists
if not settings.LDAP_ENABLED:
    urlpatterns += [
        # User Management
        path('useradd/', NewUser.as_view(), name="user_add"),

    ]

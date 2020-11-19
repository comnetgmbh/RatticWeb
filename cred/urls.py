from django.conf.urls import url
from django.urls import path, re_path
from django.conf import settings
from cred import views
from cred.views import list
from django.http import request

app_name = 'cred'

urlpatterns = [
    # New list views
    path('list/', list , name="cred_list"),
    path('list-by-<str:cfilter>/<str:value>/',views.list,name='list2'),
    path('list-by-<str:cfilter>/<str:value>/sort-<str:sortdir>-by-<str:sort>/',views.list,name='list3'),
    path('list-by-<str:cfilter>/<str:value>/sort-<str:sortdir>-by-<str:sort>/page-<int:page>/',views.list,name='list4'),

    # Search dialog for mobile
    path('search/',views.search,name='search'),

    # Single cred views
    path('detail/<int:cred_id>/', views.detail, name= 'detail'),
    path('detail/<int:cred_id>/fingerprint/',views.ssh_key_fingerprint,name= 'ssh_key_fingerprint'),
    path('detail/<int:cred_id>/download/',views.downloadattachment,name= 'downloadattachment'),
    path('detail/<int:cred_id>/ssh_key/',views.downloadsshkey,name= 'downloadsshkey'),
    path('edit/<int:cred_id>/',views.edit,name= 'edit'),
    path('delete/<int:cred_id>/',views.delete,name= 'delete'),
    path('add/',views.add,name= 'add'),

    # Adding to the change queue
    path('addtoqueue/<int:cred_id>/',views.addtoqueue,name= 'addtoqueue'),

    # Bulk views (for buttons on list page)
    path('addtoqueue/bulk/',views.bulkaddtoqueue,name= 'bulkaddtoqueue'),
    path('delete/bulk/',views.bulkdelete,name= 'bulkdelete'),
    path('undelete/bulk/',views.bulkundelete,name= 'bulkundelete'),
    path('addtag/bulk/',views.bulktagcred,name= 'bulktagcred'),

    # Tags
    path('tag/',views.tags, name= 'tags'),
    path('tag/add/',views.tagadd, name= 'tagadd'),
    path('tag/edit/<int:tag_id>',views.tagedit, name= 'tagedit'),
    path('tag/delete/<int:tag_id>',views.tagdelete,name= 'tagdelete'),
]

if not settings.RATTIC_DISABLE_EXPORT:
    urlpatterns += [
        # Export views
        path('export.kdb',views.download, name= 'download'),
        path('export-by-<str:cfilter>/<str:value>.kdb',views.download,name= 'download_filter'),
    ]
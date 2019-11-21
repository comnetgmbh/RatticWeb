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
    path('list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/',views.list,name='list2'),
    path('list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/',views.list,name='list3'),
    path('list-by-<str:cfilter>/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/page-(?P<page>\d+)/',views.list,name='list4'),

    # Search dialog for mobile
    url(r'^search/$',views.search,name='search'),

    # Single cred views
    path('detail/<int:cred_id>/', views.detail, name= 'detail'),
    path('^detail/(?P<cred_id>\d+)/fingerprint/$',views.ssh_key_fingerprint,name= 'ssh_key_fingerprint'),
    path('^detail/(?P<cred_id>\d+)/download/$',views.downloadattachment,name= 'downloadattachment'),
    path('^detail/(?P<cred_id>\d+)/ssh_key/$',views.downloadsshkey,name= 'downloadsshkey'),
    path('^edit/(?P<cred_id>\d+)/$',views.edit,name= 'edit'),
    path('^delete/(?P<cred_id>\d+)/$',views.delete,name= 'delete'),
    path('^add/$',views.add,name= 'add'),

    # Adding to the change queue
    path('^addtoqueue/(?P<cred_id>\d+)/$',views.addtoqueue,name= 'addtoqueue'),

    # Bulk views (for buttons on list page)
    path('^addtoqueue/bulk/$',views.bulkaddtoqueue,name= 'bulkaddtoqueue'),
    path('^delete/bulk/$',views.bulkdelete,name= 'bulkdelete'),
    path('^undelete/bulk/$',views.bulkundelete,name= 'bulkundelete'),
    path('^addtag/bulk/$',views.bulktagcred,name= 'bulktagcred'),

    # Tags
    path('tag/',views.tags, name= 'tags'),
    path('^tag/add/$',views.tagadd, name= 'tagadd'),
    path('^tag/edit/(?P<tag_id>\d+)/$',views.tagedit, name= 'tagedit'),
    path('^tag/delete/(?P<tag_id>\d+)/$',views.tagdelete,name= 'tagdelete'),
]

if not settings.RATTIC_DISABLE_EXPORT:
    urlpatterns += [
        # Export views
        url(r'^export.kdb$',views.download, name= 'download'),
        url(r'^export-by-(?P<cfilter>\w+)/(?P<value>[^/]*).kdb$',views.download,name= 'download_filter'),
    ]
print('cred:' + str(urlpatterns))
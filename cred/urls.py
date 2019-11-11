from django.conf.urls import url
from django.conf import settings
import views

urlpatterns = [
    # New list views
    url('list/',views.list,name= 'list'),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/$',views.list,name='list'),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/$',views.list,name='list'),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/page-(?P<page>\d+)/$',views.list,name='list'),

    # Search dialog for mobile
    url(r'^search/$',views.search,name='search'),

    # Single cred views
    url(r'^detail/(?P<cred_id>\d+)/$',views.detail,name= 'detail'),
    url(r'^detail/(?P<cred_id>\d+)/fingerprint/$',views.ssh_key_fingerprint,name= 'ssh_key_fingerprint'),
    url(r'^detail/(?P<cred_id>\d+)/download/$',views.downloadattachment,name= 'downloadattachment'),
    url(r'^detail/(?P<cred_id>\d+)/ssh_key/$',views.downloadsshkey,name= 'downloadsshkey'),
    url(r'^edit/(?P<cred_id>\d+)/$',views.edit,name= 'edit'),
    url(r'^delete/(?P<cred_id>\d+)/$',views.delete,name= 'delete'),
    url(r'^add/$',views.add,name= 'add'),

    # Adding to the change queue
    url(r'^addtoqueue/(?P<cred_id>\d+)/$',views.addtoqueue,name= 'addtoqueue'),

    # Bulk views (for buttons on list page)
    url(r'^addtoqueue/bulk/$',views.bulkaddtoqueue,name= 'bulkaddtoqueue'),
    url(r'^delete/bulk/$',views.bulkdelete,name= 'bulkdelete'),
    url(r'^undelete/bulk/$',views.bulkundelete,name= 'bulkundelete'),
    url(r'^addtag/bulk/$',views.bulktagcred,name= 'bulktagcred'),

    # Tags
    url(r'^tag/$',views.tags, name= 'tags'),
    url(r'^tag/add/$',views.tagadd, name= 'tagadd'),
    url(r'^tag/edit/(?P<tag_id>\d+)/$',views.tagedit, name= 'tagedit'),
    url(r'^tag/delete/(?P<tag_id>\d+)/$',views.tagdelete,name= 'tagdelete'),
]

if not settings.RATTIC_DISABLE_EXPORT:
    urlpatterns += [
        # Export views
        url(r'^export.kdb$',views.download, name= 'download'),
        url(r'^export-by-(?P<cfilter>\w+)/(?P<value>[^/]*).kdb$',views.download,name= 'download'),
    ]

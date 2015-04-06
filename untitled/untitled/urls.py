from django.conf.urls import patterns, include, url
# from django.contrib import admin
from Myblog import views
import Myblog.urls
import xadmin
xadmin.autodiscover()
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^xadmin/', include(xadmin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    (r'^login/$', views.Login ),
    (r'^index',views.index ),
    (r'^acc_login/$', views.acc_login),
    (r'^logout/$', views.logout_view),
    (r'^bbs_pub/$', views.bbs_pub),
    (r'^bbs_pub/$', views.bbs_pub),
    (r'^bbs_bianji/$', views.bbs_bianji),
    (r'^deletepin/$', views.deletepin),

    url(r'', include(Myblog.urls)),


)

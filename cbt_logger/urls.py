from django.conf.urls import url
from cbt_logger import views

urlpatterns = [
    url(r'^cbt_logs/$', views.cbt_log_list),
    url(r'^cbt_logs/(?P<pk>[0-9]+)/$', views.cbt_log_detail),
]

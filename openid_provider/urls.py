# vim: set ts=4 sw=4 : */

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.openid_server, name='openid-provider-root'),
    path('decide/', views.openid_decide, name='openid-provider-decide'),
    path('xrds/', views.openid_xrds, name='openid-provider-xrds'),
    re_path(r'^(?P<id>.*)/$', views.openid_xrds, {'identity': True}, name='openid-provider-identity'),
]

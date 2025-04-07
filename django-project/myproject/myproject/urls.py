from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^save/$', 'home.views.save_image'),
    url(r'^admin/', include(admin.site.urls)),
)

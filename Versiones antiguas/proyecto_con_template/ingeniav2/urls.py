from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ingeniav2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ingenia/', include('pedidos.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

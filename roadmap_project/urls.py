from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from roadmap.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('goal/', include('roadmap.urls')),
    path('', index, name='index')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

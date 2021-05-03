from django.contrib import admin
from django.urls import path, include

from roadmap.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goal/', include('roadmap.urls')),
    path('', index, name='index')
]

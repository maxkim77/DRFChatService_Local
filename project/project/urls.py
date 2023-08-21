from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("accounts.urls")),
    path('api/', include('chat.urls')),  
    re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
]

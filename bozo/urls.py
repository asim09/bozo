
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('price/', include('prices.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

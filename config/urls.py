from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from apps.gohanbot.views import top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name='top'),
    path('', include('apps.gohanbot.urls')),
    path('accounts/', include('apps.accounts.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

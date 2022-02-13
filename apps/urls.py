
from django.contrib import admin
from django.urls import path, include
from snippets.views import top
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),
    path('gohanbot/', include('gohanbot.urls'))
]

if settings.DEBUG:
     import debug_toolbar
     urlpatterns = [
         path('__debug__/', include(debug_toolbar.urls)),
     ] + urlpatterns
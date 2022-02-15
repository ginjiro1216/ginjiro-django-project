
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from gohanbot.views import top
# from snippets.views import top as s_top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name='top'),
    # path('s/', s_top, name='s_top'),
    # path('s/snippets/', include('snippets.urls')),
    path('gohanbot/', include('gohanbot.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
     import debug_toolbar
     urlpatterns = [
         path('__debug__/', include(debug_toolbar.urls)),
     ] + urlpatterns
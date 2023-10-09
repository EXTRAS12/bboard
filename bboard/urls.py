from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache


handler404 = 'bboard.views.handler404'
handler500 = 'bboard.views.handler500'

urlpatterns = [
    path("avitoadmin/", admin.site.urls),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path("captcha", include('captcha.urls')),
    path("api/", include('api.urls')),
    path('', include('main.urls')),
    ]


if settings.DEBUG:
    # import debug_toolbar

    # urlpatterns = [
    #         path('__debug__/', include(debug_toolbar.urls)),
    # ]+urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
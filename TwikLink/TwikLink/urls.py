from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



urlpatterns = [
    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('mahdiesscv69/admin/', admin.site.urls),
    path('', include("Profile.urls")),
    path('accounts/', include('allauth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'Profile.views.error_404_view'
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
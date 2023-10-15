from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



urlpatterns = [
    path('mahdi-admin/', admin.site.urls),
    path('', include("Profile.urls")),
    path('defender-admin/defender/', include("defender.urls")),
    path('accounts/', include('allauth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]

handler404 = 'Profile.views.error_404_view'


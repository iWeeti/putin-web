from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('putin.urls')),
    re_path(r'^discord/', include('discord_bind.urls'), name='discord'),
    path('register/', user_views.register, name='register'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	path('api/', api.urls, name='api-index')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

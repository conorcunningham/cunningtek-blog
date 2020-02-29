from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from blog.views import google
from blog.models import Post

post_dict = {
    'queryset': Post.objects.all(),
}

urlpatterns = [
    path('googled7c5cb564f623934.html', google, name='google'),
    path('superspacepenguins/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('users.urls')),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(post_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

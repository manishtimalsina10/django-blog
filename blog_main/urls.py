

from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import SettingsReference, settings
from blogs import views as BlogsView




urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('<slug:slug>/', BlogsView.blogs, name = 'blogs' ),
    
    #Search Endpoint
    path('blog/search/', BlogsView.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





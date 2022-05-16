from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import MainView, PostJsonListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main-view'),
    path('posts-json/<int:num_posts>/', PostJsonListView.as_view(), name='posts-json-view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
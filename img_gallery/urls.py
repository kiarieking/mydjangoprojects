from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.display_image, name='display_images'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('<int:id>/delete_image/', views.delete_image, name='delete_image'),
    path('<int:id>/', views.image_detail, name='image_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include
from uploadfile_demo import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'uploadfile_demo'

urlpatterns = [
    path('', views.IndexView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
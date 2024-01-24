from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ #главные урлы с корневой с настройками
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')), #ссылается на созданные урлы в нашем приложении
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
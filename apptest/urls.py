# Incluir la aplicación al proyecto
from django.conf.urls import url,include
# Convocar a las urls de las settings
from django.conf import settings
from django.conf.urls.static import static


# nombramos las urls de la aplicación
urlpatterns = [
 path('admin/', admin.site.urls),
 url(r"^", include("myApp.urls")),
]+static(settings.STATIC_URL,
document_root=settings.STATICFILES_DIRS)+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)

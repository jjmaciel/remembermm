from django.urls import path, include

"""mmtesteb URL Configuration
estas duas linhas static e settings são necessárias para poder abrir os arquivos de media
é usado somente para o desenvolvimento. Também é necessário concatenar no final da urlpattens
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
o django não serve para arquivos estáticos, arquivos estáticos devem ser colocados em outro servidor
o django só trabalha com arquivos python.
"""

from django.conf.urls.static import static
from django.conf import settings

# import APPs
from remembermm import urls

urlpatterns = [
    path('', include(urls)),
    
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

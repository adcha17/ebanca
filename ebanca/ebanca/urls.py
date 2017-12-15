from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from core.views import ClientListView, SignUpView, SignInView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ClientListView.as_view(), name='client_list'),
    url(r'^signup/', SignUpView.as_view(), name='signup'),
    url(r'^signin/', SignInView.as_view(), name='signin'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

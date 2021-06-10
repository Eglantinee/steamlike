from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from books import views as book_view
from accounts import views as account_view
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'books', book_view.BookViewSet, basename='books')
router.register(r'genres', book_view.GenresViewSet, basename='genres')
router.register(r'search_book', book_view.BookSearchViewSet, basename='search')
# router.register(r'admin', admin.AdminSite, basename='admin')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_framework.urls')),
    path('accounts/create/', account_view.CreateUser.as_view()),
    path('book/genres/', book_view.GenresViewSet.as_view({'get': 'list'})),
    path('book/?search', book_view.BookSearchViewSet.as_view({'get': 'list'})),
    path('accounts/auth-login/', obtain_auth_token),
    # curl -X POST http://localhost:8000/accounts/auth-login/ -d "username=user1" -d "password=111111"
    path('accounts/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
    # can be used either but it is not displayed at web
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

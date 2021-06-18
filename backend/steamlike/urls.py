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
# router.register(r'genres', book_view.GenresViewSet, basename='genres')
# router.register(r'search_book', book_view.BookSearchViewSet, basename='search')
# router.register(r'admin', admin.AdminSite, basename='admin')


from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Past API')

urlpatterns = [
    # url(r'^fake-doc/', schema_view),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('accounts/', include('rest_framework.urls')),
    path('accounts/create/', account_view.CreateUserView.as_view()),
    path('book/genres/', book_view.GenresListView.as_view()),
    # path('book/?search', book_view.BookSearchViewSet.as_view()),
    path('accounts/login/', obtain_auth_token),
    path('accounts/logout/', account_view.UserLogoutView.as_view()),
    path('accounts/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('accounts/balance/', account_view.UserBalanceView.as_view()),
    path('accounts/user_info/', account_view.GetUserInfoView.as_view()),
    path('accounts/user_info/update/', account_view.UpdateUserInfo.as_view()),
    path('accounts/buy_book/', account_view.StoreUserBook.as_view()),
    path('book/comment/', account_view.UserCommentView.as_view()),
    path('accounts/library/', account_view.UserLibraryView.as_view()),
    path('author/list/', book_view.AuthorsListView.as_view()),
    path('author/<int:pk>/', book_view.AuthorInfoView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

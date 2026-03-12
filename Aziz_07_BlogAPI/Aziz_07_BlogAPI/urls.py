
from django.contrib import admin
from django.urls import path
from blog_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('AuthorApiAdd/',AuthorApiAdd),
    path('AuthorApiView/<int:id>/',AuthorApiView),
    path('CategoryApiAdd/',CategoryApiAdd),
    path('CategoryApiView/<int:id>/',CategoryApiView),
    path('PostApiAdd/',PostApiAdd),
    path('PostApiView/<int:id>/',PostApiView),
    path('CommentApiAdd/',CommentApiAdd),
    path('CommentApiView/<int:id>/',CommentApiView),
]

from django.contrib import admin
from blog_app.models import *

admin.site.register([AuthorModel,CategoryModel,PostModel,CommentModel])

from django.db import models

class AuthorModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=254,null=True)

class CategoryModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)

class PostModel(models.Model):
    title=models.CharField(max_length=100,null=True)
    content=models.TextField(null=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name='category_name',null=True)
    published_date=models.DateTimeField(auto_now_add=True,null=True)
    author=models.ForeignKey(AuthorModel,on_delete=models.CASCADE,related_name='author_name',null=True)
    
class CommentModel(models.Model):
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name='post_name',null=True)
    author_name=models.CharField(max_length=100,null=True)
    content=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

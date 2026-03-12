from rest_framework import serializers
from blog_app.models import *

class AuthorApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuthorModel
        fields='__all__'
        
class CategoryApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryModel
        fields='__all__'
        
class PostApiSerializer(serializers.ModelSerializer):
    Categorydata=CategoryApiSerializer(source='category',read_only=True)
    authordata=AuthorApiSerializer(source='author',read_only=True)
    class Meta:
        model=PostModel
        fields=['title','content','category','published_date','author','Categorydata','authordata']
        
class CommentApiSerializer(serializers.ModelSerializer):
    postdata=PostApiSerializer(source='post',read_only=True)
    class Meta:
        model=CommentModel
        fields=['post','postdata','author_name','content','created_at']
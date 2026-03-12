from blog_app.models import *
from blog_app.serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def AuthorApiAdd(request):
    if request.method=='GET':
        data=AuthorModel.objects.all()
        serializer=AuthorApiSerializer(data, many=True)
        return Response({
            "success":True,
            "message":"Data got successfully",
            "data":serializer.data,
        })
    
    if request.method=='POST':
        serializer=AuthorApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Added successfully",
            "data":serializer.data,
        })
        
@api_view(['GET','PUT','DELETE'])
def AuthorApiView(request,id):
    viewdata=AuthorModel.objects.get(id=id)
    
    if request.method=='GET':
        serializer=AuthorApiSerializer(viewdata)
        return Response({
            "success":True,
            "message":"Data Got successfully",
            "data":serializer.data,
        })

    if request.method=='PUT':
        serializer=AuthorApiSerializer(data=request.data,instance=viewdata)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Updated successfully",
            "data":serializer.data,
        })
        
    if request.method=='DELETE':
        viewdata.delete()
        return Response({
            "success":True,
            "message":"Data Deleted successfully",
        })
        
@api_view(['GET','POST'])
def CategoryApiAdd(request):
    if request.method=='GET':
        data=CategoryModel.objects.all()
        serializer=CategoryApiSerializer(data, many=True)
        return Response({
            "success":True,
            "message":"Data got successfully",
            "data":serializer.data,
        })
    
    if request.method=='POST':
        serializer=CategoryApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Added successfully",
            "data":serializer.data,
        })
        
@api_view(['GET','PUT','DELETE'])
def CategoryApiView(request,id):
    viewdata=CategoryModel.objects.get(id=id)
    
    if request.method=='GET':
        serializer=CategoryApiSerializer(viewdata)
        return Response({
            "success":True,
            "message":"Data Got successfully",
            "data":serializer.data,
        })

    if request.method=='PUT':
        serializer=CategoryApiSerializer(data=request.data,instance=viewdata)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Updated successfully",
            "data":serializer.data,
        })
        
    if request.method=='DELETE':
        viewdata.delete()
        return Response({
            "success":True,
            "message":"Data Deleted successfully",
        })


@api_view(['GET','POST'])
def PostApiAdd(request):
    if request.method=='GET':
        data=PostModel.objects.all()
        serializer=PostApiSerializer(data, many=True)
        return Response({
            "success":True,
            "message":"Data got successfully",
            "data":serializer.data,
        })
    
    if request.method=='POST':
        serializer=PostApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Added successfully",
            "data":serializer.data,
        })
        
@api_view(['GET','PUT','DELETE'])
def PostApiView(request,id):
    viewdata=PostModel.objects.get(id=id)
    
    if request.method=='GET':
        serializer=PostApiSerializer(viewdata)
        return Response({
            "success":True,
            "message":"Data Got successfully",
            "data":serializer.data,
        })

    if request.method=='PUT':
        serializer=PostApiSerializer(data=request.data,instance=viewdata)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Updated successfully",
            "data":serializer.data,
        })
        
    if request.method=='DELETE':
        viewdata.delete()
        return Response({
            "success":True,
            "message":"Data Deleted successfully",
        })

@api_view(['GET','POST'])
def CommentApiAdd(request):
    if request.method=='GET':
        data=CommentModel.objects.all()
        serializer=CommentApiSerializer(data, many=True)
        return Response({
            "success":True,
            "message":"Data got successfully",
            "data":serializer.data,
        })
    
    if request.method=='POST':
        serializer=CommentApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Added successfully",
            "data":serializer.data,
        })
        
@api_view(['GET','PUT','DELETE'])
def CommentApiView(request,id):
    viewdata=CommentModel.objects.get(id=id)
    
    if request.method=='GET':
        serializer=CommentApiSerializer(viewdata)
        return Response({
            "success":True,
            "message":"Data Got successfully",
            "data":serializer.data,
        })

    if request.method=='PUT':
        serializer=CommentApiSerializer(data=request.data,instance=viewdata)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success":True,
            "message":"Data Updated successfully",
            "data":serializer.data,
        })
        
    if request.method=='DELETE':
        viewdata.delete()
        return Response({
            "success":True,
            "message":"Data Deleted successfully",
        })
        

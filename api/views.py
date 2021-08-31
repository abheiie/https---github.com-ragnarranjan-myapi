from copy import error
from .models import Course
from .serializers import CourseSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def courselist(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializers(course , many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def courselistpk(request,pk):

    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=404)

    if request.method =="GET":
        serializer = CourseSerializers(course)
        return Response(serializer.data)

    elif request.method=='DELETE':
        course.delete()
        return Response(status=204)

    elif request.method == 'PUT':
        serializer = CourseSerializers(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors)

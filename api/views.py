
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task
    
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail-view': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def Overview(request):
    urls = {
        'List': 'api/task-list/',
        'Detail-view': 'api/task-detail/<str:pk>/',
        'Create': 'api/task-create/',
        'Update': 'api/task-update/<str:pk>/',
        'Delete': 'api/task-delete/<str:pk>/',
    }

    return Response(urls)


@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def TaskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def TaskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Task deleted') 

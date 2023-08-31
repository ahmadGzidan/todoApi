from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework.views import APIView


class ApiOverView(APIView):
    def get(self, request, *args, **kwargs):
        api_url = {
            'list': '/task-list/',
            'detail view': '/task-detail/<str:pk>/',
            'create': '/task-create/',
            'update': '/task-update/<str:pk>/',
            'delete': '/task-delete/<str:pk>/',
        }
        return Response(api_url)

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskCreate(CreateAPIView):
    serializer_class = TaskSerializer

class TaskUpdate(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskDelete(DestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'pk'

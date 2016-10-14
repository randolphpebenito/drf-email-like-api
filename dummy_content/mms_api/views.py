from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer
from rest_framework import filters

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  #We use Filters for Ordering so remove order_by part
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields =  ('completed',)
    ordering  = ('-date_created',)


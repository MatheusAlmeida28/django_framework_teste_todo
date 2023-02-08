from app.models import Todo
from app.serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

from rest_framework.viewsets import ModelViewSet

from tmp.models import Tmp
from tmp.serializers import TmpSerializer


class TmpViewSet(ModelViewSet):
    queryset = Tmp.objects.all()
    serializer_class = TmpSerializer

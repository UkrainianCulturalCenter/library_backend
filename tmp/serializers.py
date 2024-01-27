from rest_framework.serializers import ModelSerializer

from tmp.models import Tmp


class TmpSerializer(ModelSerializer):
    class Meta:
        model = Tmp
        fields = "__all__"

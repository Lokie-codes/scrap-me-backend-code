from rest_framework.serializers import ModelSerializer
from .models import FormModel

class FormSerializer(ModelSerializer):
    class Meta:
        model = FormModel
        fields = "__all__"

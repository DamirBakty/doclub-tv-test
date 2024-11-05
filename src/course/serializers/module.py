from rest_framework import serializers

from course.models import Module, TimeCode
from .drug import DrugSerializer
from .farm_company import FarmCompanySerializer
from .file import FileSerializer
from .module_completions import ModuleCompletionSerializer


class TimeCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeCode
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    timecodes = TimeCodeSerializer(many=True, read_only=True)
    drugs = DrugSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)
    farm_company = FarmCompanySerializer(read_only=True)
    module_completions = ModuleCompletionSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = "__all__"

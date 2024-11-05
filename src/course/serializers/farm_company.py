from rest_framework import serializers

from course.models import FarmCompany


class FarmCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmCompany
        fields = "__all__"

from rest_framework import serializers

from .models import ReportTemplate


class ReportTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportTemplate
        fields = '__all__'

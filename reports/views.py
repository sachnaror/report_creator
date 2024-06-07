import json

import pandas as pd
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ReportTemplate
from .serializers import ReportTemplateSerializer


class ReportUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        data = pd.read_excel(file)

        # Convert data to JSON format
        json_data = data.to_json(orient='records')

        # Save the template to the database
        report_template = ReportTemplate.objects.create(name=file.name)
        serializer = ReportTemplateSerializer(report_template)

        return Response({
            "template": serializer.data,
            "json_data": json.loads(json_data)
        }, status=status.HTTP_201_CREATED)

class ReportUploadFromPathView(APIView):
    def get(self, request, *args, **kwargs):
        file_path = '/Users/homesachin/Downloads/Copy of Copy of Owner\'s Operating Statement - Business case.xlsx'
        data = pd.read_excel(file_path)

        # Convert data to JSON format
        json_data = data.to_json(orient='records')

        # Save the template to the database
        report_template = ReportTemplate.objects.create(name='Owner\'s Operating Statement - Business case.xlsx')
        serializer = ReportTemplateSerializer(report_template)

        return Response({
            "template": serializer.data,
            "json_data": json.loads(json_data)
        }, status=status.HTTP_200_OK)

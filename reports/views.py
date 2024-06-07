import json

import pandas as pd
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ReportTemplate
from .serializers import ReportTemplateSerializer


class ReportUploadView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            file = request.FILES['file']
        except KeyError:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return Response({"file_url": file_url}, status=status.HTTP_201_CREATED)

class ReportUploadFromPathView(APIView):
    def get(self, request, *args, **kwargs):
        file_path = '/Users/homesachin/Downloads/test.xlsx'
        data = pd.read_excel(file_path)

        # Convert data to JSON format
        json_data = data.to_json(orient='records')

        # Save the template to the database
        report_template = ReportTemplate.objects.create(name='test.xlsx')
        serializer = ReportTemplateSerializer(report_template)

        return Response({
            "template": serializer.data,
            "json_data": json.loads(json_data)
        }, status=status.HTTP_200_OK)

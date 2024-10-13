# from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DataEntry
from django.http import HttpResponse
from .serializers import DataEntrySerializer, ProcessDataSerializer
from django.shortcuts import get_object_or_404
import time  # For simulating processing delay

# Create your views here.

# Function for displaying the default path
def homepage(request):
    return HttpResponse("<h1>Welcome to the Data Ingestion API</h1>")
    

#  EndPoint for Uploading data
class DataUploadView(generics.CreateAPIView):

    serializer_class = DataEntrySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "status": "success",
                "message": "Data Uploaded successfully"
                # "data_id": serializer.data['id']
            },

            status=status.HTTP_201_CREATED,
            headers=headers
        )

# EndPoint for Processing data
class DataProcessView(APIView):
    def post(self, request, format=None):
        serializer = ProcessDataSerializer(data=request.data)
        if serializer.is_valid():
            data_id = serializer.validated_data['data_id']
            data_entry = get_object_or_404(DataEntry, id=data_id)

            if data_entry.status not in ['uploaded', 'failed']:
                return Response(
                    {"status": "error", "message": f"Data already {data_entry.status}."},
                    status=status.HTTP_404_BAD_REQUEST
                )


                # update status to processing
                data_entry.status = 'processing'
                data_entry.save()

                try:
                    # Simulate data processing delay
                    time.sleep(2) # Remove or replace in production

                    # Example processing: Extract 'field1' from each data item
                    processed = [item.get('field1') for item in data_entry.data]

                    # Update the data entry
                    data_entry.processed_data = processed
                    data_entry.status = 'processed'
                    data_entry.save()

                    return Response (
                        {
                            "status": "success",
                            "processed_data": processed
                        },
                        status=status/HTTP_200_OK
                    )
                except Exception as e:
                    data_entry.status = 'failed'
                    data_entry.save()
                    return Response(
                        {"status": "error", "message": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Endpoint to check the status of data processing.
class DataStatusView(APIView):

    def get(self, request, data_id, format=None):
        data_entry = get_object_or_404(DataEntry, id=data_id)
        serializer = DataEntrySerializer(data_entry)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )


# Endpoint to fetch processed data

class DataResultView(APIView):
    def get(self, request, data_id, format=None):
        data_entry = get_object_or_404(DataEntry, id=data_id)
        if data_entry.status != 'processed':
            return Response(
                # {"status": "error": "message": "Data not processed yet."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"status": "success", "processed_data": data_entry.processed_data},
            status=status.HTTP_200_OK
        )






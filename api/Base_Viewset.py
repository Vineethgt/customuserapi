from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
import rest_framework.mixins as mixin
from url_filter.integrations.drf import DjangoFilterBackend
import six
from .models import User


class BaseViewset(viewsets.ModelViewSet):


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        '''
        if page is not None:
            serializer = self.get_paginated_response(self.get_serializer(page,many = True).data)
        else:
            serializer = self.get_serializer(queryset, many = True)
            '''

        if page is not None:
            serializer = self.get_serializer(page, many = True)
            return self.get_paginated_response({
                "status": "true",
                "message": "data listed successfully.",
                "data": serializer.data
            }
            )

        serializer = self.get_serializer(queryset, many = True)

        return Response({"status": "true", "message": "data listed successfully.", "data": serializer.data})

    def get_object(self, pk):
        try:
            return self.model_class.objects.get(pk=pk)    
        except self.model_class.DoesNotExist:
            raise ValidationError({
                'status': False,
                'message': f"failed to find {self.head}",
                "data": {}
            })

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data={
                "status": True,
                'message': f'{self.head} created',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data={
            'status': False,
            'message': f'error creating {self.head}',
            'data': serializer.errors
        }, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj)
        return Response(
            data={
                "status": True,
                "message": f"{self.head} data reterived sucessfully",
                "data": serializer.data
            })

    def update(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "status": True,
                    "message": f"{self.head} updated sucessfully",
                    "data": serializer.data
                })
        return Response(data={
            "status": False,
            "message": f"{self.head} update failed",
            "data": serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "status": True,
                    "message": f"{self.head} updated sucessfully",
                    "data": serializer.data
                })
        return Response(data={
            "status": False,
            "message": f"{self.head} update failed",
            "data": serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(data={
            "status": True,
            "message": f"{self.head} deleted sucessfully",
            "data": {}
        },
                        status=status.HTTP_200_OK)


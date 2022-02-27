from django.shortcuts import render
from django.http.request import QueryDict
from django.core.exceptions import ObjectDoesNotExist
from .serializers import CardSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helper.format_responses import format_response
from helper.check_validity import checking_valid_email
from django.contrib.auth.hashers  import check_password, make_password
from .models import Card
from .serializers import CardSerializers

import logging
logger = logging.getLogger("api")

# Create your views here.
class AddCard(APIView):
    def post(self, request):
        try:
            input_data = QueryDict.dict(request.data)
            
            if 'card_number' not in input_data:
                return Response(format_response({'message':"Card Numbers are mandatory!..."}, 400),
                        status=status.HTTP_400_BAD_REQUEST)

            if 'expiry_month' in input_data:
                if not input_data['expiry_month']: #cheking if they provide '' value
                    return Response(format_response({'message':"Provide the value for expiry_month field"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(format_response({'message':"Provide the expiry month"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
            if 'expiry_year' in input_data:
                if not input_data['expiry_year']: #cheking if they provide '' value
                    return Response(format_response({'message':"Provide the value for expiry_year field"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(format_response({'message':"Provide the expiry year"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
            
            if 'cvv' in input_data:
                if not input_data['cvv']: #cheking if they provide '' value
                    return Response(format_response({'message':"Provide the value for cvv field"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
            
            else:
                return Response(format_response({'message':"Provide the cvv"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)
            serialized_var = CardSerializers(data = input_data)
            
            if serialized_var.is_valid():
                serialized_var.save()
                context = {
                    'message': 'Card added successfully',
                }
                return Response(format_response(context,201), status=status.HTTP_201_CREATED)
            else:
                return Response(format_response({'message': serialized_var.errors}, 400),
                        status=status.HTTP_400_BAD_REQUEST)
         
        except Exception as e:
            logger.error(f"Exception encountered while user Adding Card:{e}", exc_info=1)
            return Response(format_response({'message':f"Exception encountered while user signing up:{e}"}, 400), 
                        status=status.HTTP_400_BAD_REQUEST)
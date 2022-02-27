from django.shortcuts import render
from django.http.request import QueryDict
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helper.format_responses import format_response
from helper.check_validity import checking_valid_email
from django.contrib.auth.hashers  import check_password, make_password
from .models import UserAccount
from .serializers import UserAccountSerializers, UserAccountSerializers_1

import logging
logger = logging.getLogger("api")

# Create your views here.
class UserLogin(APIView):
    
    def post(self,request):
        try:
            """
            checking if the email and password are providing or not . If not displaying error mesg.
            checking the entered  email-id or not . If not displaying the error mesg .
            """
            input_data = QueryDict.dict(request.data)

            if 'email' not in input_data:
                return Response(format_response({'message':"Provide the email-id"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)

            if 'password' not in input_data:
                return Response(format_response({'message':"Provide the password"}, 400),
                        status=status.HTTP_400_BAD_REQUEST)
                        
            input_data['email'] = input_data['email'].strip() #removing white spaces
            valid_email = checking_valid_email(input_data['email'])
            if not valid_email:
                context = {
                    'message': 'Invalid Email , please provide the valid email',
                }
                return Response(format_response(context, 400),status=status.HTTP_400_BAD_REQUEST)

            if UserAccount.objects.filter(email__iexact = input_data['email']).exists() == True:
                user = is_authenticate(input_data['email'] ,input_data['password'])
                if user:

                    serialized_var = UserAccountSerializers_1(user).data
                    token = Token.objects.create(user=user.id)
                    context = {
                        'message':'Succesfully loggedin' ,
                        'token': token.key,
                        'UserDetails' : serialized_var ,
                    }
                    return Response(format_response(context))
                else:
                    context = {
                        'message': 'Unable to login with provided credentials',
                    }
                    return Response(format_response(context, 400), status=status.HTTP_400_BAD_REQUEST)
            else:
                context = {
                    'message': 'Email does not exist!...',
                }
                return Response(format_response(context, 400), status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Exception encountered while user login:{e}", exc_info=1)
            return Response(format_response({'message':f"Exception encountered while user login:{e}"}, 400), 
                        status=status.HTTP_400_BAD_REQUEST)
    
class UserSignUp(APIView):
    def post(self , request):
        try:
            input_data = QueryDict.dict(request.data)
            """
            checking if the email and password are providing or not . If not displaying error mesg.
            checking the entered  email-id or not . If not displaying the error mesg else insert the data into the table
            """
           
            if 'email' not in input_data:
                return Response(format_response({'message':"Email and password are mandatory!..."}, 400),
                        status=status.HTTP_400_BAD_REQUEST)

            if 'password' in input_data:
                if not input_data['password']: #cheking if they provide '' value
                    return Response(format_response({'message':"Provide the value for password field"}, 400),
                            status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(format_response({'message':"Provide the password"}, 400),
                                status=status.HTTP_400_BAD_REQUEST)

            input_data['email'] = input_data['email'].strip() #removing white spaces
            valid_email = checking_valid_email(input_data['email'])
            if not valid_email:
                context = {
                    'message': 'Invalid Email , please provide the valid email',
                }
                return Response(format_response(context, 400),status=status.HTTP_400_BAD_REQUEST)

            original_password =  input_data['password']
            input_data['password'] = make_password(input_data['password']) #encrypting the password

            if 'username' not in input_data:  # if username not provided , create by spliting the email
                input_data['username'] = input_data['email'].split('@')
            
            user_data = UserAccount.objects.filter(email__iexact = input_data['email']) #query user from model db
            if user_data.exists() != True:
                serialized_var = UserAccountSerializers(data = input_data)
                if serialized_var.is_valid():
                    
                    serialized_var.save()
                    user = UserAccount.objects.filter(email = serialized_var.data['email'])[0]
                    token = Token.objects.create(user=user.id)
                    user_serialized_var = UserAccountSerializers_1(user).data
                    context = {
                        'message':'Successfully registered .Email verification link sent to your registered email ' ,
                        'token' : token.key,
                        'UserDetails' : user_serialized_var ,
                    }
                    return Response(format_response(context , 201) , status=status.HTTP_201_CREATED)
                else: 
                    context = {
                        'message': serialized_var.errors ,
                    }
                    return Response(format_response(context, 400), status=status.HTTP_400_BAD_REQUEST)
            else:
                context = {
                    'message': 'This email-id already registered.',
                }
                return Response(format_response(context, 400), status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Exception encountered while user signing up:{e}", exc_info=1)
            return Response(format_response({'message':f"Exception encountered while user signing up:{e}"}, 400), 
                        status=status.HTTP_400_BAD_REQUEST)

def is_authenticate(email_id, password):
    """
    Authenticate the user
    1. on the basis of email + password : parameters email-id and password : required(email , password)
    return: if success user object, otherwise pass
    """
    try:
        user = UserAccount.objects.get(email__iexact = email_id)
        if check_password(password, user.password):
            return user

    except ObjectDoesNotExist:
        pass
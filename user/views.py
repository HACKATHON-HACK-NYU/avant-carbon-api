import email
import imp
from django.shortcuts import render
from django.http.request import QueryDict

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
    def get(self, request):
        return Response(format_response({"context":"context"}))
    
    # def post(self,request):
    #     try:
    #         """
    #         checking if the email and password are providing or not . If not displaying error mesg.
    #         checking the entered  email-id or not . If not displaying the error mesg .
    #         """
    #         input_data = QueryDict.dict(request.data)

    #         if 'email' not in input_data:
    #             return Response(format_response({'message':"Provide the email-id"}, 400),
    #                     status=status.HTTP_400_BAD_REQUEST)

    #         if 'password' not in input_data:
    #             return Response(format_response({'message':"Provide the password"}, 400),
    #                     status=status.HTTP_400_BAD_REQUEST)
                        
    #         input_data['email'] = input_data['email'].strip() #removing white spaces
    #         valid_email = checking_valid_email(input_data['email'])
    #         if not valid_email:
    #             context = {
    #                 'message': 'Invalid Email , please provide the valid email',
    #             }
    #             return Response(format_response(context, 400),status=status.HTTP_400_BAD_REQUEST)

    #         if UserAccount.objects.filter(email__iexact = input_data['email'],user_type = 2).exists() == True:
    #             user = is_authenticate(input_data['email'] ,input_data['password'])
    #             if user:
    #                 if not user.is_active:
    #                     context = {
    #                         'message': 'User is disabled',
    #                     }
    #                     return Response(format_response(context, 400),status=status.HTTP_400_BAD_REQUEST)

    #                 """ updating the last_login and last_ip to the useraccount table """  
    #                 last_login =  timezone.now() 
    #                 last_ip = get_client_ip(request)
    #                 UserAccount.objects.filter(id = user.id).update(last_login = last_login, last_ip = last_ip )
                    
    #                 """ generating token """
    #                 payload = jwt_payload_generate(user.id ,user.user_type.user_type)
    #                 token = generating_jwt_token(payload)

    #                 serialized_var = UserAccountSerializers_1(user).data
    #                 context = {
    #                     'message':'Succesfully loggedin' ,
    #                     'token' : token ,
    #                     'UserDetails' : serialized_var ,
    #                 }
    #                 return Response(format_response(context))
    #             else:
    #                 context = {
    #                     'message': 'Unable to login with provided credentials',
    #                 }
    #                 return Response(format_response(context, 400), status=status.HTTP_400_BAD_REQUEST)
    #         else:
    #             context = {
    #                 'message': 'Email does not exist!...',
    #             }
    #             return Response(format_response(context, 400), status=status.HTTP_400_BAD_REQUEST)

    #     except Exception as e:
    #         logger.error(f"Exception encountered while user login:{e}", exc_info=1)
    #         return Response(format_response({'message':f"Exception encountered while user login:{e}"}, 400), 
    #                     status=status.HTTP_400_BAD_REQUEST)
    
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
                    print(serialized_var)
                    user = UserAccount.objects.filter(email = serialized_var.data['email'])[0]
                    user_serialized_var = UserAccountSerializers_1(user).data
                    context = {
                        'message':'Successfully registered .Email verification link sent to your registered email ' ,
                        'token' : "token",
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

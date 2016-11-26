from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from trackEvent.models import UserModel, EventModel
from trackEvent.serializers import UserSerializer, EventSerializer

@api_view( ['POST', 'DELETE'] )
def userDetail( request ):
    
    if request.method == 'POST':
        serializer = UserSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse( serializer.data )
        return JsonResponse( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        detail.delete()
        return JsonResponse( status=status.HTTP_204_NO_CONTENT )

@api_view( ['POST', 'DELETE', 'GET'] )
def eventDetail( request ):
    
    if request.method =='POST':
        serializer = EventSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse( serializer.data )
        return JsonResponse( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        detail.delete()
        return JsonResponse( status=status.HTTP_204_NO_CONTENT )
    
@api_view(['GET'])
def current_user( request ):
    queryset = UserModel.objects.all()
    username = request.query_params.get('user_email', None)
    if username is not None:
        queryset = queryset.filter(user_fname=username)
        
    return JsonResponse(  UserSerializer( queryset.all(), many=True ).data[0].items(), safe=False ) 


@api_view(['GET'])
def current_event( request ):
    queryset = EventModel.objects.all()
    username = request.query_params.get('event_title', None)
    if username is not None:
        queryset = queryset.filter(user_fname=username)
        
    return JsonResponse(  EventSerializer( queryset.all(), many=True ).data[0].items(), safe=False ) 






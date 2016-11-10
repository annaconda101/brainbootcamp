from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cbt_logger.serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cbt_logger.models import CbtLog
from cbt_logger.serializers import CbtLogSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
    
@csrf_exempt
def cbt_log_list(request):
    if request.method == 'GET':
        cbt_logs = CbtLog.objects.all()
        cbt_log_serializer = CbtLogSerializer(cbt_logs, many=True)
            
        return JSONResponse(cbt_log_serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        cbt_log_serializer = CbtLogSerializer(data=data)
        
        if cbt_log_serializer.is_valid():
            cbt_log_serializer.save()
            return JSONResponse(cbt_log_serializer.data, status=201)
        return JSONResponse(cbt_log_serializer.errors, status=400)

@csrf_exempt
def cbt_log_detail(request, pk):
    try:
        cbt_log = CbtLog.objects.get(pk=pk)
    except CbtLog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CbtLogSerializer(cbt_log)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request) 
        serializer = CbtLogSerializer(cbt_log, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cbt_log.delete()
        return HttpResponse(status=204)

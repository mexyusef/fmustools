from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import __TABLENAME_CASE__
from .serializers import __TABLENAME_CASE__Serializer
# extra imports

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create__TABLENAME_CASE__(request):
  user = request.user
  __TABLENAME_LOWER__ = __TABLENAME_CASE__.objects.create(
    request.data
  )
  serializer = __TABLENAME_CASE__Serializer(__TABLENAME_LOWER__, many=False)
  return Response(serializer.data)


@api_view(['GET'])
def get__TABLENAME_CASE__s(request):
  orders = __TABLENAME_CASE__.objects.all()
  serializer = __TABLENAME_CASE__Serializer(orders, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def get__TABLENAME_CASE__sWithKeyword(request):
  query = request.query_params.get('keyword')
  if query == None:
    query = ''

  # print('__TABLENAME_LOWER__ list = get__TABLENAME_CAP_PLURAL__, request:', request)
  # print(request.__dict__, file=sys.stderr)

  __TABLENAME_PLURAL_LOWER__ = __TABLENAME_CASE__.objects.filter(name__icontains=query).order_by('-__TEMPLATE_ORDERING_FIELD')

  page = request.query_params.get('page')
  paginator = Paginator(__TABLENAME_PLURAL_LOWER__, 5)

  try:
    __TABLENAME_PLURAL_LOWER__ = paginator.page(page)
  except PageNotAnInteger:
    __TABLENAME_PLURAL_LOWER__ = paginator.page(1)
  except EmptyPage:
    __TABLENAME_PLURAL_LOWER__ = paginator.page(paginator.num_pages)

  if page == None:
    page = 1

  page = int(page)
  print('Page:', page)
  serializer = __TABLENAME_CASE__Serializer(__TABLENAME_PLURAL_LOWER__, many=True)
  return Response({'__TABLENAME_PLURAL_LOWER__': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def get__TABLENAME_CASE__(request, pk):
  print('__TABLENAME_LOWER__ detail, pk:', pk, 'request:', request)
  __TABLENAME_LOWER__ = __TABLENAME_CASE__.objects.get(_id=pk)
  serializer = __TABLENAME_CASE__Serializer(__TABLENAME_LOWER__, many=False)
  # print('__TABLENAME_LOWER__ detail, peroleh:', serializer, 'dg data:', serializer.data)
  return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update__TABLENAME_CASE__(request, pk):
  data = request.data
  __TABLENAME_LOWER__ = __TABLENAME_CASE__.objects.get(_id=pk)
__TEMPLATE_FIELD_ASSIGNMENT_FOR_UPDATE
  __TABLENAME_LOWER__.save()
  serializer = __TABLENAME_CASE__Serializer(__TABLENAME_LOWER__, many=False)
  return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete__TABLENAME_CASE__(request, pk):
  __TABLENAME_LOWER__ = __TABLENAME_CASE__.objects.get(_id=pk)
  __TABLENAME_LOWER__.delete()
  return Response('__TABLENAME_CASE__ed Deleted')


# extra views

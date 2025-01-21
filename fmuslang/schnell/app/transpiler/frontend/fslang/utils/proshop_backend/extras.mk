--% index/fmus
.,d
	order,d
		serializers.py,f(f=serializers.py,@ia=order_serializer="# extra members")
		urls.py,f(f=urls.py,@ia=order_urls="# extra urls")
		views.py,f(f=views.py,@ia=order_views_views="# extra views")
	product,d
		serializers.py,f(f=serializers.py,@ia=product_serializer_import="# extra imports")
		serializers.py,f(f=serializers.py,@ia=product_serializer_member="# extra members")
		urls.py,f(f=urls.py,@ia=product_urls="# extra urls")
		views.py,f(f=views.py,@ia=product_views_import="# extra imports")
		views.py,f(f=views.py,@ia=product_views_views="# extra views")
		# comment out update product utk bbrp field
		views.py,f(f=views.py,@cf="# "="product.image = data['image']")
		views.py,f(f=views.py,@cf="# "="product.numReviews = data['numReviews']")
		views.py,f(f=views.py,@cf="# "="product.rating = data['rating']")
		views.py,f(f=views.py,@cf="# "="product.user = data['user']")
--#

--% product_views_import
from apps.review.models import Review
--#

--% product_views_views
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, pk):
  user = request.user
  product = Product.objects.get(_id=pk)
  data = request.data

  # 1 - Review already exists
  alreadyExists = product.review_set.filter(user=user).exists()
  if alreadyExists:
    content = {'detail': 'Product already reviewed'}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)

  # 2 - No Rating or 0
  elif data['rating'] == 0:
    content = {'detail': 'Please select a rating'}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)

  # 3 - Create review
  else:
    review = Review.objects.create(
      user=user,
      product=product,
      name=user.first_name,
      rating=data['rating'],
      comment=data['comment'],
    )
    reviews = product.review_set.all()
    product.numReviews = len(reviews)

    total = 0
    for i in reviews:
      total += i.rating

    product.rating = total / len(reviews)
    product.save()
    return Response('Review Added')


@api_view(['GET'])
def getTopProducts(request):
  print(' * product/top')
  products = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)



@api_view(['POST'])
def uploadImage(request):
  data = request.data
  product_id = data['product_id']
  product = Product.objects.get(_id=product_id)
  product.image = request.FILES.get('image')
  product.save()
  return Response('Image was uploaded')
--#

--% product_urls
  path('products/upload/', views.uploadImage, name="image-upload"),
  path('products/<str:pk>/reviews/', views.createProductReview, name="create-review"),
  path('products/top/', views.getTopProducts, name='top-products'),
--#

--% product_serializer_import
from apps.review.serializers import ReviewSerializer
--#

--% product_serializer_member
	reviews = serializers.SerializerMethodField(read_only=True)

	def get_reviews(self, obj):
		reviews = obj.review_set.all()
		serializer = ReviewSerializer(reviews, many=True)
		return serializer.data
--#

--% order_views_views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):
  user = request.user
  orders = user.order_set.all()
  serializer = OrderSerializer(orders, many=True)
  return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderToDelivered(request, pk):  
  order = Order.objects.get(_id=pk)
  order.isDelivered = True
  order.deliveredAt = datetime.now()
  order.save()
  return Response('Order was delivered')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, pk):
  order = Order.objects.get(_id=pk)
  order.isPaid = True
  order.paidAt = datetime.now()
  order.save()
  return Response('Order was paid')
--#

--% order_urls
  path('orders/myorders/', views.getMyOrders, name='myorders'),
  path('orders/<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
  path('orders/<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
--#

--% order_serializer
	orderItems = serializers.SerializerMethodField(read_only=True)
	shippingAddress = serializers.SerializerMethodField(read_only=True)
	user = serializers.SerializerMethodField(read_only=True)

	def get_orderItems(self, obj):
		items = obj.orderitem_set.all()
		serializer = OrderItemSerializer(items, many=True)
		return serializer.data

	def get_shippingAddress(self, obj):
		try:
			address = ShippingAddressSerializer(obj.shippingaddress, many=False).data
		except:
			address = False
		return address

	def get_user(self, obj):
		user = obj.user
		serializer = UserSerializer(user, many=False)
		return serializer.data
--#

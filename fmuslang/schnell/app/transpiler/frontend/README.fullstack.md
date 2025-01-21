nda/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
dj/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
fl/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
ns/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
sb/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
fast/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
ndp/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
ml/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}username,s^
== baru
dropwizard mongo
micronaut mongo
quarkus mongo
springboot mongo
fastapi - mongo
flask - mongo
django - mongo
node - mongo

dj/C^[mg://usef:rahasia@localhost:27017/tempdb]
{@Track=#5}title,s,len=100;description,t,b;url,u;created_at,dt:dt,ana;posted_by,fk/User/d=cascade
|
{@Like=#5}user,fk/User/d=cascade;track,fk/Track/d=cascade/rn=likes;created_at,dt:dt,ana^


dj/C^[mg://usef:rahasia@localhost:27017/tempdb]{@Track=#5}title,s,len=100;description,t,b;url,u;created_at,dt:dt,ana;posted_by,fk/User/d=cascade|{@Like=#5}user,fk/User/d=cascade;track,fk/Track/d=cascade/rn=likes;created_at,dt:dt,ana^

*,dj/C^[mg://usef:rahasia@localhost:27017/tempdb]{@Track=#5}title,s,len=100;description,t,b;url,u;created_at,dt:dt,ana;posted_by,fk/User/d=cascade|{@Like=#5}user,fk/User/d=cascade;track,fk/Track/d=cascade/rn=likes;created_at,dt:dt,ana^

*,dj/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Track=#5}title,s,len=100;description,t,b;url,u;created_at,dt:dt,ana;posted_by,fk/User/d=cascade|{@Like=#5}user,fk/User/d=cascade;track,fk/Track/d=cascade/rn=likes;created_at,dt:dt,ana^

/mnt/c/tmp/hapus/fl2/jomo

*,djm/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Track=#5}title,s,len=100;description,t,b;url,u;created_at,dt:dt,ana;posted_by,fk/User/d=cascade|{@Like=#5}user,fk/User/d=cascade;track,fk/Track/d=cascade/rn=likes;created_at,dt:dt,ana^

/mnt/c/tmp/hapus/fl2/jamu

flask-postgres
*,fl/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Track=#5}title,s,len=100;description,t,b;url,u;created_at,dt:dt,ana;posted_by,fk/User/d=cascade|{@Like=#5}user,fk/User/d=cascade;track,fk/Track/d=cascade/rn=likes;created_at,dt:dt,ana^

/mnt/c/tmp/hapus/fl2/flaskp

*,nda/C^[pg://usef:rahasia@localhost:5432/tempdb]

{@Product=#5,ts}title,s,N,tr,len=32;slug,s,u,dbi,uc;blurp,s,r,len=500;description,s,len=2000;price,n,r,len=32,tr;category,fk/Category/d=cascade;subcriptions,[];in_stock,n;sold,n,df=0;images,[];shipping,s,(Yes,No);color,s,(Black,Brown,Silver,White,Blue);brand,s,(Apple,Samsung,Microsoft,Lenovo,ASUS);ratings,[];reviews,[]

*,nda/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Product=#5,ts}title,s,N,tr,len=32;slug,s,u,dbi,uc;blurp,s,r,len=500;description,s,len=2000;price,n,r,len=32,tr;category,fk/Category/d=cascade;subcriptions,[];in_stock,n;sold,n,df=0;images,[];shipping,s,(Yes,No);color,s,(Black,Brown,Silver,White,Blue);brand,s,(Apple,Samsung,Microsoft,Lenovo,ASUS);ratings,[];reviews,[]^
/mnt/c/work/github/sidopharm/backend-njs


AnyNode(faker=5, model='Product', name='table', timestamp=True, type='table')

*,ndam/C^[mg://usef:rahasia@localhost:5432/tempdb] {@Product=#5,ts}title,s,N,tr,len=32;slug,s,u,dbi,uc;blurp,s,r,len=500;description,s,len=2000;price,n,r,len=32,tr;category,fk/Category/d=cascade;subcriptions,[];in_stock,n;sold,n,df=0;images,[];shipping,s,(Yes,No);color,s,(Black,Brown,Silver,White,Blue);brand,s,(Apple,Samsung,Microsoft,Lenovo,ASUS);ratings,[];reviews,[] | {@Category=#5,ts}name,s;slug,s^

/mnt/c/work/github/sidopharm/backend-node-antd-mongo
/mnt/c/work/github/sidopharm/backend-node-antd-mongo/hapus
	subcriptions,[]
		[
			fk/Sub/d=cascade
		]
	ratings
		[
			star,n
			postedBy,fk/User/d=cascade
		]
{@Product=#5}
	user,fk/User,d=setnull,n
	name,s,len=200,n,b
	image,imagefield,n,b,df=/placeholder.png
	brand,s,len=200,n,b
	category,s,len=200,n,b
	description,t,n,b
	rating,decimalfield,digits=7,places=2,n,b
	numReviews,i,n,b,df=0
	price,decimalfield,digits=7,places=2,n,b
	countInStock,i,n,b,df=0
	createdAt,dt:dt,ana
	_id,auto,pk,E (editable=false)

{@Cart=#5,ts}
	products
		[
			{
				product,fk/Product/d=cascade
				count,n
				color,s
				price,n
			}
		]
	cartTotal,n
	totalAfterDiscount,n
	orderBy,fk/User/d=cascade
{@Category=#5,ts}
	name,s
		trim: true
		required: "Name is required"
		minlength: [2, "Too short"]
		maxlength: [32, "Too long"]
	slug,s,u,dbi
		lowercase: true
{@Coupon=#5,ts}
	name,s,u
		trim: true
		uppercase: true,
		required: "Nmae is required",
		minlength: [6, "Too short"],
		maxlength: [12, "Too long"],
	expiry,dt:d,N
	discount,n,N
{@Order=#5,ts}
	products
		[
			{
				product,fk/Product/d=cascade
				count,n
				color,s
			}
		]
	paymentIntent
		{}
	orderStatus,s,(Not Processed, Cash on Delivery, Processing, Dispatched, Cancelled, Completed)
	orderdBy,fk/User/d=cascade
		
{@Product=#5,ts}
	title,s,N,tr,len=32
		trim: true,
		maxlength: 32,
		text: true,
	slug,s,u,dbi
		lowercase: true,
	description,s,N,len=2000
		text: true,
	price,n,N,len=32
		trim: true,
	category,fk/Category/d=cascade
	subs
		[
			fk/Sub/d=cascade
		]
	quantity,n
	sold,n,df=0
	images,[]
	shipping,s,(Yes,No)
	color,s,(Black,Brown,Silver,White,Blue)
	brand,s,(Apple,Samsung,Microsoft,Lenovo,ASUS)
	ratings
		[
			star,n
			postedBy,fk/User/d=cascade
		]
{@Sub=#5,ts}
	name,s,tr,min=2,len=32,r:Name is required
		trim: true,
		required: "Name is required",
		minlength: [2, "Too short"],
		maxlength: [32, "Too long"],
	slug,s,u,dbi,lc
	parent,fk/Category/d=cascade
		required: true = N
		ini hasilkan:
		parent: { type: ObjectId, ref: "Category", required: true },

{@User=#5,ts}
	name,s
	email,s,N,dbi
	role,s,df=subscriber
	cart,[],df=[]
	address,s
	wishlist
		[
			fk/Product/d=cascade
		]

/mnt/c/work/github/sidopharm/backend-njs

bandingkan dg proshop

{@Product=#5}
	user,fk/User,d=setnull,n
	name,s,len=200,n,b
	image,imagefield,n,b,df=/placeholder.png
	brand,s,len=200,n,b
	category,s,len=200,n,b
	description,t,n,b
	rating,decimalfield,digits=7,places=2,n,b
	numReviews,i,n,b,df=0
	price,decimalfield,digits=7,places=2,n,b
	countInStock,i,n,b,df=0
	createdAt,dt:dt,ana
	_id,auto,pk,E (editable=false)
{@Review=#5}
	product,fk/Product/d=setnull,n
	user,fk/User/d=setnull,n
	name,s,len=200,n,b
	rating,i,n,b,df=0
	comment,t,n,b
	createdAt,dt:dt,ana
	_id,auto,pk,E

{@Order=#5}
	user,fk/User,d=setnull,n
	paymentMethod,s,len=200,n,b
	taxPrice,decimal,digits=7,places=2,n,b
	shippingPrice,decimal,digits=7,places=2,n,b
	totalPrice,decimal,digits=7,places=2,n,b
	isPaid,b,df=0 (False? false?)
	paidAt,dt:dt,ana,n,b
	isDelivered,b,df=0
	deliveredAt,dt:dt,ana,n,b
	createdAt,dt:dt,ana
	_id,auto,pk,E

{@OrderItem=#5}
	product,fk/Product/d=setnull,n
	order,fk/Order/d=setnull,n
	name,s,len=200,n,b
	qty,i,n,b,df=0
	price,decimal,digits=7,places=2,n,b
	image,s,len=200,n,b
	_id,auto,pk,E

{@ShippingAddress}
	order,11/Order/d=cascade,n,b
	address,s,len=200,n,b
	city,len=200,n,b
	postalCode,s,len=200,n,b
	country,s,len=200,n,b
	shippingPrice,decimal,digits=7,places=2,n,b
	_id,auto,pk,E


bahas:
title,s,len=100;
description,t,b;url,u;
created_at,dt:dt,ana;
posted_by,fk/User/d=cascade
"columns_types": [
		"String",
		"Text",
		"url",
		"DateTime",
		"ForeignKey"
],
"columns_attributes": [
		[
				""
		],
		[
				""
		],
		[],
		[
				""
		],
		[
				"",
				"User"
		]
],

user,fk/User/d=cascade;
track,fk/Track/d=cascade/rn=likes;
created_at,dt:dt,ana
"columns_types": [
		"ForeignKey",
		"ForeignKey",
		"DateTime"
],
"columns_attributes": [
		[
				"",
				"User"
		],
		[
				"",
				"",
				"Track"
		],
		[
				""
		]
]
[['', 'User'], ['', '', 'Track'], ['']]

flask-mongo

*,flm/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Track=#5}title,s,len=100;description,t,b;url,u;created_at,dt:dt,ana;posted_by,fk/User/d=cascade|{@Like=#5}user,fk/User/d=cascade;track,fk/Track/d=cascade/rn=likes;created_at,dt:dt,ana^

/mnt/c/tmp/hapus/fl2/flaskm














csv statement

fastm/C^username,s^

dbconfig						: "[" dbtype? userpass? hostport? dbspec "]"
dbtype							:  sql_nosql "://"
sql_nosql: 		"mg" -> mongodb
	|						"pg" -> postgresql
	|						"ms" -> mssql
	|						"my" -> mysql
	|						"sqlt" -> sqlite3
userpass						: user ":" pass "@"

timestamps = true
{ts}


[mg://usef:rahasia@localhost:27017/tempdb]
{@Product=#5}
category,s,N
checked,b,df=false
content,s,N
description,s,N
images,[],N
inStock,n,df=0
price,n,N,tr
sold,n,df=0
title,s,N,tr


[mg://usef:rahasia@localhost:27017/tempdb]{@Product=#5}category,s,N;checked,b,df=false;content,s,N;description,s,N;images,[],N;inStock,n,df=0;price,n,N,tr;sold,n,df=0;title,s,N,tr

fastm/C^[mg://usef:rahasia@localhost:27017/tempdb]{@Product=#5}category,s,N;checked,b,df=false;content,s,N;description,s,N;images,[],N;inStock,n,df=0;price,n,N,tr;sold,n,df=0;title,s,N,tr^

*,dj/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter>counter);stop,i,df=0 | {@System=#5}id,i,pk;name,s,len=255 | {@Measurement=#5}id,i,pk;name,s,len=255 | {@Equipment=#5}id,i,pk;name,s,len=255 | {@Room=#5}id,i,pk;name,s,len=255 | {@Floor=#5}id,i,pk;name,s,len=255 | {@Location=#5}id,i,pk;name,s,len=255 | {@Point=#5}id,i,pk;name,s,len=255 | {@Building=#5}id,i,pk;name,s,len=255;building_id,s,len=255;location_text,s,len=500;lalo,dec,digits=22,places=16,b,n;description,s,len=500,b,n;notes,s,len=1000,b,n^

*,dj/C^[mg://usef:rahasia@localhost:27017/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter>counter);stop,i,df=0^
dj/C``[mg://usef:rahasia@localhost:27017/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter>counter);stop,i,df=0``
dj/C``[mg://usef:rahasia@localhost:27017/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter);stop,i,df=0``
dj/C^[mg://usef:rahasia@localhost:27017/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter>counter);stop,i,df=0^


*,nda/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter>counter);stop,i,df=0 | {@System=#5}id,i,pk;name,s,len=255 | {@Measurement=#5}id,i,pk;name,s,len=255 | {@Equipment=#5}id,i,pk;name,s,len=255 | {@Room=#5}id,i,pk;name,s,len=255 | {@Floor=#5}id,i,pk;name,s,len=255 | {@Location=#5}id,i,pk;name,s,len=255 | {@Point=#5}id,i,pk;name,s,len=255 | {@Building=#5}id,i,pk;name,s,len=255;building_id,s,len=255;location_text,s,len=500;lalo,dec,digits=22,places=16,b,n;description,s,len=500,b,n;notes,s,len=1000,b,n^

/mnt/c/tmp/hapus/iot-platform/northside/backend/nda01

smart_building: { type: STRING, default: 'SB_0001', maxlength: [255, "Value too Long"] },
SB_0001 gak diapit...
tambah utk nytimes
title, link, summary, content
|{@News=#5}id,i,pk;title,s,r,len=1000;link,s,len=500;summary,s;content,t

*,nda/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter>counter);stop,i,df=0 | {@System=#5}id,i,pk;name,s,len=255 | {@Measurement=#5}id,i,pk;name,s,len=255 | {@Equipment=#5}id,i,pk;name,s,len=255 | {@Room=#5}id,i,pk;name,s,len=255 | {@Floor=#5}id,i,pk;name,s,len=255 | {@Location=#5}id,i,pk;name,s,len=255 | {@Point=#5}id,i,pk;name,s,len=255 | {@Building=#5}id,i,pk;name,s,len=255;building_id,s,len=255;location_text,s,len=500;lalo,dec,digits=22,places=16,b,n;description,s,len=500,b,n;notes,s,len=1000,b,n|{@News=#5}id,i,pk;title,s,r,len=1000;link,s,len=500;summary,s,len=5000;content,t;tags,s,len=500;images,s,len=5000^

/mnt/c/tmp/hapus/iot-platform/northside/backend/nda01
/mnt/c/tmp/hapus/iot-platform/northside/backend/nda02

*,dj/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Sensor=#5}id,i,pk;building,fk/Building/d=cascade;smart_building,s,len=255,df=SB_0001;sensor_id,s,len=255;min_value,i,df=0;max_value,i,df=100;yellow,i,df=60;red,i,df=80;interval,i,df=1;stopper,s,len=20,(epoch,counter>counter);stop,i,df=0 | {@System=#5}id,i,pk;name,s,len=255 | {@Measurement=#5}id,i,pk;name,s,len=255 | {@Equipment=#5}id,i,pk;name,s,len=255 | {@Room=#5}id,i,pk;name,s,len=255 | {@Floor=#5}id,i,pk;name,s,len=255 | {@Location=#5}id,i,pk;name,s,len=255 | {@Point=#5}id,i,pk;name,s,len=255 | {@Building=#5}id,i,pk;name,s,len=255;building_id,s,len=255;location_text,s,len=500;lalo,dec,digits=22,places=16,b,n;description,s,len=500,b,n;notes,s,len=1000,b,n|{@News=#5}id,i,pk;title,s,r,len=1000;link,s,len=500;summary,s,len=5000;content,t;tags,s,len=500;images,s,len=5000^

/mnt/c/tmp/hapus/iot-platform/northside/backend/dj02

todo
--
done
content
category

corona
--
country
cases
deaths
date
totalcases
totaldeaths
totalrecovered

/mnt/c/tmp/hapus/iot-platform/northside/backend/corona/dj01
/mnt/c/tmp/hapus/iot-platform/northside/backend/corona/nda01
*,dj/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Corona=#5}id,i,pk,ai;country,s;cases,i;deaths,i;date,dt:d|{@Todo=#5}done,b,df=false;content,s,len=5000;category,s^
*,nda/C^[pg://usef:rahasia@localhost:5432/tempdb]{@Corona=#5}id,i,pk,ai;country,s;cases,i;deaths,i;date,dt:d|{@Todo=#5}done,b,df=false;content,s,len=5000;category,s^

todo:
gak ada auto_increment, but:
id              = models.AutoField(primary_key=True)
jk colomn tidak ada id, maka buatkan otomatis

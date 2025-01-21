# Objective

## generate - modify - generate cycle
ini adlh pekerjaan utama kita spt ini
sampai hasilkan sst yg bener2 menarik

python, js, ts, java, ...
+ fullstack
+ cloud (docker, kube, aws/gcp)

utk c++, c#, rust => bikin video streaming server...

## hafalkan, camkan

all/C^...^ atau fs/C^...^
C = csv...
^...^ pengapit kode

## iterate 1

all/C^[usef:rahasia@localhost:27017/tempdb]{@Product=#5}name,s;brand,s;model,s^

sementara kita fokus dulu di node-pg+frontends

lesson:
fullstack punya:
class Coordinator:
  def __init__(self, RootNode, project_dir='input'):
  def generate(self):

input dari user bisa dimodifikasi:
minta dari user....
lalu jadi root folder utk semua proyek
dari csv statement, semua dipanggil dg 
om .node_antd import Coordinator as node_antd_generator
from .node_antd_mongo import Coordinator as node_antd_mongo_generator
	'node_antd': node_antd_generator,	
	'node_antd_mongo': node_antd_mongo_generator,	
generator = generator_by_backend[konfigurasi_backend] (RootNode)
generator.generate()
terima mk file: generator.output() danr baris_entry = 'index/fmus'
jadi gak pernah diberikan "project_dir" argumen...
lalu hrs lanjut dg:
					if config['fmus'] == 'execute':
						print('lets execute the prisoners now!', program_config)
						from app.fileutils import get_definition_by_key_permissive_start
						from app.fmus import Fmus
						filepath = program_config['filepath']
						baris_entry = program_config['baris_entry']
						program = get_definition_by_key_permissive_start(filepath, baris_entry)
						fmus = Fmus(False)
						fmus.set_file_dir_template(filepath)
						fmus.process(program)
  def output(self):
    return self.mkfile_output

all/C^[usef:rahasia@localhost:5432/tempdb]{@Product=#5}name,s;brand,s;model,s^
/mnt/c/tmp/hapus/fullstacker

## iterate 2
/mnt/c/fullstack-modify

all/C^[usef:rahasia@localhost:5432/tempdb]{@News=#5}id,i,pk,ai;title,s,r,len=1000;link,s,len=500;summary,s,len=5000;content,t;tags,s,len=500;images,s,len=5000^

## iterate 3

/mnt/c/fullstack-modify/django-pg

dj,*/C^[usef:rahasia@localhost:5432/tempdb]{@ShippingAddress=#10}order,11/Order/d=cascade,n,b;address,s,len=200,n,b;city,s,len=200,n,b;postalCode,s,len=200,n,b;country,s,len=200,n,b;shippingPrice,dec,digits=7,places=2,n,b;_id,auto,pk,E | {@OrderItem=#10}product,fk/Product/d=setnull,n;order,fk/Order/d=setnull,n;name,s,len=200,n,b;qty,i,n,b,df=0;price,dec,digits=7,places=2,n,b;image,s,len=200,n,b;_id,auto,pk,E | {@Order=#10,ts}user,fk/User/d=setnull,n;paymentMethod,s,len=200,n,b;taxPrice,dec,digits=7,places=2,n,b;shippingPrice,dec,digits=7,places=2,n,b;totalPrice,dec,digits=7,places=2,n,b;isPaid,b,df=False;paidAt,ts,ana,n,b;isDelivered,b,df=False;deliveredAt,ts,ana,n,b;_id,auto,pk,E | {@Product=#10,ts}_id,auto,pk,E;brand,s,len=200,n,b;category,s,len=200,n,b;countInStock,i,n,b,df=0;description,t,n,b;image,img,n,b;name,s,len=200,n,b;numReviews,i,n,b,df=0;price,dec,digits=7,places=2,n,b;rating,dec,digits=7,places=2,n,b;user,fk/User/d=setnull,n | {@Review=#10,ts}user,fk/User/d=setnull,n;product,fk/Product/d=setnull,n;name,s,len=200,n,b;rating,i,n,b,df=0;comment,t,n,b;_id,auto,pk,E^

## iterate 4: assistance
/mnt/c/fullstack-modify/assistance

all/C^[usef:rahasia@localhost:5432/tempdb]{@ShippingAddress=#10}order,11/Order/d=cascade,n,b;address,s,len=200,n,b;city,s,len=200,n,b;postalCode,s,len=200,n,b;country,s,len=200,n,b;shippingPrice,dec,digits=7,places=2,n,b;_id,auto,pk,E | {@OrderItem=#10}product,fk/Product/d=setnull,n;order,fk/Order/d=setnull,n;name,s,len=200,n,b;qty,i,n,b,df=0;price,dec,digits=7,places=2,n,b;image,s,len=200,n,b;_id,auto,pk,E | {@Order=#10,ts}user,fk/User/d=setnull,n;paymentMethod,s,len=200,n,b;taxPrice,dec,digits=7,places=2,n,b;shippingPrice,dec,digits=7,places=2,n,b;totalPrice,dec,digits=7,places=2,n,b;isPaid,b,df=False;paidAt,ts,ana,n,b;isDelivered,b,df=False;deliveredAt,ts,ana,n,b;_id,auto,pk,E | {@Product=#10,ts}_id,auto,pk,E;brand,s,len=200,n,b;category,s,len=200,n,b;countInStock,i,n,b,df=0;description,t,n,b;image,img,n,b;name,s,len=200,n,b;numReviews,i,n,b,df=0;price,dec,digits=7,places=2,n,b;rating,dec,digits=7,places=2,n,b;user,fk/User/d=setnull,n | {@Review=#10,ts}user,fk/User/d=setnull,n;product,fk/Product/d=setnull,n;name,s,len=200,n,b;rating,i,n,b,df=0;comment,t,n,b;_id,auto,pk,E^

## iterate 5: assistance
/mnt/c/fullstack-modify/assistance2

all/C^[usef:rahasia@localhost:5432/tempdb]{@ShippingAddress=#10}order,11/Order/d=cascade,n,b;address,s,len=200,n,b;city,s,len=200,n,b;postalCode,s,len=200,n,b;country,s,len=200,n,b;shippingPrice,dec,digits=7,places=2,n,b;_id,auto,pk,E | {@OrderItem=#10}product,fk/Product/d=setnull,n;order,fk/Order/d=setnull,n;name,s,len=200,n,b;qty,i,n,b,df=0;price,dec,digits=7,places=2,n,b;image,s,len=200,n,b;_id,auto,pk,E | {@Order=#10,ts}user,fk/User/d=setnull,n;paymentMethod,s,len=200,n,b;taxPrice,dec,digits=7,places=2,n,b;shippingPrice,dec,digits=7,places=2,n,b;totalPrice,dec,digits=7,places=2,n,b;isPaid,b,df=False;paidAt,ts,ana,n,b;isDelivered,b,df=False;deliveredAt,ts,ana,n,b;_id,auto,pk,E | {@Product=#10,ts}_id,auto,pk,E;brand,s,len=200,n,b;category,s,len=200,n,b;countInStock,i,n,b,df=0;description,t,n,b;image,img,n,b;name,s,len=200,n,b;numReviews,i,n,b,df=0;price,dec,digits=7,places=2,n,b;rating,dec,digits=7,places=2,n,b;user,fk/User/d=setnull,n | {@Review=#10,ts}user,fk/User/d=setnull,n;product,fk/Product/d=setnull,n;name,s,len=200,n,b;rating,i,n,b,df=0;comment,t,n,b;_id,auto,pk,E | {@Cart=#10}product_id,i;user_id,i;shippingaddress_id,i | {@User=#10}username,s;name,s;first_name,s;last_name,s;email,s;phone,s;is_active,b;is_staff,b;roles,s,(admin,user,guest>user) ^

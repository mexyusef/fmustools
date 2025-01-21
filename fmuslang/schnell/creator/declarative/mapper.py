import os, json
disini = os.path.abspath(os.path.dirname(__file__))
rootdir = os.path.join(disini, os.pardir, os.pardir, os.pardir)
declangconfig = os.path.normpath(os.path.join(rootdir, 'declang.json'))
declangvalues = None
with open(declangconfig, 'r') as f:
	declangvalues = json.load(f)

elem_mapper = declangvalues['elem_mapper']
attr_mapper = declangvalues['attr_mapper']
cdata_mapper = declangvalues['cdata_mapper']
value_mapper = declangvalues['value_mapper']

def reload_values():
	global declangvalues, elem_mapper, attr_mapper, cdata_mapper, value_mapper
	with open(declangconfig, 'r') as f:
		declangvalues = json.load(f)

	elem_mapper = declangvalues['elem_mapper']
	attr_mapper = declangvalues['attr_mapper']
	cdata_mapper = declangvalues['cdata_mapper']
	value_mapper = declangvalues['value_mapper']


elem_html = {
	'a': '',
	'b': '',
	'c': '',
	'd': '',
	'e': '',
	'f': '',
	'g': '',
	'h': '',
	'i': '',
	'j': '',
	'k': '',
	'l': '',
	'm': '',
	'n': '',
	'o': '',
	'p': '',
	'q': '',
	'r': '',
	's': '',
	't': '',
	'u': '',
	'v': '',
	'w': '',
	'x': '',
	'y': '',
	'z': '',
}

attr_html = {}
cdata_html = {}
value_html = {}

elem_kubernetes_ini = """
A=app
anno=annotations
av=apiVersion
acm=accessModes
be=backend
bo=backoffLimit
cm=configMap
cmkr=configMapKeyRef
cmd=command
comp=completions
cP=containerPort
c=containers
d=data
dns=dnsPolicy
env=environment
h=host
ht=http
hp=hostPath
i=image
imp=imagePullPolicy
iC=initContainers
jt=jobTemplate
k=kind
K=key
Ks=keys
l=labels
ml=matchLabels
mx=matchExpressions
mt=metadata
mar=maxReplicas
mir=minReplicas
mas=maxSurge
mau=maxUnavailable
n=name
ns=namespace
nsel=nodeSelector
P=port
p=ports
pa=paths
Pa=path
pl=parallelism
pro=protocol
pv=providers
par=parameters
r=replicas
ru=rules
rw1=ReadWriteOnce
res=resources
rollu=rollingUpdate
rpol=restartPolicy
s=spec
sch=schedule
sec=secret
secn=secretName
sel=selector
st=strategy
so=storage
socn=storageClassName
svn=serviceName
svp=servicePort
t=template
ti=tier
tol=tolerations
tp=targetPort
us=updateStrategy
v=volumes
vf=valueFrom
vm=volumeMounts
y=type
"""

cdata_kubernetes_ini = """
a1=apps/v1
b1=batch/v1
bv1=batch/v1beta1
n1=networking.k8s.io/v1
ce1=ceph.rook.io/v1
conf1=apiserver.config.k8s.io/v1
so1=storage.k8s.io/v1
ce=CephBlockPool
cj=CronJob
cm=ConfigMap
cip=ClusterIP
d=Deployment
df=default
ds=DaemonSet
ec=EncryptionConfiguration
hpa=HorizontalPodAutoscaler
i=Ingress
ifnp=IfNotPresent
j=Job
np=NodePort
p=Pod
pv=PersistentVolume
pvc=PersistentVolumeClaim
rec=Recreate
rollu=RollingUpdate
rs=ReplicaSet
ss=StatefulSet
sv=Service
sc=StorageClass
"""
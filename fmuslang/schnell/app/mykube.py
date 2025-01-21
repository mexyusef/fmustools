import kubernetes
from kubernetes import client, config
# https://github.com/kubernetes-client/python
# https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/


config.load_kube_config()
v1 = client.CoreV1Api()

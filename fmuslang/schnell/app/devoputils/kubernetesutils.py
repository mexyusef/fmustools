# User
# give me python functions i need to use if i want to be able to administrate Kubernetes that are used by as containers for enterprise fullstack application in my company?
# ChatGPT
# To administer a Kubernetes cluster and manage containers for an enterprise full-stack application, you'll need to use the Kubernetes Python client library. The official library is called kubernetes and can be installed using:

# bash

# pip install kubernetes

# Here are some essential Python functions using the kubernetes library for common Kubernetes administrative tasks:

# List Pods in a Namespace:



from kubernetes import client, config

def list_pods(namespace):
    config.load_kube_config()  # or use config.load_incluster_config() if running inside a pod
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        print(f"Pod Name: {pod.metadata.name}, Status: {pod.status.phase}")

list_pods("your_namespace")
# Deploying a Deployment:

from kubernetes import client, config

def deploy_deployment(namespace, deployment_name, image_name, replicas=3):
    config.load_kube_config()
    apps_api = client.AppsV1Api()
    deployment_manifest = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": deployment_name},
        "spec": {
            "replicas": replicas,
            "selector": {"matchLabels": {"app": deployment_name}},
            "template": {
                "metadata": {"labels": {"app": deployment_name}},
                "spec": {
                    "containers": [
                        {"name": deployment_name, "image": image_name}
                    ]
                }
            }
        }
    }
    apps_api.create_namespaced_deployment(namespace, body=deployment_manifest)

deploy_deployment("your_namespace", "your_deployment", "your_image")
# Scaling a Deployment:



from kubernetes import client, config

def scale_deployment(namespace, deployment_name, replicas):
    config.load_kube_config()
    apps_api = client.AppsV1Api()
    apps_api.patch_namespaced_deployment_scale(
        name=deployment_name,
        namespace=namespace,
        body={"spec": {"replicas": replicas}}
    )

scale_deployment("your_namespace", "your_deployment", replicas=5)
# Deleting a Deployment:

from kubernetes import client, config

def delete_deployment(namespace, deployment_name):
    config.load_kube_config()
    apps_api = client.AppsV1Api()
    apps_api.delete_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=client.V1DeleteOptions(propagation_policy='Foreground', grace_period_seconds=5)
    )

delete_deployment("your_namespace", "your_deployment")
# Pod Logs:

from kubernetes import client, config

def get_pod_logs(namespace, pod_name, container_name=""):
    config.load_kube_config()
    core_api = client.CoreV1Api()
    logs = core_api.read_namespaced_pod_log(name=pod_name, namespace=namespace, container=container_name)
    print(logs)

get_pod_logs("your_namespace", "your_pod_name")
# These functions cover some basic operations. Depending on your specific use case, you may need additional functions for tasks like handling ConfigMaps, Secrets, Services, Persistent Volumes, etc. Refer to the official Kubernetes Python client documentation for more details: Kubernetes Python Client.

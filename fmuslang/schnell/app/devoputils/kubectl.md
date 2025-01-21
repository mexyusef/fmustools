Certainly! Here are 25 `kubectl` commands that are commonly used for administering, deploying, managing, and monitoring Kubernetes, including scenarios with Minikube:

1. **Check Kubernetes version:**
   ```bash
   kubectl version
   ```

2. **List all nodes in the cluster:**
   ```bash
   kubectl get nodes
   ```

3. **List all pods in the default namespace:**
   ```bash
   kubectl get pods
   ```

4. **List all pods in all namespaces:**
   ```bash
   kubectl get pods --all-namespaces
   ```

5. **Describe a pod:**
   ```bash
   kubectl describe pod <pod-name>
   ```

6. **List all services:**
   ```bash
   kubectl get services
   ```

7. **Expose a deployment as a service:**
   ```bash
   kubectl expose deployment <deployment-name> --type=LoadBalancer --port=<port>
   ```

8. **Scale a deployment:**
   ```bash
   kubectl scale deployment <deployment-name> --replicas=<number-of-replicas>
   ```

9. **Rolling update for a deployment:**
   ```bash
   kubectl set image deployment/<deployment-name> <container-name>=<new-image>
   ```

10. **Delete a deployment:**
    ```bash
    kubectl delete deployment <deployment-name>
    ```

11. **Create a namespace:**
    ```bash
    kubectl create namespace <namespace-name>
    ```

12. **Switch to a specific namespace:**
    ```bash
    kubectl config set-context --current --namespace=<namespace-name>
    ```

13. **Create a secret:**
    ```bash
    kubectl create secret generic <secret-name> --from-literal=<key>=<value>
    ```

14. **Apply a configuration file:**
    ```bash
    kubectl apply -f <filename.yaml>
    ```

15. **List all persistent volumes:**
    ```bash
    kubectl get pv
    ```

16. **List all persistent volume claims:**
    ```bash
    kubectl get pvc
    ```

17. **Execute a command in a running pod:**
    ```bash
    kubectl exec -it <pod-name> -- /bin/bash
    ```

18. **Port-forward to a pod:**
    ```bash
    kubectl port-forward <pod-name> <local-port>:<pod-port>
    ```

19. **Create a Minikube cluster:**
    ```bash
    minikube start
    ```

20. **Enable Minikube dashboard:**
    ```bash
    minikube dashboard
    ```

21. **Check Minikube status:**
    ```bash
    minikube status
    ```

22. **Stop Minikube cluster:**
    ```bash
    minikube stop
    ```

23. **Delete Minikube cluster:**
    ```bash
    minikube delete
    ```

24. **View logs for a pod:**
    ```bash
    kubectl logs <pod-name>
    ```

25. **Set up a proxy to the Kubernetes API server:**
    ```bash
    kubectl proxy
    ```

These commands cover a range of common scenarios in Kubernetes administration and should be helpful for managing a full-stack application. Adjust the parameters as needed for your specific environment and application requirements.












Certainly! Here are additional `kubectl` commands that can be useful for different scenarios in Kubernetes administration:

26. **List all deployments:**
    ```bash
    kubectl get deployments
    ```

27. **List all replica sets:**
    ```bash
    kubectl get replicasets
    ```

28. **List all services in a specific namespace:**
    ```bash
    kubectl get services -n <namespace-name>
    ```

29. **Create a deployment using a specific image:**
    ```bash
    kubectl create deployment <deployment-name> --image=<image-name>
    ```

30. **Scale a deployment imperatively:**
    ```bash
    kubectl scale --replicas=<number-of-replicas> deployment/<deployment-name>
    ```

31. **Rollback a deployment to a previous revision:**
    ```bash
    kubectl rollout undo deployment/<deployment-name>
    ```

32. **List all ConfigMaps:**
    ```bash
    kubectl get configmaps
    ```

33. **Create a ConfigMap from a file:**
    ```bash
    kubectl create configmap <configmap-name> --from-file=<path/to/file>
    ```

34. **List all secrets:**
    ```bash
    kubectl get secrets
    ```

35. **Edit a resource in the default editor:**
    ```bash
    kubectl edit <resource-type> <resource-name>
    ```

36. **Create a Horizontal Pod Autoscaler:**
    ```bash
    kubectl autoscale deployment <deployment-name> --cpu-percent=<target-percent> --min=<min-replicas> --max=<max-replicas>
    ```

37. **Check the events in a namespace:**
    ```bash
    kubectl get events -n <namespace-name>
    ```

38. **List all available API resources:**
    ```bash
    kubectl api-resources
    ```

39. **Get a shell into a running container:**
    ```bash
    kubectl exec -it <pod-name> --container <container-name> -- /bin/bash
    ```

40. **Forward a local port to a pod:**
    ```bash
    kubectl port-forward <pod-name> <local-port>:<pod-port>
    ```

41. **Delete all resources in a namespace (use with caution):**
    ```bash
    kubectl delete all --all -n <namespace-name>
    ```

42. **Get information about the current context:**
    ```bash
    kubectl config get-contexts
    ```

43. **Get information about a specific resource quota:**
    ```bash
    kubectl describe resourcequota <resourcequota-name>
    ```

44. **View the YAML representation of a resource:**
    ```bash
    kubectl get <resource-type> <resource-name> -o yaml
    ```

45. **Apply a configuration file to update resources:**
    ```bash
    kubectl apply -f <filename.yaml>
    ```

These additional commands cover a broader range of Kubernetes management tasks. Make sure to adapt them to your specific use case and requirements.
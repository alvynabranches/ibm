gcloud auth application-default login
cd terraform
terraform init && terraform apply
gcloud container clusters get-credentials primary --zone us-central1-a --project gpt-j-and-gpt-neox20b
kubectl get svc
kubectl get nodes
kubectl get pods
kubectl apply -f k8s/prod/app-deployment.yaml
kubectl apply -f k8s/prod/cloud-deployment.yaml
kubectl get ns
kubectl get pods -n prod
kubectl exec -n -it <name>
# staging alpha storage ls
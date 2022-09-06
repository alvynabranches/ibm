gcloud auth application-default login
cd terraform
terraform init && terraform apply
gcloud container clusters get-credentials primary --zone us-central1-a --project gpt-j-and-gpt-neox20b
kubectl get svc
kubectl get nodes

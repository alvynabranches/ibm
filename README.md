# IBM Coding Challenge

## Problem Statement
1. Develop a basic application exposing 2 simple REST API endpoints (POST, GET)
    - POST - store some persistent data
    - GET - retrieve data

2. Implement automation that deploys and makes available the REST API endpoints on a Kubernetes environment (eg: CI/CD)

3. Implement automation that provisions all infrastructure elements that are used to run the solution

Consider code quality, security, stability / reliability.
You may pick any language and technology of your choice for this exercise.
The solution must run on Cloud ( IBM Cloud or other)

## Solution
1. 
    - The application is prepared using flask, wherein the application takes a json data from the post request and stores in a json file. 
    - The application returns all the data from the json file. 

2. To implement the CI / CD, I have used github workflows.
    - Workflows are free hence I went with this option. 
    - The [deployment.yaml](.github/workflows/deployment.yaml) is a end to end workflows for deployment of the flask app on to GKE. 

3. To automate the creation of infrastructure I have used terraform. 
    - The [provider.tf](./terraform/1-provider.tf) provides all instructions to create the provider.
    - The [vpc.tf](./terraform/2-vpc.tf) provides all instructions to create the VPC.
    - The [subnets.tf](./terraform/3-subnets.tf) provides all instructions to create the subnets.
    - The [router.tf](./terraform/4-router.tf) provides all instructions to create the router.
    - The [nat.tf](./terraform/5-nat.tf) provides all instructions to create the NAT.
    - The [firewalls.tf](./terraform/6-firewall.tf) provides all instructions to create the firewalls.
    - The [kubernetes.tf](./terraform/7-kubernetes.tf) provides all instructions to create the Kubernetes cluster.
    - The [node-pools.tf](./terraform/8-node-pools.tf) provides all instructions to create the node pools.
    - The [service-accounts.tf](./terraform/9-service-account.tf) file provides instructions to create a service account on the mentioned project. 

    - *To run the terraform files, it is first required that the device is logged in with GCP authentication. Commands found in this [file](./cmd.sh)*
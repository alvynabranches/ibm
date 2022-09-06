provider "google" {
    project = "gpt-j-and-gpt-neox20b"
    region = "us-central1"
}

terraform {
    backend "gcs" {
        bucket = "app-deploy-prod"
        prefix = "terraform/state"
    }
    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~> 4.0"
        }
    }
}
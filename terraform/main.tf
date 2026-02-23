terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
  }
}

provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "minikube"
}

resource "kubernetes_namespace" "todo" {
  metadata {
    name = var.namespace
    labels = {
      environment = var.environment
      managed-by  = "terraform"
    }
  }
}

resource "kubernetes_config_map" "todo_config" {
  metadata {
    name      = "todo-config"
    namespace = kubernetes_namespace.todo.metadata[0].name
  }

  data = {
    APP_ENV     = var.environment
    APP_VERSION = var.app_version
    APP_PORT    = "5000"
  }
}
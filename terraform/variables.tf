variable "namespace" {
  description = "Kubernetes namespace for the app"
  type        = string
  default     = "todo-app"
}

variable "app_version" {
  description = "App version label"
  type        = string
  default     = "v1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "development"
}
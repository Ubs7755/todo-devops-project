output "namespace_name" {
  value = kubernetes_namespace.todo.metadata[0].name
}

output "config_map_name" {
  value = kubernetes_config_map.todo_config.metadata[0].name
}
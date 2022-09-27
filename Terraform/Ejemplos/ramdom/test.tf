resource "random_string" "random" {
  length           = 16
  special          = true
  override_special = "/@£$"
}

output "claver" {
  description = "DNS pública del load balancer"
  value       = random_string.random.result
}


output "claver2" {
  description = "DNS pública del load balancer 2"
  value       = random_string.random.result
}


resource "random_string" "password" {
  length = 16
  special = true
  override_special = "/@\" "
}

resource "aws_db_instance" "example" {
  password = "${random_string.password.result}"
}




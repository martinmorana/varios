# -------------------------
# Define el provider de AWS
# -------------------------
provider "aws" {
  region = "us-east-1"
}

variable "usuarios" {
  description = "Nombre usuarios IAM"
  type        = number
}

resource "aws_iam_user" "ejemplo" {
  count = var.usuarios

  name = "usuario-${count.index}"
}

output "arn_usuario" {
  value = aws_iam_user.ejemplo[2].arn
}

output "arn_todos_usuarios" {
  value = aws_iam_user.ejemplo[*].arn
}

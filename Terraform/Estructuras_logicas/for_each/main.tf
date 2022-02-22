# -------------------------
# Define el provider de AWS
# -------------------------
provider "aws" {
  region = "us-east-1"
}

variable "usuarios" {
  description = "Nombre usuarios IAM"
  type        = set(string)
}

resource "aws_iam_user" "ejemplo" {
  for_each = var.usuarios

  name = "usuario-${each.value}"
}

# -------------------------
# Define el provider de AWS
# -------------------------
provider "aws" {
  region = "us-east-1"
}

# ---------------------------------
# Crea un <var.usuarios> de IAM
# ---------------------------------
resource "aws_iam_user" "ejemplo" {
  count = 2

  name = "usuario-ejemplo.${count.index}"
}

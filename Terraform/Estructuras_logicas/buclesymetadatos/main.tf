# -------------------------
# Define el provider de AWS
# -------------------------
provider "aws" {
  region = "us-east-1"
}

# ---------------------------------------
# Define una instancia EC2 con AMI Ubuntu
# ---------------------------------------
resource "aws_instance" "mi_servidor" {
  count = 2

  ami           = "ami-033b95fb8079dc481"
  instance_type = "t2.micro"
}


# ---------------------------------
# Define número de usuarios a crear
# ---------------------------------
variable "usuarios" {
  description = "Nombre de usuarios IAM"
  type        = list(string)
}

variable "a" {
  description = "Nombre de usuarios IAM"
  type        = string
}


# ---------------------------------
# Crea un <var.usuarios> de IAM
# ---------------------------------
resource "null_resource" "ejemplo" {
 count = "${length(var.usuarios) > 4 ? (length(var.usuarios) * length(var.usuarios)) : 0}"
 var.a != "" ? var.a : "default-a"
 triggers = {
    #name = "usuario-${var.usuarios[count.index]}"
    

  }
  
}

  
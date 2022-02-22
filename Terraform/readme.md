erraform Variables
💡 Usaremos variables siempre que necesitemos tener un valor estático en nuestra configuración.
Un cambio en el este valor estático debería producirse en solo un lugar, es decir, en la instanciación de la variable.  

💻 Jerarquía de Precedencia


Si asignamos a una variable un valor por diferentes mecanismos, ¿cuál es la precedencia y qué valor final tendrá?

Precedencia de menos a más, es decir, más abajo en la lista tiene precedencia sobre los primeros puntos:

Variables de entorno

Fichero terraform.tfvars

Fichero terraform.tfvars.json

Ficheros acabados en .auto.tfvars o .auto.tfvars.json, si hay más de uno, será en orden lexicográfico

Cualquier variable -var o -var-file, en el orden que son especificadas

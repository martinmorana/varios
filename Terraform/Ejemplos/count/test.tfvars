# PATH del secret con los datos del login del RDS
secret_path        = "secret/rds-lab"
db_port            = 5432
db_host            = "localhost"
db_sslmode         = "disable"
db_connect_timeout = 15

usuarios = ["uno", "dos", "tres", "cuatreo", "cinco"]
a = ""

# Mapa con bases a crear.
databases_map = {
  0 = {
    db_name           = "db10"
    vault_secret_path = "secret/db/db10"
    username          = "user_db10"

  }
  1 = {
    db_name           = "db11"
    vault_secret_path = "secret/db/db11"
    username          = "user_db11"

  }
  /*  2 = {
    db_name           = "db12"
    vault_secret_path = "secret/db/db12"
    username          = "user_db12"

  }
  3 = {
    db_name           = "db13"
    vault_secret_path = "secret/db/db13"
    username          = "user_db13"

  } */
}

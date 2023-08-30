terraform {
 required_providers{
   docker = {
     source = "kreuzwerker/docker"
     version = "~> 2.22.0"
      }
    }
  }
resource "docker_image" "gitlab" {
  name         = "registry.gitlab.com/alta3/simplegoservice"
  keep_locally = true    // keep image after "destroy"
}
resource "docker_container" "simplegoservice"{
  image = docker_image.gitlab.image_id
  name = var.container_name
  ports {
    internal = var.internal_port
    external = var.external_port
  }
}
variable "container_name"{
type = string
default = "AltaResearchWebService"
}
variable "internal_port"{
type = number
default = 9876
}
variable "external_port"{
type = number
default = 5432
}

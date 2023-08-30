variable "container_name" {
  description = "Value of the name for the Docker container"
  # basic types include string, number and bool
  type        = string
  default     = "ExampleNginxContainer"
}
variable "inter_num" {
description = "inernal port number"
type = number
default = 80
}
variable "exter_num" {
description = "external port number"
type = number
default = 2224
}

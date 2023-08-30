terraform {
  required_providers {
    http = {
      source = "hashicorp/http"
      version = "3.0.1"
    }
  }
}

provider "http" {
  # Configuration options
}
# The following example shows how to issue an HTTP GET request supplying
# an optional request header.
data "http" "api" {
  url = "https://pokeapi.co/api/v2/pokemon/"      // API to send HTTP GET to

  # Optional request headers
  request_headers = {
    Accept = "application/json"
  }
}
# produces an output value named "space_heroes"
output "pokemon" {
  description = "API that documents pokemon"
  value       = data.http.api.response_body
}

# produces legal JSON output value named "space_heroes_json"
output "pokemon_json" {
  description = "API that documents folks in space"
  value       = jsondecode(data.http.api.response_body)    // note the jsondecode()
}    


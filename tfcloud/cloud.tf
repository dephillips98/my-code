terraform {
  cloud {
    organization = "dp123"

    workspaces {
      name = "my-example"
    }
  }
}

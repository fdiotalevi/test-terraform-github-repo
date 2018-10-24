variable "TOKEN" {
  type = "string"
  description = "Github access token"
}

provider "github" {
    token = "${var.TOKEN}"
    organization = "test-filippo-org"
}

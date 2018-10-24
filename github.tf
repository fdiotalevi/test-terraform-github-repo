variable "REPO_NAME" {
  type = "string"
  description = "name of the repository to create"
}

resource "github_repository" "new_repo" {
  name        = "${var.REPO_NAME}"

  private = false
}

resource "github_team_repository" "some_team_repo" {
  team_id    = "2972513"
  repository = "${var.REPO_NAME}"
  permission = "push"
  depends_on = ["github_repository.new_repo"]
}

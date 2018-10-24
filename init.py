from sys import platform
import os

terraUrl = "https://releases.hashicorp.com/terraform/0.11.10/terraform_0.11.10_darwin_amd64.zip"

if platform == "linux" or platform == "linux2":
    terraUrl = "https://releases.hashicorp.com/terraform/0.11.10/terraform_0.11.10_linux_amd64.zip"

os.system("rm -f *.zip")
os.system("rm -f *.tfstate*")
os.system("rm -f terraform*")
os.system("rm -Rf ./terraform")
os.system("curl %s > terraform.zip"%terraUrl)
os.system("unzip terraform.zip")
os.system("./terraform init")

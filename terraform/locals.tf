locals {
    user_data = <<EOF
#!/bin/bash
# yum update -y
# yum install -y python3.9
pip3 install mysql-connector-python --user
EOF
}
import os
import subprocess
from odoo_service import get_service
from odoo_conf import get_conf
 
linux_user = "odoo16"
linux_user_home = "/odoo"
postgres_user = "odoo16"
postgres_user_pass = "Parole.Ogre777"
odoo_version = "16.0"
odoo_path = "16"
venv_name = "odoo16-venv"
conf_name = "odoo16.conf"
service_name = "odoo16.service"

psql_commands = f"""
alter user {postgres_user} with encrypted password '{postgres_user_pass}';
\\q
"""

""" process = subprocess.Popen("sudo apt update && sudo apt upgrade", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
process.stdin.write(f'sudo useradd -m -d {linux_user_home} -U -r -s /usr/sbin/nologin {linux_user}')
process.stdin.write(f'sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev')
process.stdin.write(f'sudo apt-get install postgresql')
process.stdin.write(f'sudo su - postgres -c "createuser -s {postgres_user}"')
process.stdin.write("sudo -u postgres psql")
process.stdin.write(psql_commands)
process.stdin.write(f"sudo apt install wkhtmltopdf")
process.stdin.write(f"sudo su - {linux_user} -s /bin/bash")
process.stdin.write(f"git clone https://www.github.com/odoo/odoo --depth 1 --branch {odoo_version} {odoo_path}")
process.stdin.write(f"cd {odoo_path}")
process.stdin.write(f"python3 -m venv {venv_name}")
process.stdin.write(f"source {venv_name}/bin/activate")
process.stdin.write(f"pip3 install wheel")
process.stdin.write(f"mkdir custom-addons")
process.stdin.write(f"exit")
process = subprocess.Popen(f"sudo su - {linux_user} -s /bin/bash", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
process.stdin.write(f"git clone https://www.github.com/odoo/odoo --depth 1 --branch {odoo_version} {odoo_path}")
process.stdin.write(f"cd {odoo_path}")
process.stdin.write(f"python3 -m venv {venv_name}")
process.stdin.write(f"source {venv_name}/bin/activate")
process.stdin.write(f"pip3 install wheel")
process.stdin.write(f"mkdir custom-addons")
process.stdin.write(f"exit") """



sh_script = f"""
#!/bin/bash

sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev
sudo apt-get install postgresql
sudo su - postgres -c "createuser -s {postgres_user}"
sudo su - postgres -c "alter user {postgres_user} with encrypted password '{postgres_user_pass}'"
sudo apt install wkhtmltopdf

sudo su - odoo16 -s /bin/bash -c "git clone https://www.github.com/odoo/odoo --depth 1 --branch {odoo_version} {odoo_path}"
sudo su - odoo16 -s /bin/bash -c "python3 -m venv {linux_user_home}/{odoo_path}/{venv_name}"
source {linux_user_home}/{odoo_path}/{venv_name}/bin/activate
pip3 install wheel
pip3 install -r {linux_user_home}/{odoo_path}/requirements.txt

sudo systemctl daemon-reload
sudo systemctl start {service_name}
"""

with open(f"./install.sh","w") as f:
    f.write(sh_script)


with open(f"/etc/{conf_name}","w") as f:
    f.write(get_conf())

with open(f"/etc/systemd/system/{service_name}","w") as f:
    f.write(get_service())

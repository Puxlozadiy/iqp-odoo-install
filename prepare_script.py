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

sh_script = f"""
#!/bin/bash

sudo useradd -m -d {linux_user_home} -U -r -s /usr/sbin/nologin {linux_user}
sudo apt install -y build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev
sudo apt-get install postgresql -y
sudo su - postgres -c "createuser -s {postgres_user}"
sudo su - postgres -c "alter user {postgres_user} with encrypted password '{postgres_user_pass}'"
sudo apt install wkhtmltopdf -y

sudo su - odoo16 -s /bin/bash -c "git clone https://www.github.com/odoo/odoo --depth 1 --branch {odoo_version} {odoo_path}"
sudo su - odoo16 -s /bin/bash -c "python3 -m venv {linux_user_home}/{odoo_path}/{venv_name}"
sudo su - odoo16 -s /bin/bash -c "source {linux_user_home}/{odoo_path}/{venv_name}/bin/activate && pip3 install wheel && pip3 install -r {linux_user_home}/{odoo_path}/requirements.txt"
sudo su - odoo16 -s /bin/bash -c "mkdir {odoo_path}/custom-addons"

sudo systemctl daemon-reload
sudo systemctl start {service_name}
"""

with open(f"./install.sh","w") as f:
    f.write(sh_script)


with open(f"/etc/{conf_name}","w") as f:
    f.write(get_conf())

with open(f"/etc/systemd/system/{service_name}","w") as f:
    f.write(get_service(venv_path=f"{linux_user_home}/{odoo_path}/{venv_name}/"))

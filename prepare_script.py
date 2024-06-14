import os
import subprocess
from odoo_service import get_service
from odoo_conf import get_conf
 
linux_user = "odoo16"
linux_user_home = "/odoo/16"
postgres_user = "test"
postgres_user_pass = "Parole.Ogre777"
odoo_version = "16.0"
odoo_path = "test"
venv_name = "test-venv"
conf_name = "odoo-test.conf"
service_name = "odoo-test.service"
admin_password = "Parole.Ogre777"
logfile="odoo-test.log"
http_port="40169"
longpolling_port="40172"
description="Odoo test"

copy_default_addons = False

sh_script = f"""
#!/bin/bash

sudo useradd -m -d {linux_user_home} -U -r -s /usr/sbin/nologin {linux_user}
sudo apt install -y wkhtmltopdf build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev
sudo apt-get install -y postgresql unzip
sudo su - postgres -c "createuser -s {postgres_user}"
sudo -u postgres psql -c "alter user {postgres_user} with encrypted password '{postgres_user_pass}'"

sudo su - {linux_user} -s /bin/bash -c "git clone https://www.github.com/odoo/odoo --depth 1 --branch {odoo_version} {odoo_path}"
sudo su - {linux_user} -s /bin/bash -c "python3 -m venv {linux_user_home}/{odoo_path}/{venv_name}"
sudo su - {linux_user} -s /bin/bash -c "source {linux_user_home}/{odoo_path}/{venv_name}/bin/activate && pip3 install wheel && pip3 install -r {linux_user_home}/{odoo_path}/requirements.txt"
sudo su - {linux_user} -s /bin/bash -c "mkdir {odoo_path}/custom-addons"

sudo systemctl daemon-reload
sudo systemctl start {service_name}

unzip default-addons.zip
"""

with open(f"./install.sh","w") as f:
    f.write(sh_script)

if copy_default_addons:
    with open(f"./copy-addons.sh","w") as f:
        f.write(f"""sudo cp -r default-addons/. {linux_user_home}/{odoo_path}/custom-addons
    sudo chown {linux_user}:{linux_user} {linux_user_home}/{odoo_path}/custom-addons
    """)


with open(f"/etc/{conf_name}","w") as f:
    f.write(get_conf(
        admin_password=admin_password,
        postgres_user=postgres_user,
        postgres_user_pass=postgres_user_pass,
        install_path=f"{linux_user_home}/{odoo_path}",
        logfile=logfile,
        http_port=http_port,
        longpolling_port=longpolling_port,
    ))

with open(f"/etc/systemd/system/{service_name}","w") as f:
    f.write(get_service(
        linux_user=linux_user,
        install_path=f"{linux_user_home}/{odoo_path}",
        venv_name=venv_name,
        conf_name=conf_name,
        description=description
        ))

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

subprocess.Popen('sudo apt update && sudo apt upgrade', shell=True).wait()
subprocess.Popen(f'sudo useradd -m -d {linux_user_home} -U -r -s /usr/sbin/nologin {linux_user}', shell=True).wait()
subprocess.Popen(f'sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev', shell=True).wait()
subprocess.Popen(f'sudo apt-get install postgresql git', shell=True).wait()
subprocess.Popen(f'sudo su - postgres -c "createuser -s {postgres_user}"', shell=True).wait()
process = subprocess.Popen("sudo -u postgres psql", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
process.stdin.write(psql_commands)
subprocess.Popen(f"sudo apt install wkhtmltopdf", shell=True).wait()
subprocess.Popen(f"sudo su - {linux_user} -s /bin/bash", shell=True).wait()
subprocess.Popen(f"git clone https://www.github.com/odoo/odoo --depth 1 --branch {odoo_version} {odoo_path}", shell=True).wait()
subprocess.Popen(f"cd {odoo_path}", shell=True).wait()
subprocess.Popen(f"python3 -m venv {venv_name}", shell=True).wait()
subprocess.Popen(f"source {venv_name}/bin/activate", shell=True).wait()
subprocess.Popen(f"pip3 install wheel", shell=True).wait()
subprocess.Popen(f"pip3 install -r requirements.txt", shell=True).wait()
subprocess.Popen(f"mkdir custom-addons", shell=True).wait()
subprocess.Popen(f"exit", shell=True).wait()

with open(f"/etc/{conf_name}","w") as f:
    f.write(get_conf())

with open(f"/etc/systemd/system/{service_name}","w") as f:
    f.write(get_service())

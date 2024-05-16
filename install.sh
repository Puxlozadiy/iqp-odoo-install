sudo apt update && sudo apt upgrade
sudo useradd -m -d /odoo -U -r -s /usr/sbin/nologin odoo16
sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev
sudo apt-get install postgresql
sudo su - postgres -c "createuser -s odoo16"
sudo -u postgres psql
alter user odoo16 with encrypted password 'Parole.Ogre777';
exit
sudo apt install wkhtmltopdf
sudo apt-get install git
sudo su - odoo16 -s /bin/bash
git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 16
cd 16
python3 -m venv odoo16-venv
source odoo16-venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
mkdir custom-addons
exit

sudo systemctl daemon-reload
sudo systemctl start odoo16.service
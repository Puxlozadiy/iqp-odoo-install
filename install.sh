
#!/bin/bash

sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev
sudo apt-get install postgresql
sudo su - postgres -c "createuser -s odoo16"
sudo su - postgres -c "alter user odoo16 with encrypted password 'Parole.Ogre777'"
sudo apt install wkhtmltopdf

sudo su - odoo16 -s /bin/bash -c "git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 16"
sudo su - odoo16 -s /bin/bash -c "python3 -m venv /odoo/16/odoo16-venv"
sudo su - odoo16 -s /bin/bash -c "source /odoo/16/odoo16-venv/bin/activate && pip3 install wheel && pip3 install -r /odoo/16/requirements.txt"

sudo systemctl daemon-reload
sudo systemctl start odoo16.service

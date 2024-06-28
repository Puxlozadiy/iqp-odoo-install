
#!/bin/bash

sudo useradd -m -d /odoo/16 -U -r -s /usr/sbin/nologin odoo16
sudo apt install -y wkhtmltopdf build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev
sudo apt-get install -y postgresql unzip
sudo su - postgres -c "createuser -s odoo16_dm_live"
sudo -u postgres psql -c "alter user odoo16_dm_live with encrypted password 'Parole.Ogre777'"

sudo su - odoo16 -s /bin/bash -c "git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 dm-live"
sudo su - odoo16 -s /bin/bash -c "python3 -m venv /odoo/16/dm-live/dm-live-venv"
sudo su - odoo16 -s /bin/bash -c "source /odoo/16/dm-live/dm-live-venv/bin/activate && pip3 install wheel && pip3 install -r /odoo/16/dm-live/requirements.txt"
sudo su - odoo16 -s /bin/bash -c "mkdir dm-live/custom-addons"

sudo systemctl daemon-reload
sudo systemctl start odoo16-dm-live.service

unzip default-addons.zip

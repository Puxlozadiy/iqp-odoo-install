def get_service(
    admin_password="Parole.Ogre777",
    venv_path=""
    ):
    s = f"""
[Unit]
Description=Odoo
Requires=postgresql.service
After=network.target postgresql.service
[Service]
Type=simple
SyslogIdentifier=odoo
PermissionsStartOnly=true
User=odoo16
Group=odoo16
ExecStart={venv_path}bin/python3 /odoo/16/odoo-bin -c /etc/odoo16.conf
StandardOutput=journal+console
[Install]
WantedBy=multi-user.target
"""
    return s

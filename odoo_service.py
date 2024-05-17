def get_service(
    linux_user="odoo16",
    install_path="",
    venv_name="",
    conf_name=""
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
User={linux_user}
Group={linux_user}
ExecStart={install_path}{venv_name}/bin/python3 {install_path}/odoo-bin -c /etc/{conf_name}
StandardOutput=journal+console
[Install]
WantedBy=multi-user.target
"""
    return s

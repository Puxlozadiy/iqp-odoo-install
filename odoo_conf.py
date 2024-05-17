def get_conf(
    admin_password="Parole.Ogre777",
    postgres_user="odoo",
    postgres_user_pass="Parole.Ogre777",
    install_path="/odoo/16",
    logfile="odoo16.log",
    http_port="40069",
    longpolling_port="40072",
    proxy="True",
    ):
    s = f"""
[options]
admin_passwd = {admin_password}
db_user = {postgres_user}
db_password = {postgres_user_pass}
db_host = False
db_port = False
addons_path = {install_path}/addons,{install_path}/custom-addons
logfile = /var/log/odoo/{logfile}
http_port = {http_port}
longpolling_port = {longpolling_port}
proxy_mode = {proxy}
"""
    return s
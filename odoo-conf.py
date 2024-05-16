def get_conf(
    admin_password="Parole.Ogre777"
    ):
    s = f"""
[options]
; This is the password that allows database operations:
admin_passwd = {admin_password}
db_host = False
db_port = False
db_user = odoo16 
db_password = Parole.Ogre777
addons_path = /odoo/16/dm/addons,/odoo/16/dm/custom-addons
logfile = /var/log/odoo/odoo16-dm-test.log
http_port = 40069
longpolling_port = 40072
proxy_mode = True
"""
    return s




print(get_conf())
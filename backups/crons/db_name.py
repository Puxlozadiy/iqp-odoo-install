import sys
sys.path.append('../')

from iqp_backups import do_backup


odoo_port= "40069"
db_name= "db_name"
config = {
    "odoo_port": odoo_port,
    "db_name": db_name,
    "master_pwd": "Parole.Ogre777",
    "save_path": f"/store/{db_name}/",
    "url": f'http://localhost:{odoo_port}/web/database/backup',
    "max_backup_qty": 7
}


do_backup(config)
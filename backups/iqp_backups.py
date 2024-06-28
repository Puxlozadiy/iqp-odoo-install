import requests
import os
import os.path
from time import sleep
import shutil




def do_backup(config):
    disk_usage = shutil.disk_usage("/")
    # if free disk space is lower than 10 percent, throw error to telegram
    if((100 * float(disk_usage.free)/float(disk_usage.total))>10):

        absolute_path = os.path.abspath(os.path.dirname(__file__))
        response = requests.post(config['url'], data={"name": config['db_name'], "master_pwd": config['master_pwd']})
        if response.headers['Content-Type']=='application/octet-stream; charset=binary':
            file_name = response.headers['Content-Disposition'][response.headers['Content-Disposition'].rfind('\'\'')+2:]
            os.mkdir(f"{absolute_path}{config['save_path']}")
            with open(f"{absolute_path}{config['save_path']}{file_name}", mode="wb") as file:
                file.write(response.content)
                
        def get_mtime(elem):
            return os.path.getmtime(f"{absolute_path}{config['save_path']}{elem}")

        while True:
            try:
                backups = os.listdir(f"{absolute_path}{config['save_path']}")
                if len(backups)>config['max_backup_qty']:
                    backups.sort(key=get_mtime)
                    os.remove(f"{absolute_path}{config['save_path']}{backups[0]}")
                    sleep(1)
                else: break
            except: break
    else:
        None # TODO: Notice to telegram about low free disk space.

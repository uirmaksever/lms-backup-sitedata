import subprocess
import os
import datetime
CURRENT_TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M")

DB_HOST = 'stgmlmstxepmccinjvwi-database.mysql.database.azure.com' 
DB_USER = 'moodle_admin@stgmlmstxepmccinjvwi-database'
DB_USER_PASSWORD = 'rTyexrV6f9SgArPqCEmt7TmErHQ2ARB7'
DB_NAME = 'bitnami_moodle'
DBEXCLUDE = ["performance_schema", "information_schema"]
EXTRA_OPTS = "--single-transaction"
DB_BACKUP_FILENAME = "db_backup.sql"
# dumpcmd = "mysqldump -host " + DB_HOST + " -user " + DB_USER + " -password" + DB_USER_PASSWORD + " " + DB_NAME + " > " + "lms_db_backup_" + DB_NAME + ".sql" + " --single-transaction"
ignored_tables_strs = [f"--ignore-table {DB_NAME}.{table_name}" for table_name in DBEXCLUDE]
ignored_tables = " ".join(ignored_tables_strs)
# dump_command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_USER_PASSWORD} --single-transaction {ignored_tables} {DB_NAME}  > {DB_BACKUP_FILENAME}"
# mysqldump_call = subprocess.Popen(dumpcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
# os.system(dumpcmd)
db_filename =  f"{DB_NAME}_{CURRENT_TIMESTAMP}.sql"
db_filepath = f"/home/bitnami/backups/{CURRENT_TIMESTAMP}/{db_filename}"
dump_command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_USER_PASSWORD} --single-transaction {ignored_tables} {DB_NAME}  > {db_filepath}"
print(dump_command)
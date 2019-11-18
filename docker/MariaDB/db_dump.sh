#!/usr/bin/env bash

# sh docker/MariaDB/db_dump.sh lims_project_dev

BACKUP_DIR=${PROJECT_PATH}'/db/backup/'

[ -d ${BACKUP_DIR} ] || mkdir -p ${BACKUP_DIR}

DB_NAME=${1:-lims_project_dev}

BACKUP_SQL=${BACKUP_DIR}${DB_NAME}'_'`date '+%Y%m%d%H%M%S'`'.sql'
BACKUP_SQL_LATEST=${BACKUP_DIR}${DB_NAME}'_latest.sql'

docker exec mariadb \
    sh -c 'exec mysqldump --databases '${DB_NAME}' -uroot -p"$MYSQL_ROOT_PASSWORD" --default-character-set=utf8mb4' > ${BACKUP_SQL}

\cp ${BACKUP_SQL} ${BACKUP_SQL_LATEST}

echo ${BACKUP_SQL}

ls -alh ${BACKUP_DIR}

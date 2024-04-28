#!/bin/bash

# Check if migrations have been applied
if python manage.py showmigrations | grep "\[ \]" >/dev/null; then
    echo "Migrations have not been applied. Skipping import of dump file."
elif [[ "$*" == *"--build"* ]]; then
    echo "The --build flag is set. Importing dump file."
    # Import dump file into MySQL
    mysql -h"db" -u"root" -p"rootpassword" < /docker-entrypoint-initdb.d/dump_file.sql
else
    echo "The --build flag is not set. Skipping import of dump file."
fi

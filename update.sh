#!/bin/sh

/var/www/flatwhite/bin/python /opt/proj/flatwhite/manage.py migrate
/var/www/flatwhite/bin/python /opt/proj/flatwhite/manage.py collectstatic --noinput

sudo supervisorctl stop flatwhite:*
sudo supervisorctl start flatwhite:*

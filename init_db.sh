sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE box_django;" 
python manage.py syncdb

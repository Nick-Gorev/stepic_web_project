sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE box_django;" 
python manage.py syncdb

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart


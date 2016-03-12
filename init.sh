sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE box_django;" 
python manage.py syncdb

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

if [ -e /etc/nginx/sites-enabled/default ] ; then
    sudo rm /etc/nginx/sites-enabled/default
fi

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo rm /etc/nginx/sites-enabled/default

#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#gunicorn -b 0.0.0.0:8080 hello:app -D
#gunicorn -b 0.0.0.0:8000 ask.wsgi:application -D

#cd /home/box/web/ask
#gunicorn -b 0.0.0.0:8000 ask.wsgi:application -D

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

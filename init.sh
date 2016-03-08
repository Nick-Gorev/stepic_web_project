if [ -e /etc/nginx/sites-enabled/default ] ; then
    sudo rm /etc/nginx/sites-enabled/default
fi

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

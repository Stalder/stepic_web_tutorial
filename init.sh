sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

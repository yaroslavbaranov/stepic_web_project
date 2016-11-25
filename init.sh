#!/usr/bin/env bash

sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo rm -r /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/qa.py   /etc/gunicorn.d/qa.py
sudo /etc/init.d/gunicorn restart

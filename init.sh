#!/usr/bin/env bash

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

sudo rm /etc/nginx/sites-enabled/default
sudo ﻿ln -sf /home/box/web/etc/nginx.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo /etc/init.d/gunicorn restart
﻿

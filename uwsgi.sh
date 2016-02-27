uwsgi --http :9000 --chdir /root/someproject/ --wsgi-file someproject/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

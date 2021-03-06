CONFIG = {
  'mode': 'wsgi',
  'working_dir': '/home/box/web',
  'python': '/usr/bin/python',
  'args': (
    '--bind=0.0.0.0:8080',
    '--workers=4',
    '--timeout=15',
    '--log-level=debug',
    '--log-file=/home/box/gunicorn.log',
    'hello:app'
  )
}

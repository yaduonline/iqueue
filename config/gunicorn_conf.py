# import multiprocessing
from os import environ

# workers = multiprocessing.cpu_count() * 2 + 1
workers = environ.get('GUNICORN_NUM_WORKERS', 6)
max_requests = environ.get('GUNICORN_MAX_REQUESTS', 0)
worker_class = environ.get(
    'GUNICORN_WORKER_CLASS', 'gunicorn_worker.MozSvcGeventWorker'
)
loglevel = environ.get('GUNICORN_LOG_LEVEL', 'info')
preload = False
timeout = 25
accesslog = '-'
errorlog = '-'
access_log_format = ('%({X-Forwarded-For}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s'
                     ' %(b)s "%(f)s" "%(a)s" %(D)s %({X_Request_Id}i)s '
                     '%({OT-MobilePlatform}i)s %({Content-Type}i)s')


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

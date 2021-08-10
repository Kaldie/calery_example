from celery import Celery

app = Celery('project',
             broker='pyamqp://rabbitmq//',
             include=['project.worker.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
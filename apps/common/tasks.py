from celery import task

@task
def add(a, b):
    print(a + b)

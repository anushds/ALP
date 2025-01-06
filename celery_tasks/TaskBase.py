from celery import Task

class TaskBase(Task):
    abstract = True
    def __init__(self, *args, **kwargs):
        self._task = None
        super(TaskBase, self).__init__(*args, **kwargs)

    def run_task(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")

    def run(self, *args, **kwargs):
        self.run_task(*args, **kwargs)


    def on_success(self, retval, task_id, args, kwargs):
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass
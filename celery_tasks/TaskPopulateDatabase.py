from celery_tasks.TaskBase import TaskBase

class TaskPopulateDatabase(TaskBase):
    def run_task(self, *args, **kwargs):
        pass



obj = TaskPopulateDatabase()
obj.run_task('foo', 'bar')
print("success")


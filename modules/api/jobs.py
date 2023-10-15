import time

current_task = None
pending_tasks = {}
finished_tasks = []
recorded_results = []
recorded_results_limit = 2

def start_task(id_task):
    global current_task

    current_task = id_task
    pending_tasks.pop(id_task, None)

def finish_task(id_task):
    global current_task

    if current_task == id_task:
        current_task = None

    finished_tasks.append(id_task)
    if len(finished_tasks) > 16:
        finished_tasks.pop(0)

def cancel_task(id_task):
    global current_task

    if current_task == id_task:
        current_task = None

    pending_tasks.pop(id_task, None)

def record_results(id_task, res):
    recorded_results.append((id_task, res))
    if len(recorded_results) > recorded_results_limit:
        recorded_results.pop(0)


def add_task_to_queue(id_job):
    pending_tasks[id_job] = time.time()

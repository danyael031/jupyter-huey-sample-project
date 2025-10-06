from huey_queue.queue import huey
from typing import List, Tuple


# Normal tasks
@huey.task()
def add(a: int, b: int):
    return a + b


# Task running inside a task. This helps to group tasks and wait for all to
# complete.
# Other alternative for this aproach is to use the 
@huey.task()
def bulk_add(arguments: List[Tuple[int, int]]):

    # Enqueue all the tasks and wrap those in a ResultGroup
    # It is also possible to use the .map function
    enqueued_tasks = add.map(arguments)

    # Wait for al the tasks to complete
    results = enqueued_tasks.get(blocking=True)

    # Return the list of results
    return results

from gevent import monkey; monkey.patch_all()

from huey_queue.queue import huey  # Huey instance for our app.
from tasks.addition_tasks import * # Import all tasks, so they are discoverable.
from tasks.files_tasks import *  # Import all tasks, so they are discoverable.




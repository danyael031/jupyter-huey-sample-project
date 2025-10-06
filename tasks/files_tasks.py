from huey_queue.queue import huey
from huey.api import Task
from typing import List
import requests
import os


api_base_url = "https://jsonplaceholder.typicode.com"

@huey.task(context=True)
def fetch_post_and_save_file(post_id: int, task: Task):
    print(task.id)
    r = requests.get(f'{api_base_url}/posts/{post_id}')


    # By adding the task ID to the output path, we can keep the files
    # segmented, thus avoiding conflicts between tasks when accessing
    # files. I like to call this segmentation method "Task Workspace."
    file_path = f'./output/{task.id}/post_content_{post_id}.txt'

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(r.text)

    return file_path


# TO-DO: Bulk fetch and save file
#@huey.task(context=True)
#def bulk_fetch_post_and_save_file(posts_id: List[int] , task: Task):
#    pass

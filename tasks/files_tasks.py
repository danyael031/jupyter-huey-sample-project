from huey_queue.queue import huey
from huey.api import Task, ResultGroup
from typing import List
from utils.zip import zip_folders
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


@huey.task(context=True)
def bulk_fetch_post_and_save_file(posts_ids: List[int] , task: Task):

    enqueued_subtasks: List[Task] = [fetch_post_and_save_file(post_id) for post_id in posts_ids]

    # Create a resource group to wait for all the tasks to complete
    rg = ResultGroup(enqueued_subtasks)
    rg.get(blocking=True)


    folders_list = []
    for subtask in enqueued_subtasks:
        folders_list.append(f'./output/{subtask.id}/')

    bulk_output_path = f'./output/{task.id}/zipped_posts.zip'
    zip_folders(folders_list, bulk_output_path)

    return bulk_output_path

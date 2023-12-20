import json
import os.path
from .utils import serialize_date


def read_json_from_file_except(json_path):
    if os.path.exists(json_path):
        json_tasks = read_json_from_file(json_path)
        try:
            return json_tasks
        except NameError:
            print("Variable json_tasks WASN'T defined. Check path ", json_path)


def read_json_from_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path) as f:
            json_dict = json.load(f)
    return json_dict


def is_save_json(file_path, json_dict):
    if os.path.isfile(file_path):
        with open(file_path, mode='w') as f:
            f.write(json.dumps(json_dict, indent=2))
        print("File", file_path, "saved")
        return True
    return False


# def get_json_dict(source_file):
#     print("Source File: ", source_file)
#     with open(source_file, 'r') as f:
#         json_data = f.read()
#     return json.loads(json_data)

def update_tasks(path_tasks, task_in):
    if task_in['done'] < 0 or task_in['done'] > 100:
        raise Exception("Oops! You've got a wrong size for task['done'] in task ", task_in['num'])

    json_paths = read_json_from_file(path_tasks)

    for _task in json_paths['tasks']:
        if task_in['num'] == _task['num']:
            if task_in['done'] > _task['done']:
                _task['done'] = task_in['done']

                return is_save_json(path_tasks, json_paths)
            else:
                print("The task in tasks.json has a larger or equal 'done' value for num:", task_in['num'], ", done:",
                      str(_task['done']) + ">=" + str(task_in['done']))
                return False
    print("Could not find a task in tasks.json for num:", task_in['num'])
    return False


def save_history(p):
    subject = p.cmd2

    from datetime import datetime
    current_utc_datetime = datetime.utcnow()
    task = {'num': p.task_num3, 'done': p.done4, 'date_time': str(serialize_date(current_utc_datetime))}
    json_history = json.loads('{"history": []}')
    path_history = p.get_path_history(subject)
    if os.path.isfile(path_history):
        json_history = read_json_from_file(path_history)

    if update_tasks(p.get_path_tasks(subject), task):
        json_history['history'].append(task)
        return is_save_json(path_history, json_history)
    else:
        print("Could not update history because tasks are not updated")
    return False

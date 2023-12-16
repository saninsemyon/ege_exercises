import enum
import json
import sys
import os.path
import datetime
import time
from dateutil.tz import tzutc


class Params:
    source_tasks = "tasks.json"
    source_history = "history.json"

    def __init__(self):  # constructor
        # self.name = ''
        self.subject1 = "inf"
        self.cmd2 = "report"
        self.task_num3 = 0
        self.done4 = 0

    def get_data_path(self, file_name):
        path_history = 'data/' + self.subject1 + '/'
        if os.path.exists(path_history):
            data_path = path_history + file_name
            if not os.path.exists(data_path):
                print("Datafile not found: " + data_path)
            return data_path

        else:
            raise Exception("Directory not found: " + path_history)

    def get_path_tasks(self):
        return self.get_data_path(self.source_tasks)

    def get_path_history(self):
        return self.get_data_path(self.source_history)


class Command(enum.IntEnum):
    report = 0
    chart = 1
    save = 2
    delete = 3


def usage():
    print("Usage: ./run.py <subject> <cmd> <task_number> <done>")
    print("I.e.:  ./run.py math")
    print("       ./run.py inf add 2 80")
    print("       ./run.py plot math")


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def parse_args():
    p = Params()

    if len(sys.argv) >= 3:
        p.cmd2 = sys.argv[2]

    if len(sys.argv) >= 2:
        p.subject1 = sys.argv[1]
        if p.cmd2 == Command.save.name:
            p.task_num3 = int(sys.argv[3])
            p.done4 = int(sys.argv[4])
        return p
    else:
        usage()
        raise Exception("Could not parse parameters:", sys.argv)


UTC = tzutc()


def serialize_date(dt):
    """
    Serialize a date/time value into an ISO8601 text representation
    adjusted (if needed) to UTC timezone.
    For instance:
        serialize_date(datetime(2024, 4, 10, 22, 38, 20, 604391))
    '2024-04-10T22:38:20.604391Z'
    """
    # if dt.tzinfo:
    #    dt = dt.astimezone(UTC).replace(tzinfo=None)
    return dt.isoformat() + 'Z'


def is_save_json(file_path, json_dict):
    if os.path.isfile(file_path):
        with open(file_path, mode='w') as f:
            f.write(json.dumps(json_dict, indent=2))
        print("File", file_path, "saved")
        return True
    return False


def read_json(file_path):
    if os.path.isfile(file_path):
        with open(file_path) as f:
            json_dict = json.load(f)
    return json_dict


# def get_json_dict(source_file):
#     print("Source File: ", source_file)
#     with open(source_file, 'r') as f:
#         json_data = f.read()
#     return json.loads(json_data)

def update_tasks(path_tasks, task_in):
    if task_in['done'] < 0 or task_in['done'] > 100:
        raise Exception("Oops! You've got a wrong size for task['done'] in task ", task_in['num'])

    json_paths = read_json(path_tasks)

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


def save_history(params):
    from datetime import datetime
    current_utc_datetime = datetime.utcnow()
    task = {'num': params.task_num3, 'done': params.done4, 'date_time': str(serialize_date(current_utc_datetime))}
    json_history = json.loads('{"history": []}')
    path_history = params.get_path_history()
    if os.path.isfile(path_history):
        json_history = read_json(path_history)

    if update_tasks(params.get_path_tasks(), task):
        json_history['history'].append(task)
        return is_save_json(path_history, json_history)
    else:
        print("Could not update history because tasks are not updated")
    return False


class ReportData:
    today = time.strftime("%Y-%m-%d")
    current_date = datetime.date(int(time.strftime("%Y")),
                                 int(time.strftime("%m")),
                                 int(time.strftime("%d")))
    end_date = datetime.date(2024, 2, 28)
    weeks_left = (end_date - current_date).days // 7
    count = 0
    sum_done = 0
    total_score = 0
    todo_score = 0
    min_score = 1000
    max_score = 0
    next_task_todo = 0
    next_task_todo_done = 1000
    tasks_todo = 0
    tasks_done_100 = 0
    tasks_done_50 = 0
    tasks_done_50_80 = 0
    tasks_done_80 = 0
    min_score_task_num = 0
    max_score_task_num = 0


def set_report_data(_json_tasks, d):
    # Filter python objects with list comprehensions
    # done_dict = [x for x in input_dict if (x['done'] >= 90)]
    # todo_dict = [x for x in input_dict if not (x['done'] >= 90)]  # and x['num'] != 1
    # print("Tasks Done: ", len(done_dict))
    # print("TasksTodo: ", len(todo_dict), "\n")

    # Show json
    # print(json.dumps(todo_dict, indent=2))

    # global count, total_score, todo_score, min_score, max_score, min_score_task_num, \
    #    max_score_task_num, tasks_todo, tasks_done_50, tasks_done_50_80, tasks_done_80, tasks_done_100, sum_done, \
    #    next_task_todo, next_task_todo_done

    for task in _json_tasks['tasks']:
        d.count += 1

        _num = task['num']

        _done = task['done']
        if _done < 0 or _done > 100:
            raise Exception("Oops! You've got a wrong size for task['done'] in task " + str(_num))

        _level = task['level']
        if _level < 1 or _level > 3:
            raise Exception("Oops! You've got a wrong size for task['level'] in task " + str(_num))

        _goal_score = _level * 100
        d.total_score += _goal_score
        if d.min_score > _goal_score > 0:
            d.min_score = _goal_score
            d.min_score_task_num = _num

        if _goal_score > d.max_score:
            d.max_score = _goal_score
            d.max_score_task_num = _num

        if _done < 100:
            d.todo_score += _level * (100 - _done)
            d.tasks_todo += 1
            if _done < 50:
                d.tasks_done_50 += 1
            if 50 <= _done < 80:
                d.tasks_done_50_80 += 1
            if 80 <= _done < 100:
                d.tasks_done_80 += 1
            if _done < d.next_task_todo_done:
                d.next_task_todo = _num
                d.next_task_todo_done = _done
        elif _done == 100:
            d.tasks_done_100 += 1

        d.sum_done += _level * _done

    return d


def print_report(d):
    # global today, end_date, weeks_left, count, total_score, todo_score, min_score, max_score, min_score_task_num, \
    #    max_score_task_num, tasks_todo, tasks_done_50, tasks_done_80, tasks_done_100, sum_done, \
    #    next_task_todo, next_task_todo_done
    print("\n======== REPORT ", d.today, "========\n")
    print(f"{'Today:':>28} {str(d.today):>10}")
    print(f"{'End date:':>28} {str(d.end_date):>10}")
    print(f"{'Weeks left:':>28} {d.weeks_left:>4}")
    print(f"{'Tasks amount:':>28} {d.count:>4}")
    print(f"{'Total Possible Score:':>28} {d.total_score:>4}\n")

    print(f"{'Sum Done:':>28} {d.sum_done:>4} {str(d.sum_done * 100 // d.total_score) + '%':>18}")
    print(f"{'Left Todo Score Total:':>28} {d.todo_score:>4} {'Tasks todo:':>14} {d.tasks_todo}")
    print(f"{'Min Task Score:':>28} {d.min_score:>4} {'Task No.:':>14} {d.min_score_task_num}")
    print(f"{'Max task Score:':>28} {d.max_score:>4} {'Task No.:':>14} {d.max_score_task_num}")
    print(
        f"{'Next recommended task:':>28} {BColors.OKGREEN + str(d.next_task_todo) + BColors.ENDC:>4} {'Done:':>16} {str(d.next_task_todo_done)}%\n")

    print(f"{'Tasks done <50%:':>28} {BColors.WARNING + str(d.tasks_done_50) + BColors.ENDC:>4}")
    print(f"{'Tasks done 50-80%:':>28} {d.tasks_done_50_80:>4}")
    print(f"{'Tasks done >80%:':>28} {d.tasks_done_80:>4}")
    print(f"{'Tasks done 100%:':>28} {d.tasks_done_100:>4}\n")

    print(f"{'Average Task Score:':>28} {d.total_score // d.count:>4}")
    print(f"{'The goal for this week:':>28} {BColors.FAIL + str(d.todo_score // d.weeks_left) + BColors.ENDC:>4}")

    print('\n')


def draw_plot(params):
    path_history = params.get_path_history()

    group = ["A", "B", "C", "D", "E"]
    value = [14, 12, 8, 10, 16]

    from chart import chart_progress
    chart_progress(group, value)

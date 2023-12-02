#!/usr/bin/env python3

import datetime
import time
import json
import sys


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


def get_json_dict(sourceFile):
    print("Source File: ", sourceFile, "\n")

    with open(sourceFile, 'r') as data_file:
        json_data = data_file.read()

    return json.loads(json_data)


def generate_report(_json_dict):
    # Filter python objects with list comprehensions
    # done_dict = [x for x in input_dict if (x['done'] >= 90)]
    # todo_dict = [x for x in input_dict if not (x['done'] >= 90)]  # and x['num'] != 1
    # print("Tasks Done: ", len(done_dict))
    # print("TasksTodo: ", len(todo_dict), "\n")

    # Show json
    # print(json.dumps(todo_dict, indent=2))

    global count, total_score, todo_score, min_score, max_score, min_score_task_num, \
        max_score_task_num, tasks_todo, tasks_done_50, tasks_done_50_80, tasks_done_80, tasks_done_100, sum_done, \
        next_task_todo, next_task_todo_done

    for task in _json_dict:
        count += 1

        _num = task['num']

        _done = task['done']
        if _done < 0 or _done > 100:
            raise Exception("Oops! You've got a wrong size for task['done'] in task " + str(_num))

        _level = task['level']
        if _level < 1 or _level > 3:
            raise Exception("Oops! You've got a wrong size for task['level'] in task " + str(_num))

        _goal_score = _level * 100
        total_score += _goal_score
        if min_score > _goal_score > 0:
            min_score = _goal_score
            min_score_task_num = _num

        if _goal_score > max_score:
            max_score = _goal_score
            max_score_task_num = _num

        if _done < 100:
            todo_score += _level * (100 - _done)
            tasks_todo += 1
            if _done < 50:
                tasks_done_50 += 1
            if 50 <= _done < 80:
                tasks_done_50_80 += 1
            if 80 <= _done < 100:
                tasks_done_80 += 1
            if _done < next_task_todo_done:
                next_task_todo = _num
                next_task_todo_done = _done
        elif _done == 100:
            tasks_done_100 += 1

        sum_done += _level * _done


def print_report():
    global today, end_date, weeks_left, count, total_score, todo_score, min_score, max_score, min_score_task_num, \
        max_score_task_num, tasks_todo, tasks_done_50, tasks_done_80, tasks_done_100, sum_done, \
        next_task_todo, next_task_todo_done
    print("\n======== REPORT ", today, "========\n")
    print(f"{'Today:':>28} {str(today):>10}")
    print(f"{'End date:':>28} {str(end_date):>10}")
    print(f"{'Weeks left:':>28} {weeks_left:>4}")
    print(f"{'Tasks amount:':>28} {count:>4}")
    print(f"{'Total Possible Score:':>28} {total_score:>4}\n")

    print(f"{'Sum Done:':>28} {sum_done:>4} {str(sum_done * 100 // total_score) + '%':>18}")
    print(f"{'Left Todo Score Total:':>28} {todo_score:>4} {'Tasks todo:':>14} {tasks_todo}")
    print(f"{'Min Task Score:':>28} {min_score:>4} {'Task No.:':>14} {min_score_task_num}")
    print(f"{'Max task Score:':>28} {max_score:>4} {'Task No.:':>14} {max_score_task_num}")
    print(
        f"{'Next recommended task:':>28} {BColors.OKGREEN + str(next_task_todo) + BColors.ENDC:>4} {'Done:':>16} {str(next_task_todo_done)}%\n")

    print(f"{'Tasks done <50%:':>28} {BColors.WARNING + str(tasks_done_50) + BColors.ENDC:>4}")
    print(f"{'Tasks done 50-80%:':>28} {tasks_done_50_80:>4}")
    print(f"{'Tasks done >80%:':>28} {tasks_done_80:>4}")
    print(f"{'Tasks done 100%:':>28} {tasks_done_100:>4}\n")

    print(f"{'Average Task Score:':>28} {total_score // count:>4}")
    print(f"{'The goal for this week:':>28} {BColors.FAIL + str(todo_score // weeks_left) + BColors.ENDC:>4}")

    print('\n')

    # with open('output', 'w') as f:
    #    f.write(json.dumps(filtered_dict, indent=2))


try:
    sourceFile = sys.argv[1]
except IndexError:
    sourceFile = "tasks.json"

'''
try:
    action = sys.argv.__sizeof__()
except IndexError:
    action == "report"

if action == "print":
    print(action)
    # TODO:
elif action == "report":
    report()
else:
    report()
'''
json_dict = get_json_dict(sourceFile)
generate_report(json_dict)
print_report()

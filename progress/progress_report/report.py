import os.path
import datetime
import time
import dateparser

from .json_utils import read_json_from_file_except, read_json_from_file
from .utils import BColors


class Report:
    today = time.strftime("%Y-%m-%d")
    current_date = datetime.date(int(time.strftime("%Y")),
                                 int(time.strftime("%m")),
                                 int(time.strftime("%d")))

    end_date = datetime.date(2024, 2, 28)
    weeks_left = (end_date - current_date).days // 7

    def __init__(self, ):  # constructor
        self.count = 0
        self.sum_done = 0
        self.total_score = 0
        self.todo_score = 0
        self.min_score = 1000
        self.max_score = 0
        self.next_task_todo = 0
        self.next_task_todo_done = 1000
        self.tasks_todo = 0
        self.tasks_done_100 = 0
        self.tasks_done_50 = 0
        self.tasks_done_50_80 = 0
        self.tasks_done_80 = 0
        self.min_score_task_num = 0
        self.max_score_task_num = 0

    def get_report_data(self, _json_tasks):
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
            self.count += 1

            _num = task['num']

            _done = task['done']
            if _done < 0 or _done > 100:
                raise Exception("Oops! You've got a wrong size for task['done'] in task " + str(_num))

            _level = task['level']
            if _level < 1 or _level > 3:
                raise Exception("Oops! You've got a wrong size for task['level'] in task " + str(_num))

            _goal_score = _level * 100
            self.total_score += _goal_score
            if self.min_score > _goal_score > 0:
                self.min_score = _goal_score
                self.min_score_task_num = _num

            if _goal_score > self.max_score:
                self.max_score = _goal_score
                self.max_score_task_num = _num

            if _done < 100:
                self.todo_score += _level * (100 - _done)
                self.tasks_todo += 1
                if _done < 50:
                    self.tasks_done_50 += 1
                if 50 <= _done < 80:
                    self.tasks_done_50_80 += 1
                if 80 <= _done < 100:
                    self.tasks_done_80 += 1
                if _done < self.next_task_todo_done:
                    self.next_task_todo = _num
                    self.next_task_todo_done = _done
            elif _done == 100:
                self.tasks_done_100 += 1

            self.sum_done += _level * _done

    def print_report(self):
        # global today, end_date, weeks_left, count, total_score, todo_score, min_score, max_score, min_score_task_num, \
        #    max_score_task_num, tasks_todo, tasks_done_50, tasks_done_80, tasks_done_100, sum_done, \
        #    next_task_todo, next_task_todo_done
        print("\n======== REPORT ", self.today, "========\n")
        print(f"{'Today:':>28} {str(self.today):>10}")
        print(f"{'End date:':>28} {str(self.end_date):>10}")
        print(f"{'Weeks left:':>28} {self.weeks_left:>4}")
        print(f"{'Tasks amount:':>28} {self.count:>4}")
        print(f"{'Total Possible Score:':>28} {self.total_score:>4}\n")

        print(f"{'Sum Done:':>28} {self.sum_done:>4} {str(self.sum_done * 100 // self.total_score) + '%':>18}")
        print(f"{'Left Todo Score Total:':>28} {self.todo_score:>4} {'Tasks todo:':>14} {self.tasks_todo}")
        print(f"{'Min Task Score:':>28} {self.min_score:>4} {'Task No.:':>14} {self.min_score_task_num}")
        print(f"{'Max task Score:':>28} {self.max_score:>4} {'Task No.:':>14} {self.max_score_task_num}")
        print(
            f"{'Next recommended task:':>28} {BColors.OKGREEN + str(self.next_task_todo) + BColors.ENDC:>4} {'Done:':>16} {str(self.next_task_todo_done)}%\n")

        print(f"{'Tasks done <50%:':>28} {BColors.WARNING + str(self.tasks_done_50) + BColors.ENDC:>4}")
        print(f"{'Tasks done 50-80%:':>28} {self.tasks_done_50_80:>4}")
        print(f"{'Tasks done >80%:':>28} {self.tasks_done_80:>4}")
        print(f"{'Tasks done 100%:':>28} {self.tasks_done_100:>4}\n")

        print(f"{'Average Task Score:':>28} {self.total_score // self.count:>4}")
        print(
            f"{'The goal for this week:':>28} {BColors.FAIL + str(self.todo_score // self.weeks_left) + BColors.ENDC:>4}")

        print('\n')


def deserialize_datetime_00(_dt):
    if _dt.endswith('Z'):
        _dt = _dt[:-1] + '+00:00'
    return datetime.datetime.fromisoformat(_dt)


def _parse_history(_json_history, task_nums):
    dict_progress = {}
    dict_prev_value = {}

    for it in _json_history['history']:
        _num = it['num']
        _done = it['done']
        _dt_utc = it['date_time']
        _dt = deserialize_datetime_00(_dt_utc)
        _year = _dt.year

        if _num in task_nums:
            wk = _dt.isocalendar()[1]
            week = str(_year) + '.' + str(wk)

            if week in dict_prev_value:
                _done_diff = _done - dict_prev_value[week]
            else:
                _done_diff = _done

            dict_progress[week] = _done_diff
            dict_prev_value[week] = _done
        else:
            print("Strange task_num is found in history", _num)
    return dict_progress.keys(), dict_progress.values()


def set_history_dict(subj, _json_history, task_nums):
    # dict_progress = {}
    dict_prev_value = {}
    subjects = []
    tasks = []
    dates = []
    progress = []

    for it in _json_history['history']:
        _num = it['num']
        _done = it['done']
        _dt_utc = it['date_time']
        # _dt = deserialize_datetime_00(_dt_utc)
        _dt = dateparser.parse(_dt_utc).date()

        # _year = _dt.year

        if _num in task_nums:
            # if _dt in dict_prev_value:
            #    _done_diff = _done - dict_prev_value[_dt]
            # else:
            _done_diff = _done

            subjects.append(subj)
            tasks.append(_num)
            dates.append(_dt)
            progress.append(_done_diff)
            # dict_progress[_dt] = _done_diff
            dict_prev_value[_dt] = _done
        else:
            print("Strange task_num is found in history", _num)

    # history_dict = {'dates': list(dict_progress.keys()), 'progress': list(dict_progress.values())}

    return subjects, tasks, dates, progress


def prepare_plot_hist_dict(p):
    hist_dict = {}

    for subj in p.subj_list:
        task_nums = []
        path_tasks = p.get_path_tasks(subj)
        json_tasks = read_json_from_file_except(path_tasks)
        for it in json_tasks['tasks']:
            task_nums.append(it['num'])

        path_hist = p.get_path_history(subj)
        if os.path.exists(path_hist):
            json_history = read_json_from_file(path_hist)
            try:
                _subjects, _tasks, _dates, _progress = set_history_dict(subj, json_history, task_nums)
            except NameError:
                print("Variable json_tasks WASN'T defined!")

        if "date" in hist_dict:
            hist_dict["subjects"].extend(_subjects)
            hist_dict["tasks"].extend(_tasks)
            hist_dict["date"].extend(_dates)
            hist_dict["progress"].extend(_progress)
        else:
            hist_dict["subjects"] = _subjects
            hist_dict["tasks"] = _tasks
            hist_dict["date"] = _dates
            hist_dict["progress"] = _progress

    return hist_dict


def prepare_plot_fact_dict(p):
    fact_dict = {}
    subj = 'inf'
    path_tasks = p.get_path_tasks(subj)
    json_tasks = read_json_from_file_except(path_tasks)
    tasks = []
    levels = []
    progress = []
    dates = []

    for it in json_tasks['tasks']:
        tasks.append(it['num'])
        levels.append(it['level'])
        progress.append(it['done'])

        if 'date_time' in it:
            _dt_utc = it['date_time']
            _dt = dateparser.parse(_dt_utc).date()
            dates.append(_dt)
        else: dates.append("")

    fact_dict["tasks"] = tasks
    fact_dict["levels"] = levels
    fact_dict["progress"] = progress
    fact_dict["dates"] = dates

    return fact_dict


def run_report(params):
    report = Report()
    json_tasks = read_json_from_file_except(params.path_tasks)
    report.get_report_data(json_tasks)
    return report


def run_reports_all(p, subj_list):
    dict_reports = {}
    for subj in subj_list:
        path_tasks = p.get_path_tasks(subj)
        report = run_report(path_tasks)
        dict_reports[subj] = report
    return dict_reports

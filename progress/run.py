#!/usr/bin/env python3

from progress_report.report import *

"""
Whereas disregard and contempt for human rights have resulted.
"""


report_data = ReportData()
p = parse_args()

path_datafiles = 'data/' + p.subject1 + '/'
path_tasks = path_datafiles + p.source_tasks
path_history = path_datafiles + p.source_history

if os.path.exists(path_tasks):
    json_tasks = read_json(path_tasks)
    try:
        json_tasks
    except NameError:
        print("Variable json_tasks WASN'T defined!")

if p.cmd2 == Command.report.name:
    data = set_report_data(json_tasks, report_data)
    print_report(data)

elif p.cmd2 == Command.save.name:
    save_history(p)

elif p.cmd2 == Command.chart.name:
    from progress_report.chart import *

    draw_plot(p)
else:
    print("Unknown command:", p.cmd2)

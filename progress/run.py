#!/usr/bin/env python3
import sys

from progress_report.json_utils import save_history
from progress_report.utils import Command, usage, Chart
from progress_report.params import Params
from progress_report.plot import show_chart_activities, gapminder_progress
from progress_report.report import *

p = Params()

if p.parse_args():
    if p.cmd1 == "help":
        usage(p)
    elif p.cmd1 == Command.report.name:
        if p.exists_subject(p.cmd2):
            report = run_report(p)
            report.print_report()
    elif p.cmd1 == Command.save.name:
        save_history(p)
    elif p.cmd1 == Command.chart.name:
        if p.cmd2 == Chart.activities.name:
            hist_dict = prepare_plot_hist_dict(p)
            show_chart_activities(hist_dict)
        elif p.cmd2 == Chart.gapminder.name:
            gapminder_progress()
        elif p.cmd2 == Chart.progress.name:
            # chart_progress(weeks, progress)
            # TODO
            print("//TODO show_chart")
    else:
        print("Unknown command:", p.cmd1)
        usage(p)
else:
    print("Could not parse parameters:", sys.argv)
    usage(p)

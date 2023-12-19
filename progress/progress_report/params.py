import sys
import os.path
from .utils import Command


class Params:
    source_tasks = "tasks.json"
    source_history = "history.json"

    def __init__(self):  # constructor
        self.base_data_path = "data/"
        self.cmd1 = None
        self.cmd2 = None
        self.task_num3 = 0
        self.done4 = 0
        self.path_datafiles = None
        self.path_tasks = None
        self.path_history = None
        self.subj_list = self.getSubjectList()

    def parse_args(self):
        result = True
        if len(sys.argv) >= 3:
            self.cmd2 = sys.argv[2]
            self.path_datafiles = 'data/' + self.cmd2 + '/'
            self.path_tasks = self.path_datafiles + Params.source_tasks
            self.path_history = self.path_datafiles + Params.source_history

        if len(sys.argv) >= 2:
            self.cmd1 = sys.argv[1]
            if self.cmd1 == Command.save.value:
                self.task_num3 = int(sys.argv[3])
                self.done4 = int(sys.argv[4])
        else:
            result = False
        return result

    def get_data_path(self, subject, file_name):
        dir_path = self.base_data_path + subject + '/'
        if os.path.exists(dir_path):
            data_path = dir_path + file_name
            if not os.path.exists(data_path):
                print("Datafile not found: " + data_path)
            return data_path
        else:
            raise Exception("Directory not found: " + dir_path)

    def get_path_tasks(self, subject):
        return self.get_data_path(subject, self.source_tasks)

    def get_path_history(self, subject):
        return self.get_data_path(subject, self.source_history)

    def getSubjectList(self):
        subject_list = []
        """Yield directory names not starting with '.' under given path."""
        for entry in os.scandir(self.base_data_path):
            if not entry.name.startswith('.') and entry.is_dir():
                subject_list.append(entry.name)
        return subject_list

    def exists_subject(self, subj):
        if subj in self.subj_list:
            return True
        else:
            raise Exception("Unknown subject:", subj)

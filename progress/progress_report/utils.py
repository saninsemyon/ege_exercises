from enum import auto, Flag, Enum
from dateutil.tz import tzutc


class Command(Enum):
    report = 'report'
    chart = 'chart'
    save = 'save'
    help = 'help'


class Chart(Enum):
    activities = 'activities'
    progress = 'progress'
    gapminder = 'gapminder'


def names_enum(enum):
    return [it.name for it in enum]


def values_enum(enum):
    return [it.value for it in enum]


def usage(p):
    print("Usage1: ./run.py save <subject> <task_number> <%done>")
    print("Usage2: ./run.py report <subject>")
    print("Usage3: ./run.py chart <type>\n")

    print("I.e.:  ./run.py report math")
    print("       ./run.py save inf 2 80")
    print("       ./run.py chart activities\n")
    print("Subjects:", p.subj_list, "\n")
    print("Chart types:", names_enum(Chart), "\n")


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


UTC = tzutc()


def serialize_date(_dt):
    """
    Serialize a date/time value into an ISO8601 text representation
    adjusted (if needed) to UTC timezone.
    For instance:
        serialize_date(datetime(2024, 4, 10, 22, 38, 20, 604391))
    '2024-04-10T22:38:20.604391Z'
    """
    # if dt.tzinfo:
    #    dt = dt.astimezone(UTC).replace(tzinfo=None)
    return _dt.isoformat() + 'Z'

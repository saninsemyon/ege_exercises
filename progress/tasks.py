#!/usr/bin/env python3

import datetime
import time
import json
import sys

try:
    sourceFile = sys.argv[1]
except IndexError:
    sourceFile = "tasks.json"

print("Source File: ", sourceFile, "\n")

today = time.strftime("%Y-%m-%d")

currentDate = datetime.date(int(time.strftime("%Y")),
                            int(time.strftime("%m")),
                            int(time.strftime("%d")))

endDate = datetime.date(2024, 2, 28)

weeksLeft = (endDate - currentDate).days // 7

with open(sourceFile, 'r') as data_file:
    json_data = data_file.read()

input_dict = json.loads(json_data)

# Filter python objects with list comprehensions
# done_dict = [x for x in input_dict if (x['done'] >= 90)]
# todo_dict = [x for x in input_dict if not (x['done'] >= 90)]  # and x['num'] != 1
# print("Tasks Done: ", len(done_dict))
# print("Tasks Todo: ", len(todo_dict), "\n")

# Show json
# print(json.dumps(todo_dict, indent=2))


i = 0
sumDone = 0
totalScore = 0
todoScore = 0
minScore = 1000
maxScore = 0
nextTaskTodo = 0
tasksTodo = 0
tasksDone = 0
minScoreTaskNum = 0
maxScoreTaskNum = 0

for task in input_dict:
    i += 1

    _num = task['num']

    _done = task['done']
    if (_done < 0 or _done > 100):
        raise Exception("Oops! You've got a wrong size for task['done'] in task " + str(_num))

    _level = task['level']
    if (_level < 1 or _level > 3):
        raise Exception("Oops! You've got a wrong size for task['level'] in task " + str(_num))

    _goalScore = _level * 100
    totalScore += _goalScore
    if (_goalScore < minScore and _goalScore > 0):
        minScore = _goalScore
        minScoreTaskNum = _num

    if (_goalScore > maxScore):
        maxScore = _goalScore
        maxScoreTaskNum = _num

    if _done < 100:
        todoScore += _level * (100 - _done)
        tasksTodo += 1
    elif _done == 100:
        tasksDone += 1

    sumDone += _level * _done

    if (nextTaskTodo == 0 and _done < 90):
        nextTaskTodo = _num
        nextTaskTodoDone = _done

print("\n======== REPORT ", today, "========\n")

#print("End date:", endDate)
# print ("Tasks amount:", i)
# print ("Total Possible Score:", totalScore)
# print ("Tasks done 100%:", tasksDone)
# print ("Sum Done: ", sumDone)
# print ("Left Todo Score Total: ", todoScore, "  Tasks todo: ", tasksTodo)
# print ("Min Task Score: ", minScore, "\t  Task No.: ", minScoreTaskNum)
# print ("Max Task Score: ", maxScore, "\t  Task No.: ", maxScoreTaskNum)
# print ("Average Task Score: ", totalScore // i)
# print ("The goal for this week: ", todoScore // weeksLeft)
# print ("Next recommended task No.: ", nextTaskTodo, ", ", nextTaskTodoDone, "% done\n")
print('{0:>30} {1:12}'.format("Today:", str(today)))
print('{0:>30} {1:12}'.format("End date:", str(endDate)))
print('{0:>30} {1:4}                '.format("Weeks left:", weeksLeft))
print('{0:>30} {1:4}                '.format("Tasks amount:", i))
print('{0:>30} {1:4}                '.format("Total Possible Score:", totalScore))
print('{0:>30} {1:4}                '.format("Tasks done 100%:", tasksDone))
print('{0:>30} {1:4}    {2:19}{3:4} '.format("Sum Done: ", sumDone, sumDone * 100 // totalScore, "%"))
print('{0:>30} {1:4}    {2:14} {3:4}'.format("Left Todo Score Total:", todoScore, "Tasks todo:", tasksTodo))
print('{0:>30} {1:4}    {2:14} {3:4}'.format("Min Task Score:", minScore, "Task No.:", minScoreTaskNum))
print('{0:>30} {1:4}    {2:14} {3:4}'.format("Max task Score:", maxScore, "Task No.:", maxScoreTaskNum))
print('{0:>30} {1:4}                '.format("Average Task Score:", totalScore // i))
print('{0:>30} {1:4}                '.format("The goal for this week:", todoScore // weeksLeft))
print('{0:>30} {1:4}    {2:14}{3:4} '.format("Next recommended task No.:", nextTaskTodo, nextTaskTodoDone,
                                             "% done"))
print('\n')

# with open('output', 'w') as f:
#    f.write(json.dumps(filtered_dict, indent=2))

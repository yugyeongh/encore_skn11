# 1
import q_modules.team_module as team

print(f'안녕하세요, {team.company}입니다.')
print(team.introduce_manager())
print(team.introduce_developer())

print('----------------------------')

# 2
import q_modules.attendance_module as attendance

print(attendance.record_attendance('토끼','9:00'))
print(attendance.record_leave('토끼','18:00'))

print('----------------------------')

# 3
import q_modules.task_module as task

print(task.start_task('코드 리뷰'))
print(task.complete_task('코드 리뷰'))

print('----------------------------')

#4
import math

arr = [10,12,8,15,9]
avg = sum(arr)/len(arr)
print('평균 업무량:', math.ceil(avg))

count = 0
for a in arr:
    if a > avg:
        count += 1

print('평균 업무량보다 많이 처리한 날:', count)

# 5
from datetime import datetime as dt

date = dt.now().strftime('%Y-%M-%D %H:%M:%S')

print(f'[{date}] 토끼님이 작업 \'코드 리뷰\'을(를) 완료했습니다.')
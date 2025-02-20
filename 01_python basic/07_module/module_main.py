# 1. import 구문 사용

# import our_class as oc

# print(oc.teacher_name, oc.student_count)
# oc.study()
# oc.lecture()

# menus = ['떡볶이','돈까스','제육볶음','마라샹궈','만두두']
# print(oc.go_lunch(menus))

#########################

# 2. from-import 구문 사용

# from our_class import teacher_name, student_count, study, lecture, go_lunch

# print(teacher_name, student_count)
# study()
# lecture()

# menus = ['떡볶이','돈까스','제육볶음','마라샹궈','만두두']
# print(go_lunch(menus))

# 3. 패키지 내의 모듈 import
# from our_class import teacher_name, student_count, study, lecture, go_lunch
import our_class_dir.official.official_module as m
from our_class_dir.unofficial.unofficial_module import study, go_lunch

print(m.teacher_name, m.student_count)
study()
m.lecture()

menus = ['떡볶이','돈까스','제육볶음','마라샹궈','만두두']
print(go_lunch(menus))
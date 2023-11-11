import csv
import numpy as np


def get_report(report_file):  # 성적표(output.csv) list로 가져오기
    with open(report_file, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        data = [[c.replace('\ufeff', '') for c in row] for row in reader]
    return data


def course_csv_to_np(file_name):  # 강의 목록을 ndarray로 가져오기
    with open(file_name, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        data = [[c.replace('\ufeff', '') for c in row] for row in reader]
    return np.array(data)


def create_list_of_courses(course_np, report):
    list_of_courses = []

    for row in report:
        if row[0] in course_np:
            key = np.where(course_np == row[0])[0][0]
            if course_np[key][1] != row[1]:
                print('학정번호의 과목 [' + course_np[key][1] + ']와/과 성적표의 과목 [' + row[1] + ']이 다릅니다.')
            list_of_courses.append(row)

    return list_of_courses


test_data = get_report('output.csv')

# Fail 성적 모두 제외
for row in test_data:
    if row[4] in ['U', 'W', 'WE', 'F', 'NP']:
        test_data.remove(row)

# 응용정보공학 강의 목록을 ndarray로 가져오기
aie_course_np = course_csv_to_np('aie_course.csv')

# 성적표 주인이 들은 Fail하지 않은 강의 중 응용정보공학전공 강의 추출하기
print(create_list_of_courses(aie_course_np, test_data))
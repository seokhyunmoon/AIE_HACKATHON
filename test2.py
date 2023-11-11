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

def divide_major_to_three(course_np, report):
    major_b = []
    major_e = []
    major_r = []

    for row in report:
        if row[0] in course_np:
            key = np.where(course_np == row[0])[0][0]
            if (course_np[key][2] == '전기'):
                major_b.append(row)
            elif (course_np[key][2] == '전선'):
                major_e.append(row)
            elif (course_np[key][2] == '전필'):
                major_r.append(row)

    return major_b, major_r, major_e

def create_list_of_3_4000(course_np, report):
    list_of_courses = []

    for row in report:
        if row[0][3] == '3' or row[0][3] == '4':
            list_of_courses.append(row)

    return list_of_courses


test_data = get_report('output.csv')

# Fail 성적 모두 제외
for row in test_data:
    print("row : ", row)
    if row[4] in ['U', 'W', 'WE', 'F', 'NP']:
        test_data.remove(row)

# 각 전공 강의 목록을 ndarray로 가져오기
aie_course_np = course_csv_to_np('aie_course.csv')
bio_course_np = course_csv_to_np('bio_course.csv')
media_course_np = course_csv_to_np('media_course.csv')
intcommerce_course_np = course_csv_to_np('intcommerce_course.csv')
korean_course_np = course_csv_to_np('korean_course.csv') #한국어 나중에 추가

# GLC 교양 강의 목록을 ndarray로 가져오기

# GLC 영어 강의 목록을 ndarray로 가져오기
english_course_np = course_csv_to_np('english_course.csv')

# 기독교의 이해 강의 목록을 ndarray로 가져오기
christianity_course_np = course_csv_to_np('christianity_course.csv')

# 채플 강의 목록을 ndarray로 가져오기
chapel_course_np = course_csv_to_np('chapel.csv')

# RC101 강의 목록을 ndarray로 가져오기
rc101_course_np = course_csv_to_np('rc101.csv')

# 성적표 주인이 들은 Fail하지 않은 강의 중 응용정보공학전공 강의 추출하기
print(create_list_of_courses(aie_course_np, test_data))

#성적표 주인이 들은 RC101 강의 가져오기
print(create_list_of_courses(rc101_course_np, test_data))
print(create_list_of_courses(chapel_course_np, test_data))
print(create_list_of_courses(christianity_course_np, test_data))
print(create_list_of_courses(english_course_np, test_data))

#전기, 전필, 전선 리스트 생성
major_basic, major_required, major_elective = divide_major_to_three(aie_course_np, test_data)
print(major_basic)
print(major_required)
print(major_elective)

#3-4000 단위 리스트 생성
print(create_list_of_3_4000(aie_course_np, test_data))


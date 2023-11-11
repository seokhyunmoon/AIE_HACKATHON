import csv
import numpy as np


def get_report(report_file):
    list = []
    with open(report_file, newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            list.append(row)
    return list

def course_csv_to_np(file_name):
    with open(file_name, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        data = [[c.replace('\ufeff', '') for c in row] for row in reader]
    return data


def create_list_of_courses(course_np, report):
    list_of_courses = []

    for row in report:
        if row[4] in ['U', 'W', 'F', 'NP']:
            continue
        elif row[0] in course_np:
            key = np.where(course_np == row[0])[0][0]
            if course_np[key][1] != row[1]:
                print('학정번호의 과목 [' + course_np[key][1] + ']와/과 성적표의 과목 [' + row[1] + ']이 다릅니다.')
            list_of_courses.append(row)
        else:
            print("YOU FAILED")

    return list_of_courses


def calc_other_requirements():

    return

#강의
bio_course_np = course_csv_to_np('bio_course.csv')

# 테스트 데이터
'''
test_data = [['GBL2001', '유기화학입문', '전기', 3, 'D'], ['GBL2004', '바이오생활생물1', '전기', 3, 'A+'],
             ['GBL2005', '바이오생활화학1', '전기', 3, 'D'], ['GBL2006', '바이오생활생물2', '전기', 3, 'P'],
             ['GBL2007', '가짜 과목', '전기', 3, 'A+'], ['GBL2008', '응용생화학', '전기', 3, 'S'],
             ['GBL2002', '기능성식품학개론', '전필', 3, 'C'], ['GBL2003', '바이오화장품학개론', '전필', 3, 'NP'],
             ['GBL3001', '바이오기능성소재학', '전필', 3, 'A+'], ['GBL3201', '바이오생활기초실험', '전필', 3, 'NP'],
             ['GBL1001', '바이오생활공학입문', '전선', 3, 'P'], ['GBL1002', '바이오생활융합과학개론', '전선', 3, 'NP'],
             ['GBL3002', '핵심미생물학', '전선', 3, 'P'], ['GBL3003', '피부생명과학', '전선', 3, 'B-'],
             ['GBL3004', '바이오통계학', '전선', 3, 'NP'], ['GBL3005', '미래바이오헬스케어', '전선', 3, 'F'],
             ['GBL3203', '식품화학개론', '전선', 3, 'W'], ['GBL4001', '바이오생활창의설계1', '전선', 3, 'U'],
             ['GBL4002', '바이오생활창의설계2', '전선', 3, 'S'], ['GBL4003', '기기분석학', '전선', 3, 'P'],
             ['GBL4004', '화장품제형공학', '전선', 3, 'A+'], ['GBL4005', '바이오안전및독성학', '전선', 3, 'B-'],
             ['GBL4006', '첨단발효공학', '전선', 3, 'P'], ['GBL4007', '바이오헬스케어기술과산업', '전선', 3, 'W'],
             ['GBL4008', '푸드테크과학기술특론', '전선', 3, 'U'], ['GBL4201', '바이오생활전공실험1', '전선', 3, 'NP']]
'''
test_data = get_report('output.csv')
print(test_data)
#print(create_list_of_courses(bio_course_np, test_data))
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
    if row[4] in ['U', 'W', 'WE', 'F', 'NP']:
        test_data.remove(row)

# 각 전공 강의 목록을 ndarray로 가져오기
aie_course_np = course_csv_to_np('aie_course.csv')
bio_course_np = course_csv_to_np('bio_course.csv')
media_course_np = course_csv_to_np('media_course.csv')
intcommerce_course_np = course_csv_to_np('intcommerce_course.csv')
korean_course_np = course_csv_to_np('korean_course.csv')

# GLC 교양 강의 목록을 ndarray로 가져오기
glcsubject_course_np = course_csv_to_np('glcsubject_course.csv')

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
print()

#성적표 주인이 들은 RC101 강의 가져오기
print(create_list_of_courses(rc101_course_np, test_data))
print(create_list_of_courses(chapel_course_np, test_data))
print(create_list_of_courses(christianity_course_np, test_data))
print(create_list_of_courses(english_course_np, test_data))
print(create_list_of_courses(glcsubject_course_np, test_data))

rc101 = create_list_of_courses(rc101_course_np, test_data)
chapel = create_list_of_courses(chapel_course_np, test_data)
christianity = create_list_of_courses(christianity_course_np, test_data)
english = create_list_of_courses(english_course_np, test_data)
glcsubject = create_list_of_courses(glcsubject_course_np, test_data)

#3-4000 단위 리스트 생성
print(create_list_of_3_4000(aie_course_np, test_data))


def sum_of_credits(list):
    sum = 0
    for row in list:
        sum += float(row[3])
    return sum

print('-------------------------------------------------------------')
# 전공 외 조건 이수 검사
def basic_requirement_fulfilled():
    # 채플
    chapel_sum = sum_of_credits(chapel)
    if chapel_sum < 2:
        print('채플 ' + str(2 - chapel_sum) + '학점 이수 필요')
    else:
        print('채플 달성 완료!')

    # 기독교의 이해
    christianity_sum = sum_of_credits(christianity)
    if christianity_sum < 3:
        print('기독교의 이해 ' + str(3 - christianity_sum) + '학점 이수 필요')
    else:
        print('기독교의 이해 달성 완료!')

    # GLC 영어
    if len(english) < 2:
        print('GLC 영어 ' + str((2 - len(english))*3) + '학점 이수 필요')
    else:
        print('GLC 영어 달성 완료!')

    # GLC 교양
    glcsubject_sum = sum_of_credits(glcsubject)
    print(glcsubject_sum)
    if glcsubject_sum < 9:
        print('GLC 대학교양 ' + str(9 - glcsubject_sum) + '학점 이수 필요')
    else:
        print('GLC 대학교양 달성 완료!')

    # RC101
    rc101_sum = sum_of_credits(rc101)
    if rc101_sum < 1:
        print('RC101 ' + str(1 - rc101_sum) + '학점 이수 필요')
    else:
        print('RC101 달성 완료!')

    return
basic_requirement_fulfilled()


# 성적 처리 리스트
#응용정보공학
aie_only_standard = [18, 12, 24, 45] #전기, 전필, 전선, 34천
aie_1st_double_standard = [9, 12, 15, 45] #전기, 전필, 전선, 34천
aie_2nd_double_standard = [9, 12, 15] #전기, 전필, 전선
aie_minor_standard = [6, 6, 9] #전기, 전필, 전선

# 바이오생활공학
gbl_only_standard = [18, 12, 24, 45] #전기, 전필, 전선, 34천
gbl_1st_double_standard = [9, 12, 15, 45] #전기, 전필, 전선, 34천
gbl_2nd_double_standard = [9, 12, 15] #전기, 전필, 전선
gbl_minor_standard = [6, 6, 9] #전기, 전필, 전선

# 문화미디어
cmm_only_standard = [6, 0, 42, 45] #전기, 전필, 전선, 34천
cmm_1st_double_standard = [6, 0, 30, 45] #전기, 전필, 전선, 34천
cmm_2nd_double_standard = [6, 0, 30] #전기, 전필, 전선
cmm_minor_standard = [6, 0, 15] #전기, 전필, 전선

# 한국언어문화교육
kce_only_standard = [0, 42, 6, 45] #전기, 전필, 전선, 34천
kce_1st_double_standard = [0, 39, 6, 45] #전기, 전필, 전선, 34천
kce_2nd_double_standard = [0, 39, 6] #전기, 전필, 전선
kce_minor_standard = [0, 0, 0] #전기, 전필, 전선 (전필 전선 상관없이 총 21학점, 영역별 이수요건 존재)

#!!!!!!!!한국언어문화교육 영역별 이수!!!!!!!!!!
#영역1, 영역2, 영역3, 영역4, 영역5
kce_only_area = [6, 6, 24, 6, 3] # 복수전공과 동일하지만 영역 1, 2, 3 중 하나에서 3학점 추가 이수
kce_double_area = [6, 6, 24, 6, 3]
kce_minor_area = [3, 3, 9, 3, 3]

#국제통상
icm_only_standard = [6, 0, 42, 45] #전기, 전필, 전선, 34천
icm_1st_double_standard = [6, 0, 30, 45] #전기, 전필, 전선, 34천
icm_2nd_double_standard = [6, 0, 30] #전기, 전필, 전선
icm_minor_standard = [0, 0, 0] #전기, 전필, 전선 (전필 전선 상관없이 총 21학점 이상 이수)

#국제통상 부전공 필수 이수과목 학정번호 (이 4과목 중 2과목 포함 총 21학점 이상 이수)
#[[국제통상입문 학정번호 리스트], [경영과회계 학정번호 리스트], [한국과국제관계 학정번호 리스트], [국제통상의통계적분석 학정번호 리스트]]
icm_minor_required_course = [['GCI1101', 'GLD1102', 'GLD1101'], ['GIC2209', 'GLD2209'], ['GIC2301', 'GLD2301'], ['GIC2210', 'GLD2210', 'GIC3305']] #이 4과목 중 2과목 이상 이수.

#AI융합심화전공
ai_shimhwa = [[], ]
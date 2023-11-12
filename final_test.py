import csv
import numpy as np

'''1-2'''
def get_report(report_file):
    with open(report_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = [[c.replace('\ufeff', '') for c in row] for row in reader]
    return data

def course_csv_to_np(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = [[c.replace('\ufeff', '') for c in row] for row in reader]
    return np.array(data)


def create_list_of_courses(course_np, report):
    list_of_courses = []

    for row in report:
        if row[0] in course_np:
            # print("row  : ", row[0])
            key = np.where(course_np == row[0])[0][0]
            #if course_np[key][1] != row[1]:
                #print('학정번호의 과목 [' + course_np[key][1] + ']와/과 성적표의 과목 [' + row[1] + ']이 다릅니다.')
            list_of_courses.append(row)

    return list_of_courses


def calc_other_requirements():
    return


test_data = get_report('output.csv')

# length 길이 맞추기
for row in test_data.copy():
    # print("row : ", row)
    if len(row) < 3:
        test_data.remove(row)
    elif len(row) < 4:
        row.insert(2, "")
        row.insert(4, "")

# Fail 성적 모두 제외
# for row in test_data:
#     print("row : ", row)
#     if row[4] in ['U', 'W', 'WE', 'F', 'NP']:
#         test_data.remove(row)
aie_course_np = course_csv_to_np('aie_course.csv')
# list_of_courses = create_list_of_courses(aie_course_np, test_data)
print(test_data)

'''1-3 (변경사항 있음)'''
# 선택할 수 있는 항목들이 들어있는 리스트
options = ['응용정보공학', '바이오생활공학', '국제통상학', '문화미디어학', '한국언어문화교육학'] #해당 리스트 수정할 때 주의!
# 사용자로부터 입력 받기
major = input(f"학생의 제 1 전공을 선택하세요 : {', '.join(options)}\n")
# 입력이 유효한지 확인
while major not in options:
    print("유효하지 않은 선택입니다. 다시 시도하세요.")
    major = input(f"다음 중 하나를 선택하세요: {', '.join(options)}\n")

ai_advanced = ''
#ai융합심화전공 물어보기
if major == '응용정보공학':
    ai_advanced = input(f"AI융합심화전공을 전공하시나요(Y/N)? : ")
    while ai_advanced not in ['Y', 'N']:
        print("유효하지 않은 선택입니다. 다시 시도하세요.")
        ai_advanced = input(f"다음 중 하나를 선택하세요(Y/N): ")

# 선택할 수 있는 항목들이 들어있는 리스트
options = ['응용정보공학', '바이오생활공학', '국제통상학', '문화미디어학', '한국언어문화교육학' , '없음']
# 사용자로부터 입력 받기
double_major = input(f"학생의 제 2 전공을 선택하세요 : {', '.join(options)}\n")
# 입력이 유효한지 확인
while double_major not in options:
    print("유효하지 않은 선택입니다. 다시 시도하세요.")
    double_major = input(f"다음 중 하나를 선택하세요: {', '.join(options)}\n")

# 선택할 수 있는 항목들이 들어있는 리스트
options = ['응용정보공학', '바이오생활공학', '국제통상학', '문화미디어학', '한국언어문화교육학' , '없음']
# 사용자로부터 입력 받기
minor_major = input(f"학생의 제 부전공을 선택하세요 : {', '.join(options)}\n")
# 입력이 유효한지 확인
while minor_major not in options:
    print("유효하지 않은 선택입니다. 다시 시도하세요.")
    minor_major = input(f"다음 중 하나를 선택하세요: {', '.join(options)}\n")

'''1-3 (여기서부터 변경사항 존재)'''

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
            #if course_np[key][1] != row[1]:
                #print('학정번호의 과목 [' + course_np[key][1] + ']와/과 성적표의 과목 [' + row[1] + ']이 다릅니다.')
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


def create_list_of_3_4000(report):
    list_of_courses = []

    for row in report:
        if row[0][3] == '3' or row[0][3] == '4':
            list_of_courses.append(row)

    return list_of_courses


def fail_course_collector(test_data):
    # Fail 성적 모두 제외
    fail_course = []
    for row in test_data:
        if row[4] in ['U', 'W', 'WE', 'F', 'NP']:
            fail_course.append(row)
            test_data.remove(row)
    # print("fail course : ", fail_course)
    return fail_course


def course_length_count(major_origin):
    total_length = 0
    for i in major_origin:
        total_length += float(i[3])
    return total_length

# Fail 성적 모두 제외
fail_courses = fail_course_collector(test_data)

#1. 전체 학점 확인
total_needs = 126.0 - course_length_count(test_data)

# 2. 3_4000 요건 확인
course_3_4000 = create_list_of_3_4000(test_data)
course_3_4000_length = course_length_count(create_list_of_3_4000(test_data))
course_3_4000_needs = 45.0 - course_3_4000_length

#3. 전공 요건 확인
#전공별 강의 목록을 ndarray로 가져오기
aie_course_np = course_csv_to_np('aie_course.csv')
bio_course_np = course_csv_to_np('bio_course.csv')
media_course_np = course_csv_to_np('media_course.csv')
intcommerce_course_np = course_csv_to_np('intcommerce_course.csv')
korean_course_np = course_csv_to_np('korean_course.csv')

#['응용정보공학', '바이오생활공학', '국제통상학', '문화미디어학', '한국언어문화교육학' , '없음']
course_np_dict = {options[0]: aie_course_np, options[1]: bio_course_np, options[2]: intcommerce_course_np, options[3]: media_course_np, options[4]: korean_course_np}

'''
# 성적표 주인이 들은 Fail하지 않은 강의 중 응용정보공학전공 강의 추출하기
aie_major_list_course = create_list_of_courses(aie_course_np, test_data)
aie_major_list_length = course_length_count(aie_major_list_course)
# print(aie_major_list_course)

# 전기, 전필, 전선 Divider
major_basic, major_required, major_elective = divide_major_to_three(aie_course_np, test_data)
aie_major_basic_length = course_length_count(major_basic)
aie_major_required_length = course_length_count(major_required)
aie_major_elective_length = course_length_count(major_elective)
'''

major_course_list = []
double_major_course_list = []
minor_course_list = []
#전공
#요건
major_standard = [0,0,0,0,0]
major_kce_area_check = [0,0,0,0,0,0]
#이수
major_completed = [0,0,0]
#필요
major_needs = [0,0,0]

#복전전공 (선택 시에만 존재)
double_major_standard, double_major_kce_area_check = [0, 0, 0], [0, 0, 0, 0]
double_major_completed = [0,0,0]
double_major_needs = [0,0,0]

#부전공 (선택 시에만)
minor_standard, minor_icm_check, minor_kce_area_check = [0, 0, 0], [0,0,0,0,0], [0,0,0,0,0]
minor_completed = [0,0,0]
minor_needs = [0,0,0]

#AI융합심화 추가 요건
ai_check = [0,0]

#한국언어문화교육 이수한 영역 개수 확인 (array로 리턴)
def check_area_kce(report):
    area = [0.0, 0.0, 0.0, 0.0, 0.0]

    for row in report:
        if row[0] in korean_course_np:
            key = np.where(korean_course_np == row[0])[0][0]
            if korean_course_np[key][3] == '1':
                area[0] += float(row[3])
            elif korean_course_np[key][3] == '2':
                area[1] += float(row[3])
            elif korean_course_np[key][3] == '3':
                area[2] += float(row[3])
            elif korean_course_np[key][3] == '4':
                area[3] += float(row[3])
            elif korean_course_np[key][3] == '5':
                area[4] += float(row[3])
    return area


def major_only(major):
    #해당 전공의 강의 목록 불러오기
    course_np_list = course_np_dict[major]
    course_list = create_list_of_courses(course_np_list, test_data)

    #전공별 Standard
    aie_only_standard = [18, 12, 24]  # 전기, 진필, 전선
    gbl_only_standard = [18, 12, 24]  # 전기, 전필, 전선
    cmm_only_standard = [6, 0, 42]  # 전기, 전필, 전선
    kce_only_standard = [0, 42, 6]  # 전기, 전필, 전선
    kce_only_area = [6, 6, 24, 6, 3]  # +영역 1, 2, 3 중 하나에서 3학점 추가 이수 (영역 1,2,3의 합이 39)
    icm_only_standard = [6, 0, 42]  # 전기, 전필, 전선

    #Standard 목록 만들기
    standard_dict = {options[0]: aie_only_standard, options[1]: gbl_only_standard, options[2]: icm_only_standard, options[3]: cmm_only_standard, options[4]: kce_only_standard}

    #졸업요건
    standard = standard_dict[major]

    #전기, 전필, 전선 나누기
    length = []
    major_basic, major_required, major_elective = divide_major_to_three(course_np_list, test_data)
    length.append(course_length_count(major_basic))
    length.append(course_length_count(major_required))
    length.append(course_length_count(major_elective))

    needs = [0, 0, 0]
    for i in range(3):
        need = standard[i] - length[i]
        needs[i] = (need if need >= 0 else 0) #필수 이수 요건보다 더 들었을 수도 있기 때문에 0으로

    kce_area_check = [1, 1, 1, 1, 1, 1]  # 1이 충족, 0이 미충족, 마지막은 영역 1,2,3의 합 (39 이상이면 1)

    if major == '한국언어문화교육학':
        area = check_area_kce(test_data)
        for i in range(5):
            sub = int(area[i]) - kce_only_area[i] #i영역 이수 학점 - 필요 학점 (음수일 경우 학점 부족)
            if sub < 0:
                kce_area_check[i] = 0
                #print('한국언어교육전공 영역' + str(i) + '의 학점이 ' + str(sub) + '만큼 부족합니다')
        #영역 1, 2, 3의 합이 39가 아니며 영역1, 2, 3 중에서 이미 미달난게 없을 경우
        if (int(area[0]) + int(area[1]) + int(area[2])) < 39 and (kce_area_check[0]+kce_area_check[1]+kce_area_check[2]) >= 3:
            kce_area_check[5] = 0
            #print('한국언어교육전공 단일전공의 경우 영역 1, 2, 3 중 하나에서 3학점을 추가로 이수해야합니다.')

    # course_list: 전공 이수한 수업 리스트
    # standard: 이수해야하는 학점 수
    # length: 이수한 학점 수 [전기, 전필, 전선]
    # needs = [basic_needs, required_needs, elective_needs, total_needs]
    return course_list, standard, length, needs, kce_area_check


def double_major_first(major):
    # 해당 전공의 강의 목록 불러오기
    course_np_list = course_np_dict[major]
    course_list = create_list_of_courses(course_np_list, test_data)

    #전공별 Standard
    aie_1st_double_standard = [9, 12, 15]  # (응정) : 전기, 진필, 전선
    gbl_1st_double_standard = [9, 12, 15]  # 전기, 전필, 전선
    cmm_1st_double_standard = [6, 0, 30]  # 전기, 전필, 전선
    kce_1st_double_standard = [0, 39, 6]  # 전기, 전필, 전선
    kce_double_area = [6, 6, 24, 6, 3]
    icm_1st_double_standard = [6, 0, 30]  # 전기, 전필, 전선

    #Standard 목록 만들기
    standard_dict = {options[0]: aie_1st_double_standard, options[1]: gbl_1st_double_standard, options[2]: icm_1st_double_standard,
                     options[3]: cmm_1st_double_standard, options[4]: kce_1st_double_standard}

    #전공에 대한 졸업 요건
    standard = standard_dict[major]

    # 전기, 전필, 전선 나누기
    length = []
    major_basic, major_required, major_elective = divide_major_to_three(course_np_list, test_data)
    length.append(course_length_count(major_basic))
    length.append(course_length_count(major_required))
    length.append(course_length_count(major_elective))

    needs = [0, 0, 0]
    for i in range(3):
        need = standard[i] - length[i]
        needs[i] = (need if need>=0 else 0)#필수 이수 요건보다 더 들었을 수도 있기 때문에 0으로

    kce_area_check = [1, 1, 1, 1, 1]  # 1이 충족, 0이 미충족, 마지막은 영역 1,2,3의 합 (39 이상이면 1)

    if major == '한국언어문화교육학':
        area = check_area_kce(test_data)
        for i in range(5):
            sub = int(area[i]) - kce_double_area[i]  # i영역 이수 학점 - 필요 학점 (음수일 경우 학점 부족)
            if sub < 0:
                kce_area_check[i] = 0
                # print('한국언어교육전공 영역' + str(i) + '의 학점이 ' + str(sub) + '만큼 부족합니다')

    # course_list: 전공 이수한 수업 리스트
    # standard: 이수해야하는 학점 수
    # length: 이수한 학점 수 [전기, 전필, 전선]
    # needs = [basic_needs, required_needs, elective_needs, total_needs]
    return course_list, standard, length, needs, kce_area_check


def double_major_second(double_major):
    # 해당 전공의 강의 목록 불러오기
    course_np_list = course_np_dict[double_major]
    course_list = create_list_of_courses(course_np_list, test_data)

    # 전공별 Standard
    aie_2nd_double_standard = [9, 12, 15]  # 응정을 제 2전공으로 복전하는 경우 : 전기, 진필, 전선, 전공총합
    gbl_2nd_double_standard = [9, 12, 15]  # 전기, 전필, 전선
    cmm_2nd_double_standard = [6, 0, 30]  # 전기, 전필, 전선
    kce_2nd_double_standard = [0, 39, 6]  # 전기, 전필, 전선
    kce_double_area = [6, 6, 24, 6, 3]
    icm_2nd_double_standard = [6, 0, 30]  # 전기, 전필, 전선

    # Standard 목록 만들기
    standard_dict = {options[0]: aie_2nd_double_standard, options[1]: gbl_2nd_double_standard,
                     options[2]: icm_2nd_double_standard,
                     options[3]: cmm_2nd_double_standard, options[4]: kce_2nd_double_standard}

    # 전공에 대한 졸업 요건
    standard = standard_dict[double_major]

    # 전기, 전필, 전선 나누기
    length = []
    double_major_basic, double_major_required, double_major_elective = divide_major_to_three(course_np_list, test_data)
    length.append(course_length_count(double_major_basic))
    length.append(course_length_count(double_major_required))
    length.append(course_length_count(double_major_elective))

    needs = [0, 0, 0]
    for i in range(3):
        need = standard[i] - length[i]
        needs[i] = (need if need >= 0 else 0)  # 필수 이수 요건보다 더 들었을 수도 있기 때문에 0으로

    kce_area_check = [1, 1, 1, 1, 1]  # 1이 충족, 0이 미충족, 마지막은 영역 1,2,3의 합 (39 이상이면 1)

    if double_major == '한국언어문화교육학':
        area = check_area_kce(test_data)
        for i in range(5):
            sub = int(area[i]) - kce_double_area[i]  # i영역 이수 학점 - 필요 학점 (음수일 경우 학점 부족)
            if sub < 0:
                kce_area_check[i] = 0
                # print('한국언어교육전공 영역' + str(i) + '의 학점이 ' + str(sub) + '만큼 부족합니다')

    return course_list, standard, length, needs, kce_area_check

def major_ai():
    # 해당 전공의 강의 목록 불러오기
    course_np_list = course_csv_to_np('ai_advanced_course.csv') #AIE 제1전공자 필수. 무조건 AIE 전공 불러오게 됨
    course_list = create_list_of_courses(course_np_list, test_data)

    #Standard
    aie_only_standard = [18, 12, 24]  # 전기, 진필, 전선

    # 졸업요건
    standard = aie_only_standard

    # 전기, 전필, 전선 나누기
    length = []
    major_basic, major_required, major_elective = divide_major_to_three(course_np_list, test_data)
    length.append(course_length_count(major_basic))
    length.append(course_length_count(major_required))
    length.append(course_length_count(major_elective))

    #전공 학점
    needs = [0, 0, 0]
    for i in range(3):
        need = standard[i] - length[i]
        needs[i] = (need if need >= 0 else 0)  # 필수 이수 요건보다 더 들었을 수도 있기 때문에 0으로

    ai_check = [0, 0] #[수강한 ai과목 개수, 인공지능개론 이수 여부 (1일 경우 이수)

    # 1. AI과목 3개 이상 이수
    for row in course_list:
        if row[0] in ['AIC2100', 'AIC2130', 'AIC2120', 'AIC3100', 'AIC2110', 'AIC3110']:
            ai_check[0] += 1
    # 2. 인공지능개론 이수
    for row in major_required:
        if row[0] == 'GAI3006':
            ai_check[1] = 1
    return course_list, standard, length, needs, ai_check

def minor_major_function(minor_major):
    course_np_list = course_np_dict[minor_major]
    course_list = create_list_of_courses(course_np_list, test_data)

    # 전공별 Standard
    aie_minor_standard = [6, 6, 9]  # 전기, 전필, 전선
    gbl_minor_standard = [6, 6, 9]  # 전기, 전필, 전선
    cmm_minor_standard = [6, 0, 15]  # 전기, 전필, 전선
    kce_minor_standard = [0, 0, 0]  # 전기, 전필, 전선 (전필 전선 상관없이 총 21학점, 영역별 이수요건 존재)
    icm_minor_standard = [0, 0, 0]  # 전기, 전필, 전선 (전필 전선 상관없이 총 21학점 이상 이수)
    kce_minor_area = [3, 3, 9, 3, 3]

    # 국제통상 부전공 필수 이수과목 학정번호 (이 4과목 중 2과목 포함 총 21학점 이상 이수)
    # [[국제통상입문 학정번호 리스트], [경영과회계 학정번호 리스트], [한국과국제관계 학정번호 리스트], [국제통상의통계적분석 학정번호 리스트]]
    icm_minor_required_course = [['GCI1101', 'GLD1102', 'GLD1101'], ['GIC2209', 'GLD2209'], ['GIC2301', 'GLD2301'],
                                 ['GIC2210', 'GLD2210', 'GIC3305']]  # 이 4과목 중 2과목 이상 이수.

    # Standard 목록 만들기
    standard_dict = {options[0]: aie_minor_standard, options[1]: gbl_minor_standard,
                     options[2]: icm_minor_standard,
                     options[3]: cmm_minor_standard, options[4]: kce_minor_standard}

    # 전공에 대한 졸업 요건
    standard = standard_dict[minor_major]

    # 전기, 전필, 전선 나누기
    length = []
    minor_major_basic, minor_major_required, minor_major_elective = divide_major_to_three(course_np_list, test_data)
    length.append(course_length_count(minor_major_basic))
    length.append(course_length_count(minor_major_required))
    length.append(course_length_count(minor_major_elective))

    needs = [0, 0, 0]
    for i in range(3):
        need = standard[i] - length[i]
        needs[i] = (need if need >= 0 else 0)  # 필수 이수 요건보다 더 들었을 수도 있기 때문에 0으로

    kce_area_check = [1, 1, 1, 1, 1]  # 1이 충족, 0이 미충족, 마지막은 영역 1,2,3의 합 (39 이상이면 1)
    icm_minor_check = [0, 0, 0, 0, 1] # 0~3: 각각 수업0~3 이수 (2개 이상 달성), 4: 21학점 이상 이수 (각자 달성하면 1, 실패하면 0)

    if minor_major == '한국언어문화교육학':
        area = check_area_kce(test_data)
        for i in range(5):
            sub = int(area[i]) - kce_minor_area[i]  # i영역 이수 학점 - 필요 학점 (음수일 경우 학점 부족)
            if sub < 0:
                kce_area_check[i] = 0
                # print('한국언어교육전공 영역' + str(i) + '의 학점이 ' + str(sub) + '만큼 부족합니다')

    # 이수한 과목에 대한 학정번호 리스트
    completed_course_id = []
    for row in test_data:
        completed_course_id.append(row[0])

    if minor_major == '국제통상학':
        # 21학점 이상 이수
        if (length[0] + length[1] + length[2]) < 21:
            icm_minor_check[4] = 0
        # 4 과목 이수 여부 체크 (2개 이상 이수 해야함)
        for course_name_index in range(4):
            for course_id in icm_minor_required_course[course_name_index]:
                if course_id in icm_minor_required_course:
                    icm_minor_check[course_name_index] = 1

    return course_list, standard, length, needs, kce_area_check, icm_minor_check
# (0)AI융합심화전공일 시 요건 충족여부
# (0-1) 단일 전공일 때
if ai_advanced == 'Y' and double_major == '없음':
    major_course_list, major_standard, major_completed, major_needs,ai_check = major_ai()

# (0-2) 복수전공일 떄
elif ai_advanced == 'Y':
    major_course_list, major_standard, major_completed, major_needs, ai_check= major_ai() #제1전공 요건 변함X
    double_major_course_list, double_major_standard, double_major_completed, double_major_needs, double_major_kce_area_check = double_major_second(double_major)

# (1)복수전공이 아닐시 요건 충족 여부 (단일전공 or 단일전공+부전공)
elif double_major == '없음':
    # 수업 리스트, 전공 학점 요건, 전공 이수 학점, 전공 부족 학점, 한국언어문화교육 영역 이수
    major_course_list, major_standard, major_completed, major_needs, major_kce_area_check = major_only(major)
    kce_only_area = [6, 6, 24, 6, 3]

# (2)복수전공 시 요건 충족 여부
else:
    # (2-1) 제1전공
    major_course_list, major_standard, major_completed, major_needs, major_kce_area_check = double_major_first(major)

    # (2-2) 제2전공
    double_major_course_list, double_major_standard, double_major_completed, double_major_needs, double_major_kce_area_check = double_major_second(double_major)

# 부전공 요건 충족 여부
if minor_major != '없음':
    minor_course_list, minor_standard, minor_completed, minor_needs, minor_kce_area_check, minor_icm_check = minor_major_function(minor_major)
    # minor_kce_area_check = [영역1, 영역2, 영역3, 영역4, 영역5] <- 모두 1이어야 졸업요건 만족
    # minor_icm_check = [과목1, 과목2, 과목3, 과목4, 21학점 이상] <- 인덱스 0~3 중 2개가 1, 인덱스 4가 1이면 졸업요건 만족

# 이미 들어간 수업 리스트 빼기
def major_course_eliminator(test_data):
    remaining = []
    # Fail 성적 모두 제외
    for row in test_data:
        if row not in (major_course_list + double_major_course_list + minor_course_list):
            remaining.append(row)
    return remaining

remaining_course = major_course_eliminator(test_data)
#print(remaining_course)


#교양 요건 확인
def sum_of_credits(list):
    sum = 0
    for row in list:
        sum += float(row[3])
    return sum

# 교양 강의 목록을 ndarray로 가져오기
glcsubject_course_np = course_csv_to_np('glcsubject_course.csv')
english_course_np = course_csv_to_np('english_course.csv')
christianity_course_np = course_csv_to_np('christianity_course.csv')
chapel_course_np = course_csv_to_np('chapel.csv')
rc101_course_np = course_csv_to_np('rc101.csv')

#과목 리스트 만들기
rc101_list = create_list_of_courses(rc101_course_np, test_data)
chapel_list = create_list_of_courses(chapel_course_np, test_data)
christianity_list = create_list_of_courses(christianity_course_np, test_data)
english_list = create_list_of_courses(english_course_np, test_data)
glcsubject_list = create_list_of_courses(glcsubject_course_np, test_data)

#각 교양 이수학점 (GLC 영어의 경우 이수 과목 수)
chapel_credit = sum_of_credits(chapel_list)
christianity_credit = sum_of_credits(christianity_list)
rc101_credit = sum_of_credits(rc101_list)
english_course_taken = len(english_list)
glcsubject_credit = sum_of_credits(glcsubject_list)

#이수 완료 여부
chapel_pass = chapel_credit >= 2
christianity_pass = christianity_credit >= 3
english_pass = len(english_list) >= 2
glcsubject_pass = glcsubject_credit >= 9
rc101_pass =rc101_credit >=1

#print(chapel_pass)
#print(christianity_pass)
#print(english_pass)
#print(glcsubject_pass)
#print(rc101_pass)
'''
#TODO: 부전공 50% 이상이면 보여주기 (전공에 포함된 과목 외의 데이터만 가지고)
def show_minor():
    # 전공별 Minor Standard
    aie_minor_standard = [6, 6, 9]  # 전기, 전필, 전선
    gbl_minor_standard = [6, 6, 9]  # 전기, 전필, 전선
    cmm_minor_standard = [6, 0, 15]  # 전기, 전필, 전선
    kce_minor_standard = [0, 0, 0]  # 전기, 전필, 전선 (전필 전선 상관없이 총 21학점, 영역별 이수요건 존재)
    icm_minor_standard = [0, 0, 0]  # 전기, 전필, 전선 (전필 전선 상관없이 총 21학점 이상 이수)
    kce_minor_area = [3, 3, 9, 3, 3]

    # 국제통상 부전공 필수 이수과목 학정번호 (이 4과목 중 2과목 포함 총 21학점 이상 이수)
    # [[국제통상입문 학정번호 리스트], [경영과회계 학정번호 리스트], [한국과국제관계 학정번호 리스트], [국제통상의통계적분석 학정번호 리스트]]
    icm_minor_required_course = [['GCI1101', 'GLD1102', 'GLD1101'], ['GIC2209', 'GLD2209'], ['GIC2301', 'GLD2301'],
                                 ['GIC2210', 'GLD2210', 'GIC3305']]  # 이 4과목 중 2과목 이상 이수.

    # minor_major 빼고.
    course_np_list = course_np_dict[minor_major]
    course_list = create_list_of_courses(course_np_list, test_data)


    for one_major in options:
        if(one_major==minor_major):
            continue
        else:
            # 전공을 50% 이상 들었는지 확인
            minor_major_basic, minor_major_required, minor_major_elective = divide_major_to_three(course_np_list,test_data)
            total_credit = course_length_count(minor_major_basic) + course_length_count(minor_major_required) + course_length_count(minor_major_elective)
            #TODO: 50%이상 들었는지, 각각 요건을 완료했는지 구현

#TODO: 마이크로전공 추가 (major_course_eliminator 함수에도 해당 전공 수업들 추가)

#기타 과목 (전체 - (전공+교양)) 구하기
def major_and_gyoyang_course_eliminator(remaining_course):
    general_elective_list = []
    # Fail 성적 모두 제외
    for row in remaining_course:
        if row not in (rc101_list + chapel_list + christianity_list + glcsubject_list + rc101_list + english_list):
            general_elective_list.append(row)
    return general_elective_list

general_elective_list = major_and_gyoyang_course_eliminator(remaining_course)
#print(general_elective_list)

#TODO: (확인) 교양 등등 부족학점을 계산하는 식에 3항 연산식 (음수가 안나오게) 적용했는지 확인

#교양
#요건:작성 필요 (모두 동등)

#이수: (영어의 경우 학점이 아닌 과목 개수이기 때문에 유의)
#print("chapel_credit : ",chapel_credit)
#print("christianity_credit : ",christianity_credit)
#print("rc101_credit : ", rc101_credit)
#print("english_course_taken: ",english_course_taken) #수업개수 2개, 1개, 0개
#print("glcsubject_credits : ",glcsubject_credit)

#필요: 계산 필요
'''


# ---------------출력----------------------

student_name = input("학생의 성함을 입력해주세요 : ")
result = "가능" if (course_3_4000_needs==0 and major_needs==0 and 9-(ai_check[0]*3)<0 and ai_check[1]==1 and double_major_needs ==0 and minor_needs==0 and chapel_pass and christianity_pass and rc101_pass and english_pass and glcsubject_pass) else "불가능"
print(f"----------{student_name}님의 {major}전공 자가진단 상세내역-----------\n")
print(f"{student_name}님은 졸업 예비판정 시스템 상, 졸업이 {result}합니다.")
print()
print(f"현재 이수한 {major} 3,4천단위 학점은 {course_3_4000_length}점이며, 부족한 학점은 {course_3_4000_needs}입니다")
print()
print(f"현재 이수한 {major}전공 학점은 {(major_completed[0] + major_completed[1] + major_completed[2])}점이며, 부족한 전공 학점은 {major_needs}입니다.")
print(f"현재 이수한 {major}전공의 전공기초 학점은 {major_completed[0]}점이며, 부족한 학점은 {major_needs[0]}입니다.")
print(f"현재 이수한 {major}전공의 전공필수 학점은 {major_completed[1]}점이며, 부족한 학점은 {major_needs[1]}입니다.")
print(f"현재 이수한 {major}전공의 전공선택 학점은 {major_completed[2]}점이며, 부족한 학점은 {major_needs[2]}입니다.")
print()

if(ai_advanced == 'Y'):
    print(f"현재 이수한 AI융합심화전공 학점은 {ai_check[0]*3}점이며, 부족한 AI융합심화전공 학점은 {9-(ai_check[0]*3) if (9-(ai_check[0]*3))>0 else 0}입니다.")
    print(f"현재 AI융합심화전공 이수를 위해 이수해야하는 인공지능개론과목을", ("이수한" if ai_check[1]==1 else "이수하지 않은"), "상태입니다.")
    print()

if(double_major != '없음'):
    print(f"현재 이수한 {double_major}전공 학점은 {(double_major_completed[0] + double_major_completed[1] + double_major_completed[2])}점이며, 부족한 전공 학점은 {double_major_needs}입니다.")
    print(f"현재 이수한 {double_major}전공의 전공기초 학점은 {double_major_completed[0]}점이며, 부족한 학점은 {double_major_needs[0]}입니다.")
    print(f"현재 이수한 {double_major}전공의 전공필수 학점은 {double_major_completed[1]}점이며, 부족한 학점은 {double_major_needs[1]}입니다.")
    print(f"현재 이수한 {double_major}전공의 전공선택 학점은 {double_major_completed[2]}점이며, 부족한 학점은 {double_major_needs[2]}입니다.")
    print()

if(minor_major != '없음'):
    print(f"현재 이수한 {minor_major}전공 학점은 {(minor_completed[0] + minor_completed[1] + minor_completed[2])}점이며, 부족한 전공 학점은 {minor_needs}입니다.")
    print(f"현재 이수한 {minor_major}전공의 전공기초 학점은 {minor_completed[0]}점이며, 부족한 학점은 {minor_needs[0]}입니다.")
    print(f"현재 이수한 {minor_major}전공의 전공필수 학점은 {minor_completed[1]}점이며, 부족한 학점은 {minor_needs[1]}입니다.")
    print(f"현재 이수한 {minor_major}전공의 전공선택 학점은 {minor_completed[2]}점이며, 부족한 학점은 {minor_needs[2]}입니다.")
    print()

print(f"현재 이수한 채플 학점은 {(chapel_credit)}점이며, 부족한 채플 학점은 {2-chapel_credit if (2-chapel_credit) > 0 else 0}입니다.")
print(f"현재 이수한 기독교의 이해 학점은 {(christianity_credit)}점이며, 부족한 기독교의 이해 학점은 {3-christianity_credit if (3-christianity_credit) > 0 else 0}입니다.")
print(f"현재 이수한 RC101 학점은 {(rc101_credit)}점이며, 부족한 RC101 학점은 {1-rc101_credit if (1-rc101_credit) > 0 else 0}입니다.")
print(f"현재 이수한 GLC영어 학점은 {english_course_taken*3}점이며, 부족한 GLC영어 학점은 {(2 - english_course_taken)*3 if (2-english_course_taken) > 0 else 0}입니다.")
print(f"현재 이수한 GLC교양 학점은 {glcsubject_credit}점이며, 부족한 GLC교양 학점은 {9 - glcsubject_credit if (9-glcsubject_credit) > 0 else 0}입니다.")
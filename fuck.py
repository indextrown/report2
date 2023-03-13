## 파일 읽기
## 읽기( r 모드로 test.inp 파일을 객체로 열기
testFile = open('./test.inp', 'r')

# test.inp에서 첫번째 문장 문자열을 읽고 변수에 정수 형태로 저장
test = int(testFile.readline())

# # 입력값이 5보다 크거나 같고 1000보다 작거나 같은 조건일 때만 실행
if test >= 5 and test <= 1000:
    # 변수 test 출력
    # print(test)

    # 파일 내용을 리스트 형식으로 저장(str 방식)
    test_all = testFile.readlines()

    # 리스트로 저장할 때 나타나는 개행문자 \n 삭제
    test_all = [t.rstrip('\n') for t in test_all]

    # 리스트를 오름차순으로 정렬해주는 기능
    test_all.sort()
    # 오름차순으로 정렬된 리스트 출력
    # print(test_all)

    # 딕셔너리 생성
    dict = {}

    # 가장 긴 Firstname 문자열을 찾기 위해 리스트 생성
    first = []
    # 리스트 값을 추출해서 딕셔너리에 삽입
    for i in test_all:
        dict[i[0:5]] = i[6:]

        # 딕셔너리 value값을 name 변수로 저장
        name = i[6:]

        # 공백 기준으로 문자열 자르기
        name_cut = name.split()

        # Firstname Last name 문자열 추출
        First_name = name_cut[0]
        Last_name = name_cut[1]

        # 출력 파일로 데이터를 저장할 때 last name 첫 글자 정렬을 위해
        # 가장 긴 First name 찾기
        first.append(First_name)
    max_first = max(first, key=len)

    # sprint("가장 긴 문자열", max_first)

    # 가장 긴 문자열의 길이
    max_len = len(max_first)
    #print(len(max_first))
    n = 0

    with open('./test.out', 'w', encoding='UTF-8') as f:
        for i in test_all:
            dict[i[0:5]] = i[6:]

            # 딕셔너리 value값을 name 변수로 저장
            name = i[6:]

            # 공백 기준으로 문자열 자르기
            name_cut = name.split()

            # Firstname Last name 문자열 추출
            First_name = name_cut[0]
            Last_name = name_cut[1]

            # 가장 긴 문자열의 길이 - 현재 출력하는 First name 함수 길이
            result = max_len - len(First_name)
            # print("결과", result)
            # ===================================================
            # Firstname Last name 문자열 길이 구하기
            if len(First_name) < 30:
                if len(Last_name) < 30:

                    # print(First_name+(result)*" ", Last_name)
                    print(list(dict.keys())[n], First_name + (result) * " ", Last_name)
                    f.write(f'{list(dict.keys())[n]} {First_name + (result) * " "} {Last_name} \n')
                    n = n + 1

                else:
                    print("Last name 길이가 30을 초과했습니다")
            else:
                print("First name 길이가 30을 초과했습니다")



else:
    print("조건을 벗어났습니다")


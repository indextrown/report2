## 파일 읽기
## 읽기( r 모드로 test.inp 파일을 객체로 열기
testFile = open('./test.inp', 'r')

# test.inp에서 첫번째 문장 문자열을 읽고 변수에 정수 형태로 저장
test = int(testFile.readline())

# # 입력값이 5보다 크거나 같고 1000보다 작거나 같은 조건일 때만 실행
if test >= 5 and test <= 1000:
    # 변수 test 출력
    #print(test)

    # 파일 내용을 리스트 형식으로 저장
    test_all = testFile.readlines()
    # 리스트로 저장할 때 나타나는 개행문자 \n 삭제
    test_all = [t.rstrip('\n') for t in test_all]


    # 리스트를 오름차순으로 정렬해주는 기능
    test_all.sort()
    # 오름차순으로 정렬된 리스트 출력
    #print(test_all)

    # Frist name 과 Last name의 길이가 30 이상이면 프로그램 종료문
    print(test_all[1])

else:
    print("조건을 벗어났습니다")


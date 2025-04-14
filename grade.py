while True:
    score = int(input("점수를 입력하세요 (종료하려면 -1): "))
    if score == -1:
        print("프로그램을 종료합니다.")
        break

    if score >= 90:
        print("수")
    elif score >= 80:
        print("우")
    elif score >= 70:
        print("미")
    else:
        print("재시험") SS
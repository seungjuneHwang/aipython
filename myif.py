# 아스키 코드 그림 출력 하기
def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    
    for line in cat:
        print(line)

def print_dog():
    dog = [
        " / \\__",
        "(    @\\___",
        " /         O",
        "/   (_____/",
        "/_____/   U"
    ]

    for line in dog:
        print(line)

def print_rabbit():
    rabbit = [
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    
    for line in rabbit:
        print(line)

# 여기서 반복하면 되겠네
# for i in range(5):
while True: # 무한 반복 (계속 참)
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토 끼")
    print("=====================")
    # n = 3
    n = int(input("선택(0을 입력하면 종료): "))
    # 0 이 입력되면 프로그램 종료
    if n == 0:
        print("프로그램을 종료합니다.")
        break
    # 만약에 1을 입력하면 1번 캐릭터 출력
    if n == 1:
        print("고양이")
        print_cat()
    # 만약에 2를 입력하면 2번 캐릭터 출력
    elif n == 2:
        print("강아지")
        print_dog()
    # 3을 입력하면 3번 캐릭터 출력
    elif n == 3:
        print("토끼")
        print_rabbit()
    # 잘못입력하면 잘못 입력했다고 출력
    else:
        print("잘못입력")
# 여기까지 하면 되겠네

# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.

# 위 프로그램을 완성한한 사람은 프로그램이 계속(무한)반복하게 하고
# 만약에 0을 입력하면 종료 되는 프로그램을 만드시오.
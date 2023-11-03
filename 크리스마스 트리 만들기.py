def 크리스마스_트리_만들기(높이):
    for i in range(1, 높이 + 1):
        spaces = " " * (높이 - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

def main():

    try:
        높이 = int(input("크리스마스 트리의 높이를 설정하세요: "))
        크리스마스_트리_만들기(높이)
    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    main()

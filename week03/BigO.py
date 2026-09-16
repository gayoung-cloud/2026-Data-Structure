n = int(input("정수 입력 :"))
total = 0
for i in range(1,n+1):
    total = total + 1
print(f"1부터 {n}까지 누산 합계는 {total}입니다.")
# f(n) = n + 3
# 0(n) 선형시간을 갖는다
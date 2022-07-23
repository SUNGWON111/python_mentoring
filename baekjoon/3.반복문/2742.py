# https://www.acmicpc.net/problem/2742

N = int(input())
print("\n".join(map(str, range(N, 0, -1))))
# 출력을 할건데 줄을 바꿔 하나씩 출력할거고,
# 리스트를 생성해 문자열로 합친후
#join을 사용 할 때 "구분자.join"
# range(시작, 끝, +할 범위)
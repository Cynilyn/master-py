# 요세푸스 순열 구하는 함수 정의
def yosePus(tolerance, list):
    answer = []
    # 초기 인덱스
    index = tolerance-1
    answer.append(list.pop(index))
    while(len(list) != 0):
        size = len(list)
        index += (tolerance-1)
        # list의 size를 초과하지 않도록 0~size 값 부여
        index = index % size
        answer.append(list.pop(index))
    return answer


length, start = map(int, input().split())

# 입력값 Check
# print(length)
# print(start)

group = []
for i in range(length):
    group.append(i+1)

answer = yosePus(start, group)

# 값을 문자열로 포맷팅
answerP = "<"
for j in range(length):
    if j != length-1:
        answerP += "{0}, ".format(answer[j])
    else:
        answerP += "{0}>".format(answer[j])

print(answerP)

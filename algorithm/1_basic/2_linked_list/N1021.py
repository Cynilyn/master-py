# acmicpc.net/problem/1021


# 입력 리스트 요소 -1 기능(왼쪽 move, delete 시)
def minusList(list1, list2):
    size_list1 = len(list1)
    size_list2 = len(list2)
    for i in range(size_list1):
        if list1[i] <= 1:
            list1[i] = size_list2
        else:
            list1[i] -= 1


# 입력 리스트 요소 +1 기능(오른쪽 move시)
def plusList(list1, list2):
    size_list1 = len(list1)
    size_list2 = len(list2)
    for i in range(size_list1):
        if list1[i] > size_list2-1:
            list1[i] = 1
        else:
            list1[i] += 1


# a1 삭제 기능
def deleteInitial(list1, list2):
    del list2[0]
    # print("현재 list2의 길이 : ", len(list2))
    minusList(list1, list2)


# a(index)를 a1자리까지 왼쪽으로 이동
def leftMove(list1, index, list2):
    global result
    for i in range(index):
        a = list2[0]
        del list2[0]
        list2.append(a)
        result += 1
        minusList(list1, list2)


# a(index)를 a1자리까지 오른쪽으로 이동
def rightMove(list1, index, list2):
    size_list2 = len(list2)
    global result
    for i in range(len(list2)-index):
        a = list2[size_list2-1]
        del list2[size_list2-1]
        list2.insert(0, a)
        plusList(list1, list2)
        result += 1


n, m = map(int, input().split())
list = list(map(int, input().split()))

# print(n, m)
# print(list)

global result
result = 0
lList = []
# n의 크기만큼 리스트에 1~n 값 삽입
for i in range(n):
    lList.append(i+1)


# 연산처리 해야하는 element 마다 값에 따라 연산 수행
for i in range(len(list)):
    if list[i] == 1:
        deleteInitial(list, lList)
    elif list[i] <= (len(lList)+1)//2 and list[i] != 1:
        leftMove(list, list[i]-1, lList)
        deleteInitial(list, lList)
    else:
        rightMove(list, list[i]-1, lList)
        deleteInitial(list, lList)

print(result)

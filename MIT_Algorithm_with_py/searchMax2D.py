# 2차원 배열에서의 극대값 찾기.

#  i ,j = 탐색을 시작할 세로, 가로 인덱스값


def searchMax2D(i, array):

    rowMax = max(array[i])
    x = array[i].index(rowMax)

    # 중앙에서부터 시작해서 행이 모서리에 위치하였을 때는 반환.

    if i <= 0:
        if array[i][x] >= array[i+1][x]:
            return array[i][x]
        else:
            return None

    if i >= len(array)-1:
        if array[i][x] >= array[i-1][x]:
            return array[i][x]
        else:
            return None

    if array[i][x] < array[i-1][x]:
        result = searchMax2D(i-1, array)
        return result
    elif array[i][x] < array[i+1][x]:
        result = searchMax2D(i+1, array)
        return result
    else:
        return rowMax


array = [[63, 57, 50, 37, 44],
         [6, 30, 10, 24, 42],
         [30, 29, 10, 20, 43],
         [7, 8, 49, 48, 44],
         [32, 55, 54, 53, 4],
         [33, 28, 6, 54, 74]]
# [[63, 57, 50, 37, 44], [6, 89, 74, 24, 50],
#          [30, 29, 10, 87, 89], [75, 8, 70, 56, 79], [99, 55, 54, 98, 4], [33, 28, 6, 89, 74]]

print(searchMax2D((len(array)-1)//2, array)
      )

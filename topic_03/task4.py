def findInsertPosition(sortedList: list, target: int) -> int:
    left = 0
    right = len(sortedList)

    while left < right:
        mid = (left+right)//2

        if sortedList[mid] < target:
            left = mid+1
        else: right = mid
    return left


def insertNum(sortedList: list, num: int)-> str:
    workList= sortedList.copy()

    index = findInsertPosition(workList, num)
    workList.insert(index, num)
    return f"Ціль: {num}, знайдена позиція: {index}, результат вставки: {workList}."


sortedList = [3, 4, 5, 6, 9]
print(f"Відсортований список{sortedList}")
print(insertNum(sortedList, 2))
print(insertNum(sortedList, 7))
print(insertNum(sortedList, 15))
print(insertNum(sortedList, 0))
print(insertNum(sortedList, 5))
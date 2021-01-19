#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    greatest_number = number_list[0]
    for number in number_list[1:]:
        greatest_number = max(greatest_number, number)
    return greatest_number


def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    smallest_number = number_list[0]
    for number in number_list[1:]:
        smallest_number = min(smallest_number, number)
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    sum_numbers = 0
    for number in number_list:
        sum_numbers += number
    mean = sum_numbers // len(number_list)
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    minheap = [0]

    # insert
    for number in number_list:
        minheap.append(number)
        index = len(minheap)
        parent = index // 2
        while parent: # 0보다 클때까지            
            if minheap[index] >= minheap[parent]:
                break
            minheap[index], minheap[parent] = minheap[parent], minheap[index]
            index = parent
            parent = index // 2
    # pop
    answer = []
    for i in range( (len(number_list)//2)+1):
        poped_number = minheap[1]
        answer.append(poped_number)
        minheap[1] = minheap.pop()
        index = 1
        child1 = index * 2 + 1
        while child1 < len(minheap):
            min_index = index
            if minheap[min_index] > minheap[child1]:
                min_index = child1
            if child1+1 < len(minheap) and minheap[min_index] > minheap[child1+1]:
                min_index = child1+1
            if min_index == index:
                break
            else:
                minheap[index], minheap[min_index] = minheap[min_index], minheap[index]
                index = min_index
                child1 = index * 2 + 1
    # 홀수
    if len(number_list) % 2:
        median = answer[-1]
    # 짝수
    else:
        median = (answer[-1] + answer[-2]) / 2
    return median

'''
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
입출력 예
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
입출력 예 설명
입출력 예 #1
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.
'''

from itertools import combinations


def isNum(n):
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    for i in arr:
        if isNum(sum(i)):
            answer += 1
    return answer

########### 다른 풀이

def isNum(n):
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def comb(population,num):
	ans = []
    ## 정의된 값인지 확인한다.
	if num > len(population): return ans
	## Base Case
	if num == 1:
		for i in population:
			ans.append([i])
    ## General Case
	elif num>1:
		for i in range(len(population)-num+1): ## i가 시작하는 값 - len(population) - (n-1)이고 이 때 n은 lst로부터 추출할 개수와 같다.
			for temp in comb(population[i+1:],num-1):
				ans.append([population[i]]+temp)

	return ans

def solution(nums):
    answer = 0
    arr = list(comb(nums, 3))
    for i in arr:
        if isNum(sum(i)):
            answer += 1
    return answer

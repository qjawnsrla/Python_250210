# 넘파이? 파이썬에서 과학적인 계산을 하기 위한 핵심 라이브러리, 아나콘다를 사용하면 기본 포함
# - 다차원 배열 객체 제공, 고성능 수학 연산 지원
import numpy as np  # np 라는 별칭으로 사용

data = [0,1,2,3,4,5]    # [] : 리스트 / {} : 딕셔너리 / () : 튜플
a1 = np.array(data)     # 리스트를 numpy 배열로 변환
print(a1)

# 정수와 실수가 혼합된 경우는 전부 실수로 변환
data2 = [0, 1, 2, 3.14, 4, 5.5, 6, 7, 8.99]
a2 = np.array(data2)
print(a2)

# 배열의 속성 확인
x = np.array([0.1, 0.2, 0.3])
print(x.shape)      # 배열의 형태
print(x.dtype)

y = np.array(([1, 2, 3, 4, 5],[6, 7, 8, 9, 10]))
print(y.shape)
print(y.dtype)

z = np.array(([1, 2, 3],[4, 5, 6]))
print(z.shape)
print(z.dtype)      # 결과 값 : int64
# 강제적으로 int32를 사용하고 싶다면?
# 배열을 생성할 때 명시적으로 데이터 타입을 지정할 수 있습니다:
# z = np.array(([1, 2, 3], [4, 5, 6]), dtype=np.int32)
# print(z.dtype)  # int32 출력

# 특정 범위의 배열 생성
a3 = np.arange(0, 10, 2)    # 0 ~ 10 미만, 간격을 2
print(a3)

a4 = np.arange(10)     # 0 ~ 10 미만, 간격 1
print(a4)

# 2차원 배열 생성
a5 = np.arange(12).reshape(4, 3)
print(a5)
print(a5.shape)

# 주어진 범위를 3번째 값으로 일정한 간격으로 삽입
a6 = np.linspace(1, 10, 10)
print(a6)
ab6 = np.linspace(1, 10)
print("ab6" ,ab6)

# 특정한 숫자로 채워진 배열 생성
a7 = np.zeros(10)
print(a7)

a8 = np.zeros((3, 4))
print(a8)

a9 = np.ones(10)
print(a9)

a10 = np.ones((5, 5))
print(a10)

a11 = np.eye(5)     # 5 x 5 단위 행렬
print(a11)

# 배열의 데이터 타입 변환
a12 = np.array(['1.5', '0.44', '3.14', '3.145992'])
print(a12)
print(a12.dtype)

num_a12 = a12.astype(float)
print(num_a12)

a13 = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
num_a13 = a13.astype(int)
print(a13)
print(num_a13)


# 난수 배열의 생성
# rand() : 0 ~ 1 ㅁ만의 실수로 난수 배열을 생성
# a14 = np.random.rand(2, 3)
a14 = (np.random.rand(6) * 45 ) + 2
print(a14)
print(a14.astype(int))

# 지정한 범위에 해당하는 정수로 난수 배열을 생성 : randint()
a15 = np.random.randint(10, size=(5, 10))    # 0 ~ 9 사이의 임의의 값을 사이즈만큼 생성
print(a15)

# numpy 기본 연산 : 각 요소끼리 연산이 가능
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 ** 2)
print(arr2 > 5)

ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
print(ls1 + ls2)

# 통계 연산
arr3 = np.arange(10)    # 0 ~ 9 까지 데이터 생성
print(arr3)
print(f"합계 : {arr3.sum()}")
print(f"평균 : {arr3.mean()}")    # sum(arr3) / len(arr3)
print(f"표준편차 : {arr3.std()}")
print(f"분산 : {arr3.var()}")
print(f"최댓값 : {arr3.max()}")
print(f"최소값 : {arr3.min()}")

arr4 = np.array([9, 7, 6, 12, 3, 45, 18, 1])
print(np.sort(arr4))      # 오름차순 정렬
print(np.argsort(arr4))   # 정렬된 인덱스 반환

arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 인덱싱
print(arr5[6])
# 슬라이싱
print(arr5[5:])     # 6, 7, 8, 9
print(arr5[2:6])    # 3, 4, 5, 6


## 1번 문제 : 1 부터 10 까지의 숫자로 이루어진 1차원 배열을 생성하거, 모든 요소에 5를 더한 결과를 출력하세요.
arr_1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr_1 + 5)
## 풀이
arr__1 = np.arange(1,11)
print(arr__1 + 5)


## 2번 문제 : 1 부터 9 까지의 숫자를 사용하여 3x3 크기의 2차원 배열을 생성하고 출력하세요.
arr_2 = np.random.randint(9, size=(3,3))
print(arr_2)
## 풀이
arr__2 = np.arange(1,10).reshape(3,3)
print(arr__2)

## 3번 문제 : 1부터 20 까지의 숫자로 이루어진 배열을 생성하고, 다음을 계산하세요.
## 1. 배열의 합계
## 2. 배열의 평균
## 3. 배열의 최댓값과 최솟값
arr_3 = np.arange(1, 21)
print(arr_3)
print(f" 합계 : ",arr_3.sum())
print(f" 평균 : ",arr_3.mean())
print(f" 최댓값 : ",arr_3.max())
print(f" 최솟값 : ",arr_3.min())
## 풀이
arr__3 = np.arange(1,21)
print(f"합계 : ,{arr__3.sum()}")
print(f"평균 : {arr__3.mean()}")
print(f"최댓값 : {arr__3.max()}, 최솟값 : {arr__3.min()}")

## 4번 문제. 0 에서 100 사이의 난수를 10개 생성하고, 50 이상인 값을 출력
arr_4 = np.random.randint(100, size=(10))
# arr_4 = np.arange((0,101), 10)
print(arr_4)
print(arr_4[50:])
## 풀이
arr__4 = np.random.randint(0, 101, size=10)
print(arr__4[arr__4 >= 50])


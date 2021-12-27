x = int(input())
y = int(input())

if (x>0) and (y>0) :
    print(1)

elif (x<0) and (y>0) :
    print(2)

elif (x<0) and (y<0) :
    print(3)

elif (x>0) and (y<0) :
    print(4)

#얘도 마찬가지로  (−1000 ≤ x ≤ 1000; x ≠ 0), (−1000 ≤ y ≤ 1000; y ≠ 0)로 x, y의 범위가
#주어져 있는데 문제 풀 때 딱히 고려하지 않는듯..?? 딴 사람이 푼거 봐도 딱히 고려 안한다. 이걸 풀이에 어떻게 표현하나...

# 정렬
# 1302_베스트셀러

import sys
if __name__ == "__main__":
    N = int(input())
    
    # 입력받은 책을 dictionary에 저장
    # book_dic의 Key는 책 제목, Value는 책이 팔린 횟수
    book_dic = {}
    for i in range(N):
        bookname = sys.stdin.readline()
        if bookname in book_dic:
            book_dic[bookname] += 1
        else:
            book_dic[bookname] = 1
    
    # book_dic을 책이 팔린 횟수에 따라 내림차순으로 정렬, 같은 값을 가지는 경우 책 제목에 따라 오름차순으로 정렬
    result = sorted(book_dic.items(), key = lambda x : (-x[1], x[0]))

    # 가장 많이 팔린 책의 제목을 출력
    print(result[0][0])

    

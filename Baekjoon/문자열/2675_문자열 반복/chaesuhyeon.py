T = int(input()) # 테스트 케이스 개수
for i in range(1,T+1):
    R,S = map(str, input().split()) # 반복횟수와 문자열 입력
    R = int(R) # 반복횟수를 정수로 바꿔줌
    P = "" # 새로운 문자열 P를 빈문자열로 생성
    for s in range(len(S)): # 문자열 길이만큼 반복
        P += S[s]*R # 문자열 각 인덱스에 R만큼(반복횟수) 곱해줌
    print(P)
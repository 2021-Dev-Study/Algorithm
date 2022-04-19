# https://programmers.co.kr/learn/courses/30/lessons/60057

s = input()
answer = len(s)

for i in range(1, len(s)//2+1):  # 길이가 절반 이상이면 단위는 어차피 1개이므로
  s_unit = ''
  previous = s[0:i]
  cnt = 1

  for j in range(i, len(s), i):  # 글자수별로 단위 만들기
    temp = s[j:j+i]
    
    if previous == temp:         # 중복이면 카운트
      cnt += 1
    else:                        # 중복 아니면 새로운 글자 나오므로 기존 중복 숫자로 교체, 초기화
      # if cnt >= 2: s_unit += str(cnt) + previous
      # else: previous
      s_unit += str(cnt) + previous if cnt >= 2 else previous
      previous = temp
      cnt = 1

  s_unit += str(cnt) + previous if cnt >= 2 else previous
  answer = min(answer, len(s_unit))

print(answer)
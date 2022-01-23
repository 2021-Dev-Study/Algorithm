# 2447 : 별 찍기
# 2448과 유사, 프랙탈구조

n = int(input())
stars = ["***", "* *", "***"]

cnt = 0      # 몇 번 반복할지 계산
while n > 3:
  n //= 3
  cnt += 1

def fractal():
  length = len(stars)
  new_stars = []
  for i in range(length*3):
    # new_stars.append(stars[i%3]*3)  # 공백없이 만들어짐
                                      # *** *** ***
                                      # * * * * * *
                                      # *** *** ***
                                      # *** *** ***
                                      # * * * * * *
                                      # *** *** ***
                                      # *** *** ***
                                      # * * * * * *
                                      # *** *** ***
    if i // length == 1:
      new_stars.append(stars[i%3] + " "*length + stars[i%3])
    else:
      new_stars.append(stars[i%3]*3)
  return new_stars

for _ in range(cnt): 
  stars = fractal()   # star = new_stars > 반복

for j in stars:
  print(j)

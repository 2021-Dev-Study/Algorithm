def solution(s):
    answer = 0
    english = ['zero', 
               'one',
              'two',
              'three',
              'four',
              'five',
              'six',
              'seven',
              'eight',
              'nine']
    for idx, eng in enumerate(english):
        s = s.replace(eng, str(idx))
        
    answer = int(s)
    return answer
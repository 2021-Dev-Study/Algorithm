from collections import Counter

def solution(id_list, report, k):
    # 중복 신고 제거 과정
    report = set(report)
    # reporting: 신고한 유저
    # reported: 신고 당한 유저 (+ Counter)
    reporting_user = {reporting: [] for reporting in id_list}

    for i in report:
        reporting, reported = i.split()
        reporting_user[reporting].append(reported)

    reported_user = Counter([user.split()[1] for user in report])

    answer = [0 for i in range(len(id_list))]
    for idx, user in enumerate(id_list):
        for reported in reporting_user[user]:
            if reported_user[reported] >= k:
                answer[idx] += 1

    return answer

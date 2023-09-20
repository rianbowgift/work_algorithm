def solution(my_string):
    answer = ''


    a = my_string


    for i in a:
        if ord(i)<96:
            answer+= i.lower()
        else:
            answer+= i.upper()

    return answer


sBJ_
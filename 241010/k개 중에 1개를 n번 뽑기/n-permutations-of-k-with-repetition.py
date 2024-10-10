k, n = map(int, input().split())

answer = []
def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(curr_num):
    if curr_num == n+1:
        print_answer()
        return

    answer.append(1)
    choose(curr_num + 1)
    answer.pop()

    answer.append(2)
    choose(curr_num + 1)
    answer.pop()
    return

choose(1)
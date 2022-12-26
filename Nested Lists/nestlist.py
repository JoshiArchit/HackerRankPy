if __name__ == '__main__':
    student = list()
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     student.append([name, score])
    student = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
    min_score = min(item[1] for item in student)
    second_min = min(item[1] for item in student if item[1] != min_score)

    for item in sorted(student):
        if item[1] == second_min:
            print(item[0])

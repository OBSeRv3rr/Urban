def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


def insertion_sort(ls):
    for i in range(1, len(ls)):
        j = i
        while j > 0 and ls[j] < ls[j - 1]:
            ls[j], ls[j - 1] = ls[j - 1], ls[j]
            j -= 1

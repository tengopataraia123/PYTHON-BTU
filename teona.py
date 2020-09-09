numbers = []
string = []


def nums_or_str(k):
    for aline in k:
        values = aline
        for i in values:
            for numorstr in i:
                if numorstr.isdigit():
                    f = open("nums.txt", "a")
                    f.write(numorstr)
                    numbers.append(int(numorstr))
                    k = sum(list(numbers))
                    f.close()

                else:
                    m = open("str.txt", "a")
                    m.write(numorstr)
                    string.append(numorstr)
    print("string tipis raodenoba: ", len(string))
    print("ricxvebis jami: ", k)

    return numbers,string


def main():
    n = open('numstr.txt', "r")
    nums_or_str(n)


main()

res = []

for i in range(50):
    fh = open(f'wyniki_czas/inst{i}_results.txt')
    x = fh.read()
    # print(x)
    fh.close()

    # print(x)
    for line in x:
        print(line)
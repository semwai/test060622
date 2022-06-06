import parser as p


if __name__ == '__main__':
    filename = '../result.txt'
    p.write(filename)
    text = p.read(filename)
    output = p.filter(text)
    n = p.names(output)
    for s in n[:-1]:
        print(s, end=', ')
    print(n[-1])

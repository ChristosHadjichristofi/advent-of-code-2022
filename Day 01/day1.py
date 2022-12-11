from audioop import reverse


def main():
    with open('in.txt', 'r') as f:
        arr = list(map(sum, [list(map(int, l.split("\n"))) for l in f.read().rstrip("\n").split("\n\n")]))
    
    print(max(arr))
    arr.sort(reverse=True)
    print(sum(arr[0:3]))

if __name__ == "__main__":
    main()
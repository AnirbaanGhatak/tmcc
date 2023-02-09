from collections import deque

def power_of_2(arr):
    return [2 ** i for i in arr]

def main():
    n = int(input().strip())
    azl = [list(map(int, input().strip().split()))]
    k = int(input().strip())

    f = azl[:k]
    print(f)

    azl = azl[k:]
    print(azl)

    test = deque(f)
    test.rotate((-len(f)+1))
    f = list(test)
    print(f)

    z = azl[1:]
    test = deque(z)
    test.rotate((-len(z)+1))
    z = list(test)

    print(z)

    azl = azl[0]
    
    azl.append(f)
    azl.append(z)

    print(azl)

    # arr = rotate_array(arr, k, n)
    azl = power_of_2(azl)
    print(azl)

if __name__ == '__main__':
    main()
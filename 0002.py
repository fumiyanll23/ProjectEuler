def fibonacchi(n: int) -> int:
    return round((((1+5**0.5)/2)**n-((1-5**0.5)/2)**n) / 5**0.5)


def main():
    # input
    n = 4 * 10**6

    # compute
    ans = 0
    i = 2
    while True:
        tmp_fib = fibonacchi(i)
        if tmp_fib <= n:
            if tmp_fib%2==0:
                ans += tmp_fib
        else:
            break
        i += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()

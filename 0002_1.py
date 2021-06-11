def fibonacchi(n: int) -> int:
    return round((((1+5**0.5)/2)**n-((1-5**0.5)/2)**n) / 5**0.5)


def main():
    # input
    n = 4 * 10**6

    # compute

    # output
    print(sum([fibonacchi(i) for i in range(2,100) if fibonacchi(i)<=n and fibonacchi(i)%2==0]))


if __name__ == '__main__':
    main()

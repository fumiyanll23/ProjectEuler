def main():
    # input
    n = 1000

    # compute
    ans = 0
    for i in range(n):
        if i%3==0 or i%5==0:
            ans += i

    # output
    print(ans)


if __name__ == '__main__':
    main()

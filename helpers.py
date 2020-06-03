
def facto(n):
    res = n
    if res in [0, 1]:
        return 1
    for i in range(2, n):
        res *= i
    return res

def binomial(k, n):
    return facto(n)/facto(k)/facto(n-k)


def binomial_dist(p, k, n):
    return binomial(k, n) * p**k * (1-p)**(n-k)


if __name__ == "__main__":
    print(binomial_dist(0.4, 5, 10))

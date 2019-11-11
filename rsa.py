
"""Шифрование и дешифрование по RSA.
Проектное домашнее задание по алгебре,
бакалавриат «Современное программирование»
факультета Математики и компьютерных наук СПбГУ"""

import random
import math

def fast_pow_mod(n, a, d):
    """Быстрое возведение в степень по модулю.
    
    Возвращает a^d mod n."""

    res = 1
    while d > 0:
        if d & 1:
            res = res * a % n
        a = a * a % n
        d >>= 1
    return res

def gen_small_primes(n):
    small_primes = []
    for i in range(2, n + 1):
        is_prime = 1
        for j in range(2, i):
            if i % j == 0:
                is_prime = 0
        if is_prime:
            small_primes += [i]
    return small_primes

def check_lucas_prime_number(n, primes):

    log_n = math.floor(math.log(n))

    ok = 1
    for a in range(2, log_n + 1):
        for p in primes:
            if fast_pow_mod(n, a, (n - 1) // p) == 1:
                ok = 0
        if fast_pow_mod(n, a, n - 1) != 1:
            ok = 0
        if ok:
            return a
    return 0


def gen_primes():
    """Генерация доказуемо простых на основе теста Люка.

    Возвращает кортеж (n, ps, a), где
    n — простое между 2^123 и 2^128;
    ps — список простых, на которые раскладывается n-1;
    a — число, удовлетворяющее тесту Люка."""

    min_n = 2 ** 123

    small_primes = gen_small_primes(128)

    while True:
        primes = [2] + random.sample(small_primes, k=10)

        n = 1
        for p in primes:
            n *= p

        while n <= min_n:
            n *= random.choice(primes)

        n += 1

        res = check_lucas_prime_number(n, primes)
        if res > 0:
            return (n, primes, res)


def gen_pseudoprime():
    """Генерация псевдопростых на основе теста Миллера—Рабина.

    Возвращает целое число n в диапазоне от 2^123 до 2^128,
    псевдопростое по основание не менее чем log(n) чисел."""



    pass


def rsa_gen_keys():
    """Генерация открытого и секретного ключей.

    Возвращает кортеж (n, p, q, e, d), где
    n = p*q;
    p, q — сильно псевдопростые по не менее чем log(q) основаниям;
    e — целое число, меньшее n и взаимно простое с phi(n), значением функции Эйлера от n,
    d — целое число, обратное к e по модулю phi(n)."""
    pass


def rsa_encrypt(n, e, t):
    """Шифрование по RSA.

    На входе открытый ключ n, e и сообщение t.
    Возвращает целое число, равное t^e mod n."""
    pass


def rsa_decrypt(n, d, s):
    """Дешифрование по RSA.

    На входе закрытый ключ n, d и зашифрованное сообщение s.
    Возвращает целое число, равное s^d mod n."""
    pass




def prime_factorization_pollard(n, cutoff):
    """Разложение на простые по алгоритму Полларда.

    На входе целое число n (имеющие вид p*q для некоторых простых p, q)
    и константа отсечения cutoff ~ log(n).
    Возвращает нетривиальный делитель p (или 1, если найти такой не удалось)."""
    pass

if __name__ == "__main__":
    print(gen_primes())
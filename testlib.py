import rsa
import unittest
import random

class TestRSAmodule(unittest.TestCase):
  def test_fast_pow_mod(self):
    self.assertEqual(rsa.fast_pow_mod(100, 2, 6), 64)
    self.assertEqual(rsa.fast_pow_mod(100, 1, 6), 1)
    self.assertEqual(rsa.fast_pow_mod(30, 2, 6), 4)
    self.assertEqual(rsa.fast_pow_mod(1023, 2, 10), 1)

  def test_gen_primes(self):
    self.assertEqual(rsa.gen_small_primes(128), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127])

  def test_miller_rabin_test(self):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 1000000007, 1000000009, 1791791791]
    for p in primes:
      self.assertTrue(rsa.miller_rabin_test(p))

    nprimes = [10, 20, 30, 1000, 228, 69, 111, 123, 747747, 13311331]
    for p in nprimes:
      self.assertFalse(rsa.miller_rabin_test(p))

  def test_rsa(self):
    n, p, q, e, d = rsa.rsa_gen_keys()

    m = random.randint(1, n - 1)
    em = rsa.rsa_encrypt(n, e, m)
    dm = rsa.rsa_decrypt(n, d, em)

    self.assertEqual(m, dm)

if __name__ == '__main__':
  unittest.main()
import rsa
import unittest

class TestRSAmodule(unittest.TestCase):
  def test_fast_pow_mod(self):
    self.assertEqual(rsa.fast_pow_mod(100, 2, 6), 64)
    self.assertEqual(rsa.fast_pow_mod(100, 1, 6), 1)
    self.assertEqual(rsa.fast_pow_mod(30, 2, 6), 4)
    self.assertEqual(rsa.fast_pow_mod(1023, 2, 10), 1)

  def test_gen_primes(self):
    self.assertEqual(rsa.gen_primes(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127])

if __name__ == '__main__':
  unittest.main()
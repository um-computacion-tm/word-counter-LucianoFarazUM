import unittest
from contador_palabras import count_words


class Test_Count_words(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words(""), 0)
    def test_count_words(self):
        self.assertEqual(count_words("Hola mundo"), 2)
   # def test_simple(self):
      #  result = count_words('hola')
      # self.assertEqual(result, {'hola': 1})

    #def test_doble(self):
     #   result = count_words_2("hola")
      #  self.assertEqual(result, { "holahola" :2})
    


if __name__ == '__main__':
    unittest.main()
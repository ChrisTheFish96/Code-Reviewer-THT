import unittest

from isbn_valid import isbn_validation

class TestIsbnValidation(unittest.TestCase):
    
    def test_isbn10_valid(self):
        self.assertEqual(isbn_validation('080442957X'), 'Valid')
        self.assertEqual(isbn_validation('020161622X'), 'Valid')
        self.assertEqual(isbn_validation('1593276036'), 'Valid')
        self.assertEqual(isbn_validation('048665088X'), 'Valid')
        self.assertEqual(isbn_validation('0451526538'), 'Valid')
        
    def test_isbn13_valid(self):
        self.assertEqual(isbn_validation('9780132350884'), 'Valid')
        self.assertEqual(isbn_validation('9780596009205'), 'Valid')
        self.assertEqual(isbn_validation('9780132856201'), 'Valid')
        self.assertEqual(isbn_validation('9780201896831'), 'Valid')
        self.assertEqual(isbn_validation('9781118531648'), 'Valid')
        
    def test_isbn10_with_hyphens(self):
        self.assertEqual(isbn_validation('0-8044-2957-X'), 'Valid')
        self.assertEqual(isbn_validation('04-51526-538'), 'Valid')
        self.assertEqual(isbn_validation('1-56619-909-3'), 'Valid')
        self.assertEqual(isbn_validation('15-93276-036'), 'Valid')
        self.assertEqual(isbn_validation('01-3-235-08-82'), 'Valid')
        
    def test_isbn13_with_hyphens(self):
        self.assertEqual(isbn_validation('978-0132350884'), 'Valid')
        self.assertEqual(isbn_validation('978-0596009205'), 'Valid')
        self.assertEqual(isbn_validation('97-80201835953'), 'Valid')
        self.assertEqual(isbn_validation('978-0201896831'), 'Valid')
        self.assertEqual(isbn_validation('978-1118531648'), 'Valid')
        
    def test_isbn10_with_spaces(self):
        self.assertEqual(isbn_validation('  08044 2957X  '), 'Valid')
        self.assertEqual(isbn_validation('   0 13235 088 2   '), 'Valid')
        self.assertEqual(isbn_validation(' 1 56619 909 3 '), 'Valid')
        self.assertEqual(isbn_validation('    0596  009208  '), 'Valid')
        self.assertEqual(isbn_validation('  01 323508 82  '), 'Valid')
        
    def test_isbn13_with_spaces(self):
        self.assertEqual(isbn_validation('  978 0132350884  '), 'Valid')
        self.assertEqual(isbn_validation('   978 0596009205   '), 'Valid')
        self.assertEqual(isbn_validation(' 978 0132856201 '), 'Valid')
        self.assertEqual(isbn_validation('   978 0201896831  '), 'Valid')
        self.assertEqual(isbn_validation('  978 1118531648  '), 'Valid')
        
    def test_invalid_isbn(self):
        self.assertEqual(isbn_validation(''), 'Invalid')
        self.assertEqual(isbn_validation(None), 'Invalid')
        self.assertEqual(isbn_validation('123'), 'Invalid')
        self.assertEqual(isbn_validation('12345678901234'), 'Invalid')
        self.assertEqual(isbn_validation('12345-67890'), 'Invalid')
        
if __name__ == '__main__':
    unittest.main()
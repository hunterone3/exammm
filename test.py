
import copy
import unittest

def sum(a0, d, n):
    if n == 1:
        return a0
    else:
        return a0 + (n-1) * d + sum(a0, d, n-1)

print('Сума прогресії: ') 
print (sum(1, 2, 3))

class MyTest(unittest.TestCase): 
    def test_usage1(self):
        self.assertIsNot(3, sum(1, 2, 3))   
        
        
if __name__ == "__main__":
    import xmlrunner
    print ("hello")
    runner=xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
    







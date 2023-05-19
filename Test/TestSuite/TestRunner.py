import sys
import os
from unittest import TestLoader, TestSuite, TextTestRunner

from Test.Scripts.test_Leader_Auth import Leader_Auth
from Test.Scripts.test_Leader_Home_Page import Leader_HomePage
from Test.Scripts.test_Leader_Profile_Page import Leader_ProfilePage
from Test.Scripts.test_Leader_EventsPageFilter import Leader_EventsPageFilter
from Test.Scripts.test_Leader_BoilPoints_Sort import Leader_BoilPointsPageSort
from Test.Scripts.test_Leader_UsersPage_Filter import Leader_UsersFilter

sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())


import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Leader_HomePage),
        test_loader.loadTestsFromTestCase(Leader_Auth),
        test_loader.loadTestsFromTestCase(Leader_ProfilePage),
        test_loader.loadTestsFromTestCase(Leader_EventsPageFilter),
        test_loader.loadTestsFromTestCase(Leader_BoilPointsPageSort),
        test_loader.loadTestsFromTestCase(Leader_UsersFilter),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())

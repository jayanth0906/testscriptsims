
from unittest import TestLoader, TestSuite, TextTestRunner


from add_customer import ims_Test1
from add_order import ims_Test2
from add_tub import ims_Test3
from update_tub import ims_Test4
from delete_tub import ims_Test5
from add_bottle import ims_Test6
from update_bottle import ims_Test7
from delete_bottle import ims_Test8
from ship_order import ims_Test9
from dashboard import ims_Test10


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ims_Test1),
        loader.loadTestsFromTestCase(ims_Test2),
        loader.loadTestsFromTestCase(ims_Test3),
        loader.loadTestsFromTestCase(ims_Test4),
        loader.loadTestsFromTestCase(ims_Test5),
        loader.loadTestsFromTestCase(ims_Test6),
        loader.loadTestsFromTestCase(ims_Test7),
        loader.loadTestsFromTestCase(ims_Test8),
        loader.loadTestsFromTestCase(ims_Test9),
        loader.loadTestsFromTestCase(ims_Test10),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

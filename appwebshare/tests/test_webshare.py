__author__ = 'Tomas Hartmann'

import unittest
import appwebshare.webshare as webshare
import appwebshare.views as views


class WebshareApiTests(unittest.TestCase):
    def test_login(self):
        self.assertTrue(webshare.login_to_webshare())

    def test_search(self):
        self.assertIsNotNone(webshare.search_files('test'))

    def test_link(self):
        if 'vip' not in webshare.get_link(webshare.search_files('test')):
             raise AssertionError('no vip link')

    def test_linktwice(self):
        #should not login second time it search link
        if 'vip' not in webshare.get_link(webshare.search_files('test')):
             raise AssertionError('no vip link')
        if 'vip' not in webshare.get_link(webshare.search_files('pan prstenu')):
             raise AssertionError('no vip link')



class appwebshareViewTests(unittest.TestCase):
    # TODO add views tests. selenium?
    def test_index(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

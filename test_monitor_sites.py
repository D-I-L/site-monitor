import unittest
import requests

# web sites to monitor
sites = ['http://www.chicp.org', 'http://www.chicp.org/x']


class TestSites(unittest.TestCase):

    def test_site(self):
        for site in sites:
            r = requests.get(site)
            self.assertEqual(r.status_code, 200, site+' '+str(r.status_code))
            r = requests.get(site+'/x')
            self.assertEqual(r.status_code, 404, site+' '+str(r.status_code))
            self.assertFalse("DEBUG = True" in r.content.decode("utf-8"), site+" DEBUG = True")

if __name__ == '__main__':
    unittest.main()

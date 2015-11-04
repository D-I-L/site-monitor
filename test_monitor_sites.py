import unittest
import requests

# web sites to monitor
sites = ['https://www.chicp.org']


class TestSites(unittest.TestCase):

    def test_site(self):
        for site in sites:
            r = self._get(site)
            self.assertEqual(r.status_code, 200, site+' '+str(r.status_code))
            r = self._get(site+'/x')
            self.assertEqual(r.status_code, 404, site+' '+str(r.status_code))
            self.assertFalse("DEBUG = True" in r.content.decode("utf-8"), site+" DEBUG = True")
    
    def _get(self, url):
        if url.startswith('https'):
            return requests.get(url, verify=False)
        else: 
            return requests.get(url)

if __name__ == '__main__':
    unittest.main()

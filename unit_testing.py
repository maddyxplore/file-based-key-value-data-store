import unittest,crd as data_store

class Crd_testing(unittest.TestCase):

    def test_create(self):
        d = {"up": 1 , "wb":2 , "mh":3,"ka":4,"ra":5}
        for i,j in d.items():
            self.assertEqual(data_store.create(i,j), "data created", "Error")
    
    def test_read(self):
        d = {"up": 1 , "wb":2 , "mh":3,"ka":4,"ra":5} # test for keys in data_store without time_to_live
        for i,j in d.items():
            data_store.create(i,j)
        for i,j in d.items():
            self.assertEqual(data_store.read(i), j, "Error")
        for i in d.items():
            data_store.delete(i)
        
    def test_delete(self):
        d = {"up": 1 , "wb":2 , "mh":3,"ka":4,"ra":5} # test for keys in data_store without time_to_live
        for i in d.keys():
            self.assertEqual(data_store.delete(i), "Value Deleted", "Error")

    def test_read_for_not_in_data_store(self):
        d = {"pa": 6 , "zz":7 , "xx":8,"vv":9,"yy":10}
        for i in d.keys(): # testing for the keys not in data_store
            self.assertEqual(data_store.read(i),"Error || Key is not present in data","Error")

    def test_delete_for_not_in_data_store(self):
        d = {"pa": 6 , "zz":7 , "xx":8,"vv":9,"yy":10} #test for key not in data store
        for i in d.keys():
            self.assertEqual(data_store.delete(i), "Error || Key is not present in data", "Error")

if __name__ == '__main__':
    unittest.main()

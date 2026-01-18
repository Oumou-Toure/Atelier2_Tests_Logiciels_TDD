import unittest
from laboratory import Laboratory

class TestLaboratory(unittest.TestCase):
    
    def test_quantite_substance_connue_initialisee_a_zero(self):
        substances_laboratoire = Laboratory(["farine", "sucre"])
        self.assertEqual(substances_laboratoire.getQuantity("farine"), 0.0)
        self.assertEqual(substances_laboratoire.getQuantity("sucre"), 0.0)
        
    def test_quantite_substance_inconnue(self):
        
        substances_laboratoire = Laboratory(["farine", "sucre", "levure"])
        with self.assertRaises(ValueError):
            substances_laboratoire.getQuantity("lait")
            
    def test_mauvais_type_de_données_getQuantity_error(self):
        
        substances_laboratoire = Laboratory(["farine", "sucre", "levure", "oeufs"])
        
        with self.assertRaises(TypeError):
            substances_laboratoire.getQuantity(None)
        
        with self.assertRaises(TypeError):
            substances_laboratoire.getQuantity(123)
            
    def test_getQuantity_substances_pluriels(self):
        
        lab = Laboratory(["farine", "sucre"])
        self.assertEqual(lab.getQuantity("farines"), 0.0)
        self.assertEqual(lab.getQuantity("sucres"), 0.0)

    def test_ajout_substance_connue_et_incrementation_quantite_en_stock(self):
        
        substances_laboratoire = Laboratory(["farine", "sucre", "lait"])
        substances_laboratoire.add("farine", 2.5)  
        self.assertEqual(substances_laboratoire.getQuantity("farine"), 2.5)


        
if __name__ == '__main__':
    unittest.main()
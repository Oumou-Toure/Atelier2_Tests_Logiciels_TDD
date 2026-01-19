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

    def test_ajout_substance_inconnue_en_stock(self):
        
        substances_laboratoire = Laboratory(["arome", "yaourt"])
        with self.assertRaises(ValueError):
            substances_laboratoire.add("lait", 2.0)  
            
    def test_ajout_quantite_negative(self):
        
        substances_laboratoire = Laboratory(["chocolat", "sucre", "miel"])
        with self.assertRaises(ValueError):
            substances_laboratoire.add("sucre", -2.0)

    def test_ajout_mauvais_type_de_donnees_quantite(self):
        
        substances_laboratoire = Laboratory(["farine", "sucre"])
        for q in ["deux", None, [], {}]:
            with self.assertRaises(TypeError):
                substances_laboratoire.add("farine", q)
                
    def test_initialisation_avec_reactions_ajoute_les_produits_au_stock(self):
        
        substances = ["farine", "sucre", "beurre", "levure", "arome"]
        reactions = {
            "pate à gateau": [(200, "farine"), (100, "sucre"), (50, "beurre")]
        }

        substances_laboratoire = Laboratory(substances, reactions)

        self.assertEqual(substances_laboratoire.getQuantity("pate à gateau"), 0.0)
        
        
    def test_fabriquer_reactions_avec_substances_inconnues(self):
        
        substances = ["farine"]
        reactions = {
            "pate": [(200, "sucre")] 
        }

        with self.assertRaises(ValueError):
            Laboratory(substances, reactions)
            
            
    def test_initialisation_laboratoire_sans_substances(self):
        with self.assertRaises(ValueError):
            Laboratory([])
            
    
    def test_make_produit_inconnu(self):
        
        substances_laboratoire = Laboratory(["farine", "sucre"])
        with self.assertRaises(ValueError):
            substances_laboratoire.make("pate")  





if __name__ == '__main__':
    unittest.main()
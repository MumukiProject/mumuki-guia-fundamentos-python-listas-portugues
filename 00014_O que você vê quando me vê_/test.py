
  def test_stranger_things_no_es_recomendable(self):
    self.assertTrue(serie_nao_recomendavel("Stranger things"))
    
  def test_el_marginal_no_es_recomendable(self):
    self.assertTrue(serie_nao_recomendavel("El marginal"))
    
  def test_veinticuatro_no_es_recomendable(self):
    self.assertTrue(serie_nao_recomendavel("24"))
    
  def test_breaking_bad_es_recomendable(self):
    self.assertFalse(serie_nao_recomendavel("Breaking bad"))
    
  def test_los_simpsons_es_recomendable(self):
    self.assertFalse(serie_nao_recomendavel("Los simpsons"))
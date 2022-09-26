  
  def test_transferir_move_o_3_da_primeira_lista_para_a_segunda(self):
    un_array = [1, 2, 3]
    otro_array = [4, 5]
  
    transferir(un_array, otro_array, 3)
  
    self.assertEqual(un_array, [1, 2])
    self.assertEqual(otro_array, [4, 5, 3])
  
  def test_trasferir_move_o_8_da_primeira_lista_para_a_segunda(self):
    un_array = [9, 8, 7]
    otro_array = [4, 5]
  
    transferir(un_array, otro_array, 7)
  
    self.assertEqual(un_array, [9, 8])
    self.assertEqual(otro_array, [4, 5, 7])
  

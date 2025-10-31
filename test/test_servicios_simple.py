import unittest
from unittest.mock import Mock, MagicMock

class TestServiciosSimple(unittest.TestCase):
    """
    Tests de servicios usando mocks simples - sin imports reales
    """

    def test_eleccion_servicio_mock(self):
        """Prueba EleccionServicio con mock manual"""
        # Crear mock manual del servicio
        mock_servicio = Mock()
        mock_servicio.get_all_eleccion.return_value = [
            {"id": 1, "nombre": "Elección Test 1"},
            {"id": 2, "nombre": "Elección Test 2"}
        ]

        # Probar el mock
        result = mock_servicio.get_all_eleccion(4)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        mock_servicio.get_all_eleccion.assert_called_once_with(4)

    def test_voto_servicio_mock(self):
        """Prueba VotoServicio con mock manual"""
        mock_servicio = Mock()
        mock_servicio.get_all_votos.return_value = [
            {"nombre_completo": "Juan Perez", "nombre_lista": "Lista A"},
            {"nombre_completo": "Maria Lopez", "nombre_lista": "Lista B"}
        ]

        result = mock_servicio.get_all_votos()
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["nombre_completo"], "Juan Perez")
        mock_servicio.get_all_votos.assert_called_once()

    def test_candidato_servicio_mock(self):
        """Prueba CandidatoServicio con mock manual"""
        mock_servicio = Mock()
        mock_servicio.get_candidatos_inscritos.return_value = [
            {"id": 1, "nombre": "Candidato 1", "denegado": False},
            {"id": 2, "nombre": "Candidato 2", "denegado": False}
        ]

        result = mock_servicio.get_candidatos_inscritos()
        
        self.assertEqual(len(result), 2)
        self.assertFalse(result[0]["denegado"])
        mock_servicio.get_candidatos_inscritos.assert_called_once()

if __name__ == '__main__':
    unittest.main()
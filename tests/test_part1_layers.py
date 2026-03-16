
from layers.repository import InMemoryUserRepository
from layers.service import UserService
from layers.controller import UserController

def test_controller_service_repository_integration():
    repo = InMemoryUserRepository()
    service = UserService(repo)
    controller = UserController(service)

    assert controller.get_user_full_name(1) == "Ada Lovelace"
    assert controller.get_user_full_name(2) == "Alan Turing"
    assert controller.get_user_full_name(3) == "Grace Hopper"
    assert controller.get_user_full_name(999) == "404 NOT_FOUND"

    """
    Si cambias el formato de salida del controlador, ¿qué otras capas tendrías que adaptar?

    No habría que cambiar otras capas porque es la capa que no se envía como
    parámetro a otras capas (es la capa más externa). Habría que cambiar los asserts
    de la prueba.
    """

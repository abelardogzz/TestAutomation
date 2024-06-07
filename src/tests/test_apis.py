import pytest
import requests

RSC = [
    pytest.param("type", "1", id="Test 1"),
    pytest.param("pokemon", "1", id="Test 2")]


class TestApis:
    POKE_API = "https://pokeapi.co/api/v2/"

    @pytest.mark.parametrize("route, value", RSC)
    def test_pokemon(self, route, value):
        resp = requests.get(self.POKE_API, params=route + "/" + value)

        print("response", resp)

        assert resp.status_code == 200

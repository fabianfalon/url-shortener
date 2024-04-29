from expects import be, expect, equal
from fastapi.testclient import TestClient
from starlette import status
from src.main import app


class TestApi:
    client = TestClient(app)


class TestCoursesApi(TestApi):

    def test_create_short_url(self, mock_create_short_url_use_case):
        data = {"url": "https://probando.com/121323"}
        response = self.client.post("/shortener", json=data)
        expect(response.status_code).to(be(status.HTTP_200_OK))

    def test_get_original_url(self, mock_create_short_url_use_case, mock_get_original_url_use_case):
        data = {"url": "https://probando.com/121323"}
        self.client.post("/shortener", json=data)

        response = self.client.get("/6b86b273")
        expect(response.json()).to(equal({"url": "https://probando.com/121323"}))
        expect(response.status_code).to(be(status.HTTP_302_FOUND))

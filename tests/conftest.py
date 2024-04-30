import pytest


@pytest.fixture
def mock_create_short_url_use_case(mocker):
    short_url = "6b86b273"
    mocker.patch("src.use_case.url_shortener.CreateShortUrlUseCase.execute", return_value=short_url)
    return short_url


@pytest.fixture
def mock_get_original_url_use_case(mocker):
    original_url = "https://probando.com/121323"
    mocker.patch("src.use_case.get_original_url.GetOriginalUrlUseCase.execute", return_value=original_url)
    return original_url

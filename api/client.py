import allure
import requests
import config


class DiskClient:
    def __init__(self, base_url: str, token: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"OAuth {token}",
            "Accept": "application/json",
        })

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"

        with allure.step(f"{method} {endpoint}"):
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            self._attach_request(response.request)
            self._attach_response(response)

        return response
    @staticmethod
    def _attach_request(request) -> None:
        allure.attach(
            f"{request.method} {request.url}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT,
        )

        if request.body is None:
            return

        body = request.body
        if isinstance(body, bytes):
            body = body.decode("utf-8", errors="replace")

        allure.attach(
            body,
            name="Request body",
            attachment_type=allure.attachment_type.JSON,
        )

    @staticmethod
    def _attach_response(response) -> None:
        if not response.text:
            allure.attach(
                f"{response.status_code} (empty body)",
                name="Response",
                attachment_type=allure.attachment_type.TEXT,
            )
            return

        allure.attach(
            response.text,
            name=f"Response {response.status_code}",
            attachment_type=allure.attachment_type.JSON,
        )

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("DELETE", endpoint, **kwargs)


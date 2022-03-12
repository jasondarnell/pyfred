
import json
from http import HTTPStatus

from requests.models import Response


MOCK_CATEGORY_CHILDREN_RESP = {'categories': [{'id': 32991, 'name': 'Money, Banking, & Finance', 'parent_id': 0}, {'id': 10, 'name': 'Population, Employment, & Labor Markets', 'parent_id': 0}, {'id': 32992, 'name': 'National Accounts', 'parent_id': 0}, {'id': 1, 'name': 'Production & Business Activity', 'parent_id': 0}, {'id': 32455, 'name': 'Prices', 'parent_id': 0}, {'id': 32263, 'name': 'International Data', 'parent_id': 0}, {'id': 3008, 'name': 'U.S. Regional Data', 'parent_id': 0}, {'id': 33060, 'name': 'Academic Data', 'parent_id': 0}]}


MOCK_RESPONSES = {
    "/category/children": MOCK_CATEGORY_CHILDREN_RESP
}


def get_mock_response(*args, **kwargs):
    url = args[0]
    path = url.split("?")[0].split("fred")[-1]
    print(path)
    if path not in MOCK_RESPONSES:
        raise RuntimeError(f"Unhandled path: {path}")
    content = MOCK_RESPONSES[path]
    r = Response()
    r.status_code = HTTPStatus.OK
    r._content = str.encode(json.dumps(content))
    return r

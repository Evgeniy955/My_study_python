import pytest
import os


@pytest.fixture()
def rounding_result():
    os.environ['rounding'] = '3'
    round_result = os.environ.get('rounding')
#   round_result = os.getenv("rounding")
    return round_result



# def pytest_addoption(parser):
#     parser.addoption(
#         "--rounding_index", action="store", default=3,
#         help='Enter rounding precision')
#
# @pytest.fixture()
# def rounding_result(request):
#     return request.config.getoption("--rounding_index")

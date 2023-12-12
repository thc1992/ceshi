import pytest, allure
import os


@allure.feature('测试用例功能') 
class Test_Class(object):

    @pytest.fixture(scope='function')
    def setup_function(request):
        def teardown_function():
            print("teardown_function called.")

        request.addfinalizer(teardown_function)
        print('setup_function called.')

    @pytest.fixture(scope='module')
    def setup_module(request):
        def teardown_module():
            print("teardown_module called.")
        request.addfinalizer(teardown_module)
        print('setup_module called.')

    @allure.story('11111111111111111111')  
    @pytest.mark.website
    def test_1(setup_function):
        print('Test_1 called.')

    @allure.story('22222222222222') 
    def test_2(setup_module):
        print('Test_2 called.')

    @allure.story('333333333333333333333') 
    def test_3(setup_module):
        print('Test_3 called.')
        assert 2== 1 + 1



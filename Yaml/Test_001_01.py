import pytest, allure


class Test_abc:
    '''
    step：加标题
    attach:加文本，和文本内容
    使用方式：添加测试级别
        @allure.severity(allure.severity_level.CRITICAL）

      Severity：严重级别(BLOCKER,CRITICAL,NORMAL,MINOR,TRIVIAL)
      @allure.testcase() 跳转到问题路径
      @allure.issue("") 跳转到bug地址

      allure generate report / -o report/html  将json执行成html文件

    '''

    @allure.step(title='第一个测试')
    @allure.testcase('https:www.baidu.com')

    @allure.severity(allure.severity_level.BLOCKER)
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_01(self):
        allure.attach('这是一个描述', '测试下')
        assert 1


if __name__ == '__main__':
    pytest.main('-s --alluredir  report Test_001_01.py')

from selenium import webdriver

driver = webdriver.Chrome()


def parse(ref, i):
    driver.get(ref)
    count = i + 1
    element_name = driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/div[3]/div[4]/div[1]/div[1]/section/article/table/tbody/tr[' + str(count) + ']/td[2]')
    element_name_value = element_name.get_attribute('data-value')
    element_wr = driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/div[3]/div[4]/div[1]/div[1]/section/article/table/tbody/tr[' + str(count) + ']/td[4]')
    element_wr_value = element_wr.get_attribute('data-value')
    return str(
        element_name_value) + u'\u043f\u0440\u043e\u0438\u0433\u0440\u044b\u0432\u0430\u0435\u0442 ' \
                              u'\u0432\u0441\u0435\u0433\u043e \u0432 ' + str(
        round(float(element_wr_value))) + u' \u0438\u0433\u0440\u0430\u0445 \u0438\u0437 100'

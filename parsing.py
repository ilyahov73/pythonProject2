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
    return str(element_name_value) + ' проигрывает всего в ' + str(round(float(element_wr_value))) + ' играх из 100'

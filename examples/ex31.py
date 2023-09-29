from selenium import webdriver
from selenium.webdriver.common.by import By
if __name__ == '__main__':
    d1 = webdriver.Chrome()
    d1.implicitly_wait(10)

    d1.get('https://vinod.co')
    print(d1.title)

    elem1 = d1.find_element(By.TAG_NAME, 'H3')
    print(elem1.text)

    h5elems = d1.find_elements(By.XPATH, '//h5')
    print(f'there are {len(h5elems)} H5 elements in the website.')
    print('The text values of each one of them are:')
    for h5elem in h5elems:
        print(f'{h5elem.text}')

    print('-' * 50)

    link = d1.find_element(By.XPATH, '//a[@href="/posts/logging-in-java"]')
    link.click()
    elem1 = d1.find_element(By.TAG_NAME, 'H2')
    print(elem1.text)

    d1.close()

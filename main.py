from data import address_from, address_to, card_number, card_code, message_for_driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')


    ask_taxi_button = (By.CLASS_NAME, 'button round')
    comfort_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    phone_number_container = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    close_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/button')
    payment_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_placeholder = (By.XPATH, '//*[@id="number"]')
    code_placeholder = (By.XPATH, '//*[@id="code"]')
    add_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    payment_close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    comment_to_driver = (By.ID, 'comment')
    blanket_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
#Exploración de otro tipo de selector
    ice_cream_counter_plus = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    intro_code_chart = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/label')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    confirmation_service_button = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button > span.smart-button-secondary')


    def __init__(self, driver): #Constructor de clase
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('address_from')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('address_to')


    def click_ask_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ask_taxi_button))
        self.driver.find_element(*self.ask_taxi_button).click()

    def click_comfort_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.comfort_button))
        self.driver.find_element(*self.comfort_button).click()

    def click_payment_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.payment_button))
        self.driver.find_element(*self.payment_button).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.add_card_button))
        self.driver.find_element(*self.add_card_button).click()

    def click_card_placeholder(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.card_placeholder))
        self.driver.find_element(*self.card_placeholder).click()

    def set_card_placeholder(self, card_placeholder):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.card_placeholder))
        self.driver.find_element(*self.card_placeholder).send_keys('card_number')

    def click_code_placeholder(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.code_placeholder))
        self.driver.find_element(*self.code_placeholder).click()

    def set_code_placeholder(self, code_placeholder):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.code_placeholder))
        self.driver.find_element(*self.code_placeholder).send.keys('card_code')
        self.driver.find_element(*self.card_placeholder).click()

    def click_add_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.add_button))
        self.driver.find_element(*self.add_button).click()

    def click_payment_close_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.payment_close_button))
        self.driver.find_element(*self.payment_close_button).click()

    def add_comment_to_driver(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.comment_to_driver))
        self.driver.find_element(*self.comment_to_driver).send_keys('message for driver')

    def click_blanket_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.blanket_button))
        self.driver.find_element(*self.blanket_button).click()

    def click_ice_cream_counter_plus(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ice_cream_counter_plus))
        self.driver.find_element(*self.ice_cream_counter_plus).click()
        self.driver.find_element(*self.ice_cream_counter_plus).click()

    def click_phone_number_container(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.phone_number_container))
        self.driver.find_element(*self.phone_number_container).click()

    def set_phone_number_field(self, phone_number_field):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).send_keys('phone_number')

    def click_next_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.next_button))
        self.driver.find_element(*self.next_button).click()

    def click_intro_code_chart(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.intro_code_chart))
        self.driver.find_element(*self.intro_code_chart).click()

    def click_confirm_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.confirm_button))
        self.driver.find_element(*self.confirm_button).click()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

#Modificaciones después de la primera entrega

    def test_select_plan(self):
        rate_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        rate_page.click_ask_taxi_button()
        rate_page.click_comfort_button()
        assert rate_page.get_blanket_button() == 'Manta y pañuelos'

    def test_fill_phone_number(self):
        form_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        form_page.click_phone_number_container()
        phone_number = data.phone_number
        form_page.filling_phone_number_field(phone_number)
        assert form_page.get_phone() == phone_number

    def test_fill_card_(self):
        card_form = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        card_form.click_payment_button()
        card_form.click_add_card_button()
        card_data = data.card_number
        code_data = data.card_code
        card_form.filling_card_placeholder(card_data)
        card_form.filling_code_placeholder(code_data)
        assert card_form.get_card_number() == card_number
        assert card_form.get_code_number() == code_data
        card_form.click_add_button()
        card_form.click_payment_close_button()

    def test_comment_for_driver(self):
        comment_form = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        comment = data.message_for_driver
        comment_form.add_comment_to_driver(comment)
        assert comment_form.get_comment_to_driver() == comment

    def test_blanket_and_handkerchiefs(self):
        requests_form = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        requests_form.click_blanket_button()
        assert requests_form.blanket_button.is_selected() == True

    def test_order_2_ice_creams(self):
        requests_form = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        requests_form.add_ice_cream_counter_plus()
        assert requests_form.get_ice_cream_counter_plus_value() == 2

    def test_car_search_model_appears(self):
        service_confirm = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        service_confirm.click_confirmation_service_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

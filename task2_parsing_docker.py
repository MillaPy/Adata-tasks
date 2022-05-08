import os, platform
from pathlib import Path
import pandas as pd
from selenium import webdriver
from pyvirtualdisplay import Display
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

class NotProperlyParsed(Exception):
    """
    Exception raised for incorrect parsing of organizations information
    """
    def __init__(self, number_in_interface, number_in_dataframe):
        self.number_in_interface = number_in_interface
        self.number_in_dataframe = number_in_dataframe
        self.message = f'Number of Organisations in interface ({self.number_in_interface}) ' \
                       f'is not equal to Number of parsed Organisations ({self.number_in_dataframe})'
        super().__init__(self.message)

class GosZakup():
    def __init__(self, download_folder=''):
        # simple init nothing serious is needed here
        self.driver = None
        self.download_folder = download_folder
        self.executable_path = '/usr/bin/chromedriver'

    def driver_innit(self):
        print("\nExpecting connection ---")
        # initialize driver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        try:
            if platform.system() in ('Darwin', 'Windows'):
                self.driver = webdriver.Chrome(self.executable_path, options=chrome_options)
                print("headless regime is activated ---")
            else:
                display = Display(visible=False, size=(1024, 768))
                display.start()
                self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',
                                                service_args=['--verbose', '--log-path=/home/snc/mylogs/chromedriver.log'])
                print('chrome will not be displayed ---')

            print("headless regime is activated ---")
        except WebDriverException:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options= chrome_options)
        print("Got connected - waiting for URL ---")
        self.driver.implicitly_wait(10)

    def geting_in_webpage(self):
        # prepare url and innitialise driver for driver to get
        if not self.driver:
            self.driver_innit()
        print('driver has started ---')

        # get url ready
        export_url = 'https://www.goszakup.gov.kz/ru/registry/rqc'
        try:
            self.driver.get(export_url)
            print('We got into webpage ---')

            # if some has problems of not secure webpage throe try and exception
            try:
                # find button to advanced settings
                advnaced_btn = self.driver.find_element_by_xpath('//*[@id="details-button"]')
                advnaced_btn.click()
                # click on manually proceed link
                manually_proceed = self.driver.find_element_by_xpath('//*[@id="proceed-link"]')
                manually_proceed.click()
            except NoSuchElementException:
                print('There is non such elements on the page.')
                pass
            print('Welcome to the GosZakup pages!')

            # after getting in show immediately all possible records
            select_all_records = '/html/body/main/div[4]/div[2]/div[3]/div[3]/div[4]/div/div[3]/div/div/select/option[9]'
            self.driver.find_element_by_xpath(select_all_records).click()
            print('2000 records are now shown ---')
        except TimeoutException:
            print("Error - system timed out")
        except WebDriverException:
            print("Error with connection and system timed out")

    def scroll_shim(self, element):
        # get x and y axis value of any element on page
        x = element.location['x']
        y = element.location['y']

        # scroll down by x and y axis of element
        scroll_by_coord = f'window.scrollTo({x},{y});'
        # navigate by such axises
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'

        # execute such actions by driver on page
        self.driver.execute_script(scroll_by_coord)
        # to to the top of page
        self.driver.execute_script(scroll_nav_out_of_way)

    @staticmethod
    def prepare_df(data):
        # gte columns and dtypes ready
        columns = ['Наименование потенциального поставщика', 'БИН/ИИН', 'ФИО руководителя', 'ИИН руководителя',
                   'Полный адрес']
        dtypes = {'Наименование потенциального поставщика': 'object', 'БИН/ИИН': 'object', 'ФИО руководителя': 'object',
                  'ИИН руководителя': 'object', 'Полный адрес': 'object'}
        # create df with column names and dtypes
        df = pd.DataFrame(data, columns=columns)
        df = df.astype(dtypes)
        return df

    @staticmethod
    def transform_df(df):
        subset = 'Наименование потенциального поставщика'
        # sorting by first name
        df.sort_values(subset, inplace=True)
        # dropping ALL duplicate values
        df.drop_duplicates(subset=subset, keep=False, inplace=True)
        # parse to excel file what is in df
        df.to_excel("Реестр квалифицированных поставщиков.xlsx")
        print('New excel file ahs been downloaded ---')
        return df

    def get_org_info(self):
        # obtain window handle of browser in focus
        p = self.driver.current_window_handle
        # obtain parent window handle
        parent = self.driver.window_handles[0]
        # obtain browser tab window
        chld = self.driver.window_handles[1]
        # switch to new browser tab
        self.driver.switch_to.window(chld)

        # get current url
        current_url = self.driver.current_url
        # get id of current url
        get_id = current_url.split('/')[-1]
        # get new url - actually not needed process
        new_url = f'https://www.goszakup.gov.kz/ru/registry/show_supplier/{get_id}'
        # swithc to new url with driver
        self.driver.get(new_url)
        print('We got new active tab ---')

        # create lists where data will be saved
        fullname_head = []
        iin_head = []
        address = []
        name_org = []
        biin = []

        organizations = []

        # find needed elements xpath on web table
        table_org_xpath = '//*[@id="main-wrapper"]/div[3]/div[3]/div[2]/div/table/tbody/tr'

        org_name_xpath = table_org_xpath + '[8]/td'
        org_biin_xpath = table_org_xpath + '[5]/td'

        table_org_head_xpath = '//*[@id="main-wrapper"]/div[3]/div[3]/div[4]/div[2]/table/tbody/tr'

        org_head_name_xpath =  table_org_head_xpath + '[3]/td'
        org_head_biin_xpath = table_org_head_xpath + '[1]/td'

        org_address_xpath = '//*[@id="main-wrapper"]/div[3]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td[3]'

        # after finding all elements add them to list
        name_org.append(self.driver.find_element_by_xpath(org_name_xpath).text)
        biin.append(self.driver.find_element_by_xpath(org_biin_xpath).text)
        # as well other details that needed to be added
        fullname_head.append(self.driver.find_element_by_xpath(org_head_name_xpath).text)
        iin_head.append(self.driver.find_element_by_xpath(org_head_biin_xpath).text)
        address.append(self.driver.find_element_by_xpath(org_address_xpath).text)
        print('New details about organisations have been saved ---')

        # save all details in one list
        organizations.append(name_org + biin + fullname_head + iin_head + address)
        print('Organisation of one instance has been saved --')

        # close child browser tab window
        self.driver.close()
        # switch back to parent window
        self.driver.switch_to.window(parent)
        print('We have switched back to parent page ---')
        # check window name just in case
        print("Page title for current window:")
        print(self.driver.title)

        return organizations

    def get_org_records(self):
        try:
            # start driver and get url
            self.geting_in_webpage()
            # find elements on web table
            table_xpath = '//*[@id="main-wrapper"]/div[3]/div[3]/div[3]/div/table/tbody/tr'
            # get to the top of table after getting all records
            self.scroll_shim(self.driver.find_element_by_xpath(table_xpath))
            # get the length of table
            number_of_orgs = len(self.driver.find_elements_by_xpath(table_xpath)) - 1
            link_xpath = '//*[@id="main-wrapper"]/div[3]/div[3]/div[3]/div/table/tbody/tr[{}]/td[2]/a'

            # innit new list where data will be saved
            organizations = []

            # go through all elements in table body to register each detail
            try:
                for i in range(1, number_of_orgs):
                    # click on the link
                    self.driver.find_element_by_xpath(link_xpath.format(i)).click()
                    print('You are on details page!')
                    # get information in new url
                    organisations_details = self.get_org_info()
                    # save them in a list
                    organizations.extend(organisations_details)
                    # show what we have added
                    print(f'---{i}/{number_of_orgs} organisations_details added---')
                    # self.driver.execute_script('window.history.go(-1)')
            # throw exception when page is not loaded yet or too many requests are send, and captcha are shown
            except NoSuchElementException:
                print("Could not find such element---")
            # when captcha is shown or page is not loaded just throw out
            except TimeoutException:
                print("Timed out waiting for page to load---")

            # transfer list into df
            orgs_df = self.prepare_df(organizations)
            print('We got organisation details into df ---')

            # check if saved number of records are correct - find web table
            xpath = '//*[@id="main-wrapper"]/div[3]/div[3]/div[3]/div/table'
            html = self.driver.find_element_by_xpath(xpath).get_attribute('outerHTML')
            real_table = pd.read_html(html)[0]

            # find number of records in web and df
            subset = 'БИН/ИИН'
            number_in_interface = real_table[['Наименование потенциального поставщика', 'БИН/ИИН']].drop_duplicates()[subset].nunique()
            number_in_dataframe = orgs_df[['Наименование потенциального поставщика', 'БИН/ИИН']].drop_duplicates()[subset].nunique()

            # check if there are correct
            if number_in_interface != number_in_dataframe:
                raise NotProperlyParsed(number_in_interface, number_in_dataframe)

            # save as excel and remove duplicates by names
            # if only collection length on both interface and df are correct then save as excel
            orgs_excel = self.transform_df(orgs_df)
            print('We have downloaded newly created excel file ---')

            # either way return newly created df for other transformations
            return orgs_df
        except NoSuchElementException:
            print('Error with connection - please, try later.')


if __name__ == '__main__':
    # initialize download folder and driver path
    home = str(Path.home())
    download_folder = os.path.join(home, "Downloads")

    # create object of class
    gk = GosZakup()
    gk.__init__(download_folder)
    orgs_df = gk.get_org_records()






from selene import browser
from selene import be, have
import os


def test_fill_check_practice_form():

    # Should fill elements
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Barashka')
    browser.element('#userEmail').type("abarashka@gmail.com")
    browser.element('[value="Male"]').with_(click_by_js=True).click()
    browser.element('#userNumber').type("1234567890")
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class*="react-datepicker__day--013"]').click()
    browser.element('[id="subjectsInput"]').type("English").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/resources/chatgpt_logo.png')
    browser.element('[placeholder="Current Address"]').type("Tbilisi")
    browser.element('#state').click()
    browser.element('#state #react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#city #react-select-4-option-0').click()
    browser.element('#submit').click()

    # Should check elements
    browser.element(".modal-content").should(be.visible)
    success_message = '.modal-header'
    assert success_message == "Thanks for submitting the form"

    browser.all('.table-responsive .table tbody > tr')[0].should(have.text('Alex Barashka'))
    browser.all('.table-responsive .table tbody > tr')[1].should(have.text('abarashka@gmail.com'))
    browser.all('.table-responsive .table tbody > tr')[2].should(have.text('Male'))
    browser.all('.table-responsive .table tbody > tr')[3].should(have.text('1234567890'))
    browser.all('.table-responsive .table tbody > tr')[5].should(have.text('Physics'))
    browser.all('.table-responsive .table tbody > tr')[6].should(have.text('Sports'))
    browser.all('.table-responsive .table tbody > tr')[7].should(have.text('chatgpt_logo.png'))
    browser.all('.table-responsive .table tbody > tr')[8].should(have.text('Tbilisi'))
    browser.all('.table-responsive .table tbody > tr')[9].should(have.text('NCR Delhi'))

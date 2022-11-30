from behave import *
from common import PayGradesTest

global test

@given('we have the driver initialized')
def step_impl(context):
    global test
    test = PayGradesTest()


@when('we login successfully')
def step_impl(context):
    test.login_page()


@when('we go to the Pay Grades panel')
def step_impl(context):
    test.main_page()


@when('we add a new record')
def step_impl(context):
    test.pay_grades_page()


@then('we can see the record appeared')
def step_impl(context):
    test.check_record()


@then('we delete the record')
def step_impl(context):
    test.remove_record_check()
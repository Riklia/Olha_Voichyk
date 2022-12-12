from behave import *
from common import DropboxTest

global test


@given('we are authenticated on Dropbox')
def step_impl(context):
    global test
    test = DropboxTest()


@when('we upload a file to Dropbox')
def step_impl(context):
    context.response = test.upload_file()


@then('the file is successfully uploaded')
def step_impl(context):
    assert context.response.status_code == 200


@when('we retrieve the metadata of the file')
def step_impl(context):
    context.response = test.get_file_metadata()


@then('we get the metadata')
def step_impl(context):
    assert context.response.status_code == 200


@when('we delete the file from Dropbox')
def step_impl(context):
    context.response = test.delete_file()


@then('the file is successfully deleted')
def step_imp(context):
    assert context.response.status_code == 200

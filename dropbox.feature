Feature: Using Dropbox storage
  Scenario: We have an access to storage on Dropbox
    Given we are authenticated on Dropbox
    When we upload a file to Dropbox
    Then the file is successfully uploaded
    When we retrieve the metadata of the file
    Then we get the metadata
    When we delete the file from Dropbox
    Then the file is successfully deleted

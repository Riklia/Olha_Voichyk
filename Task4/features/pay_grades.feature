Feature: Pay grades test on OrangeHRM
  Scenario: Pay grades system works
    Given we have the driver initialized
    When we login successfully
    And we go to the Pay Grades panel
    And we add a new record
    Then we can see the record appeared
    And we delete the record

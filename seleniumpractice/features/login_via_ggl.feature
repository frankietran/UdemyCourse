@fixture.driver.chrome
Feature: log in via Google
  A user should be able to log in using Google account
  and post a problem

  Scenario: log in via Google successfully
    Given user is at landing page
    When user clicks login button
    Then user sees login modal
    When user clicks google icon in login modal
    Then user sees a new authentication window
    When user switches to the new window
    And user fills in correct email and password
    And user switches back to the main window
    Then user is at home page
    When user posts a problem
    Then user sees choose package modal

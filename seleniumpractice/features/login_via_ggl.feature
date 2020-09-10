@fixture.browser.chrome
Feature: a user can log in via Google and post a problem

  Scenario: log in via Google successfully and post a problem
    Given user is on landing page
    When user clicks login button on landing page
    Then user sees login modal
    When user clicks Google icon in login modal
    Then user sees a new window
    When user switches to the Google authentication window
    And user successfully follows through Google authentication process in Google authentication window
    And user switches back to the main window
    Then user is on home page
    When user enters problem description and uploads a problem file on home page and submits the problem
    Then user sees choose package modal

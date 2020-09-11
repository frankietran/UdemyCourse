Feature: As a user, I can log in via Google and post a problem

  Background: I can see login modal on landing page
    Given I am on landing page
    When I click login button on landing page
    Then I should see login modal

  @fixture.browser.chrome
  Scenario: I log in via Google successfully and post a problem
    Given I click Google icon in login modal
    When a new Google authentication window pops up
    Then I should be able to switch to the Google authentication window
    Given I successfully follow through Google authentication process in Google authentication window
    When I switch back to the main window
    Then I should be on home page
    When I enter problem description on home page
    And upload a problem file
    And submit the problem
    Then I should see choose package modal

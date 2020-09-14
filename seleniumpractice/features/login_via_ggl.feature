Feature: As a user, I can log in via Google and post a problem

  @fixture.browser.chrome
  Scenario Outline: I log in via Google successfully and post a problem
    Given I am on landing page of "<page_type>"
    When I click login button on landing page of "<page_type>"
    Then I should see login modal
    Given I click Google icon in login modal
    When a new Google authentication window pops up
    Then I should be able to switch to the Google authentication window
    Given I successfully follow through Google authentication process in Google authentication window
    When I switch back to the main window
    Then I should be on home page of "<page_type>"
    When I enter problem description on home page of "<page_type>"
    And upload a problem file on home page of "<page_type>"
    And submit the problem on home page of "<page_type>"
    Then I should see expert matching modal
    Examples:
      | page_type          |
      | ASKER_PORTAL       |
      | MS_LANDING         |
      #| MS_SUPPORT_LANDING |
      # LEARNER_PORTAL     |
      #| BYO_LEARNER_PORTAL |
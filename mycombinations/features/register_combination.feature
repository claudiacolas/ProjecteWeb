Feature: Register Combination
  In order to keep track of the combinations I try
  As a user
  I want to register a combination together with its mix and alcohol details

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just combination name
    Given I login as user "user" with password "password"
    When I register combination
      | name    |
      | RumCola |
    Then I'm viewing the details page for combination by "user"
      | name     |
      | RumCola  |
    And There are 1 combinations

  Scenario: Try to register combination but not logged in
    Given I'm not logged in
    When I register combination
      | name     |
      | RumCola  |
    Then I'm redirected to the login form
    And There are 0 combination

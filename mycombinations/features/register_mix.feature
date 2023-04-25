Feature: Register Mix
    In order to keep track of the mixes I try
    As a user
    I want to register a mix together with its brand details

 Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just mix name
    Given I login as user "user" with password "password"
    When I register mix
      | name        |
      | Coca-Cola   |
    Then I'm viewing the details page for mix by "user"
      | name        |
      | Coca-Cola   |
    And There are 1 mix
    
  Scenario: Try to register mix but not logged in
    Given I'm not logged in
    When I register mix
      | name          |
      | FantaLlimona  |
    Then I'm redirected to the login form
    And There are 0 mi
  
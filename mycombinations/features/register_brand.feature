Feature: Register Brand
    In order to keep track of the brands I know
    As a user
    I want to register a brand

 Background: There is a registered user and mix or alcohol
    Given Exists a user "user" with password "password"

  Scenario: Register just brand name
    Given I login as user "user" with password "password"
    When I register brand
      | name        |
      | Larios      |
    Then I'm viewing the details page for brand by "user"
      | name        |
      | Larios      |
    And There are 1 brands

  Scenario: Try to register brand but not logged in
    Given I'm not logged in
    When I register brand
      | name         |
      | Larios       |
    Then I'm redirected to the login form
    And There are 0 brands

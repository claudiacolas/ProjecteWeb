Feature: Register Brand
    In order to keep track of the brands I try
    As a user
    I want to register a brand

 Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just brand name
    Given I login as user "user" with password "password"
    When I register brand
      | name        |
      | Gin |
    Then I'm viewing the details page for brand by "user"
      | name        |
      | Gin  |
    And There are 1 brand
    
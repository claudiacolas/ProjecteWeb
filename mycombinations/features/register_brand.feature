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
    And There are 1 brand
    
  Scenario: Register brand with picture
    Given I login as user "user" with password "password"
    When I register brand at alcohol "Ginebra"
      | name            | image                    |
      | Larios          | features/random.png      |
    Then I'm viewing the details page for dish at restaurant "The Tavern" by "user"
      | name            | image                    |
      | Larios          | mycombinations/random.png |
    And There are 1 dishes

  Scenario: Try to register brand but not logged in
    Given I'm not logged in
    When I register brand at alcohol "Ginebra"
      | name         |
      | Larios       |
    Then I'm redirected to the login form
    And There are 0 dishes

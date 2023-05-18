Feature: Edit Brand
  In order to keep updated my previous registers about brands
  As a user
  I want to edit a brand register I created

  Background: There are registered users and an alcohol by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists alcohol registered by "user2"
      | name    | brand        |
      |  Ron    | Negrita      |
    And Exists brand at alcohol "Ron" by "user2"
      | name     |
      | Negrita  |



  Scenario: Edit owned alcohol registry brand
    Given I login as user "user2" with password "password"
    When I view the details for brand "Negrita"
    And I edit the current Brand
      | name        |
      | Negrita     |
    Then I'm viewing the details page for brand at alcohol "Ron" by "user2"
      | name     |
      | Negrita  |
    And There are 1 brands

  Scenario: Try to edit brand but not logged in
    Given I'm not logged in
    When I view the details for brand "Negrita"
    Then There is no "edit" link available

  Scenario: Try to edit brand but not the owner
    Given I login as user "user1" with password "password"
    When I view the details for brand "Negrita"
    Then There is no "edit" link available
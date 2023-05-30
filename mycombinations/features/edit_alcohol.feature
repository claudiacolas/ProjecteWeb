Feature: Edit Alcohol
  In order to keep updated my previous registers about alcohols
  As a user
  I want to edit an alcohol register I created

  Background: There are registered users and an alcohol by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists combination registered by "user1"
      | name         | alcohol   | mix         |
      | RumCola      | Rum       | Cola        |
    And Exists alcohol at combination "Roncola" by "user2"
      | name    | brand        |
      | Rum     | Negrita      |

  Scenario: Edit owned combination registry alcohol
    Given I login as user "user2" with password "password"
    When I view the details for alcohol "Rum"
    And I edit the current alcohol
      | brand           |
      | Negrita         |
    Then I'm viewing the details page for alcohol at combination "RumCola" by "user2"
      | name     | brand           |
      | Rum      | Negrita         |
    And There are 1 alcohols

  Scenario: Try to edit alcohol but not logged in
    Given I'm not logged in
    When I view the details for alcohol "Rum"
    Then There is no "edit" link available

  Scenario: Try to edit mix but not the owner
    Given I login as user "user1" with password "password"
    When I view the details for alcohol "Rum"
    Then There is no "edit" link available
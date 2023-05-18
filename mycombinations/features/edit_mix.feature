Feature: Edit Mix
  In order to keep updated my previous registers about mixes
  As a user
  I want to edit a mix register I created

  Background: There are registered users and a mix by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists combination registered by "user1"
      | name         | alcohol   | mix         |
      | Roncola      | Ron       | Cola    |
    And Exists mix at combination "Roncola" by "user2"
      | name     | brand          |
      |  Cola    | CocaCola       |

  Scenario: Edit owned combination registry mix
    Given I login as user "user2" with password "password"
    When I view the details for mix "Cola"
    And I edit the current mix
      | brand           |
      | CocaCola        |
    Then I'm viewing the details page for mix at combination "Roncola" by "user2"
      | name     | brand           |
      | Cola     | CocaCola        |
    And There are 1 mixes

  Scenario: Try to edit mix but not logged in
    Given I'm not logged in
    When I view the details for mix "Cola"
    Then There is no "edit" link available

  Scenario: Try to edit mix but not the owner
    Given I login as user "user1" with password "password"
    When I view the details for mix "Cola"
    Then There is no "edit" link available
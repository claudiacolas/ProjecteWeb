Feature: View Mix
  In order to know about a mix
  As a user
  I want to view the registered mix details

  Background: There is one combination with 2 mixes and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists combination registered by "user1"
      | name        |
      | RumCola     |
    And Exists mix at combination "Roncola" by "user1"
      | name       | brand        |
      | Cola       | Coca-Cola      |
    And Exists mix at combination "Roncola" by "user2"
      | name       | brand        |
      | Cola       | Hacendado    |

  Scenario: View details about owned mix
    Given I login as user "user1" with password "password"
    When I view the details for mix "Cola"
    Then I'm viewing mix details including
      | name       | brand        |
      | Cola       | Coca-Cola     |
    And There is "edit" link available

  Scenario: View details about mix but not logged in
    Given I'm not logged in
    When I view the details for mix "Cola"
    Then I'm viewing mix details including
      | name       | brand        |
      | Cola       | Coca-Cola      |
    And There is no "edit" link available

  Scenario: View details about other user mix
      Given I login as user "user1" with password "password"
    When I view the details for mix "Cola"
    Then I'm viewing mix details including
      | name      | brand     |
      | Cola      | Hacendado |
    And There is no "edit" link available
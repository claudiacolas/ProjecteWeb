Feature: View Alcohol
  In order to know about an alcohol
  As a user
  I want to view the registered alcohol details

  Background: There is one combination with 1 alcohol and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists combination registered by "user1"
      | name        |
      | Rumcola     |
    And Exists alcohol at combination "Roncola" by "user1"
      | name      | brand        |
      | Ron       | Negrita      |

  Scenario: View details about owned alcohol
    Given I login as user "user1" with password "password"
    When I view the details for alcohol "Ron"
    Then I'm viewing alcohol details including
      | name      | brand        |
      | Rum       | Negrita      |
    And There is "edit" link available

  Scenario: View details about alcohol but not logged in
    Given I'm not logged in
    When I view the details for alcohol "Ron"
    Then I'm viewing alcohol details including
      | name      | brand        |
      | Rum       | Negrita      |
    And There is no "edit" link available

  Scenario: View details about other user alcohol
      Given I login as user "user1" with password "password"
    When I view the details for alcohol "Ginebra"
    Then I'm viewing alcohol details including
      | name         | brand    |
      | Gin          | Gordon's |
    And There is no "edit" link available
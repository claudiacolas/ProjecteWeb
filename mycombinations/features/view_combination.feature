Feature: View Combination
  In order to know about a combination
  As a user
  I want to view the combination details including all its alcohols, mixes and reviews

  Background: There is one combination with 2 mixes
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists combination registered by "user1"
      | name         | alcohol    | mix       |
      | RumCola      | Rum        | Cola      |
    And Exists mix at combination "Roncola" by "user1"
      | name   | brand    |
      | Cola   | Coca-Cola |
    And Exists mix at combination "WhiskeyCola" by "user2"
      | name   | brand     |
      | Cola   | Hacendado |
    And Exists review at combination "RumCola" by "user1"
      | rating          | comment       |
      | 4               | Quite good    |
    And Exists review at combination "RumCola" by "user2"
      | rating          |
      | 2               |

  Scenario: View details for owned combination with two reviews and a mix
    Given I login as user "user1" with password "password"
    When I view the details for combination "RumCola"
    Then I'm viewing combinations details including
      | name         | alcohol    | mix       |
      | Rumcola      | Rum        | Cola      |
    And There is "edit" link available
    And I'm viewing a combination reviews list containing
      | rating          | comment       | user          |
      | 4               | Quite good    | user1         |
      | 2               |               | user2         |
    And The list contains 2 reviews
    And I'm viewing a combination mixes list containing
      | name      | user          |
      | Cola      | user1         |
    And The list contains 1 mix

  Scenario: View details for other user combination with 1 mix but no reviews
    Given I login as user "user2" with password "password"
    When I view the details for combination "WhiskeyCola"
    Then I'm viewing combinations details including
      | name          | alcohol      | mix       |
      | WhiskeyCola   | Whiskey      | Cola      |
    And There is no "edit" link available
    And I'm viewing a combination reviews list containing
      | rating          | comment       | user          |
    And The list contains 0 reviews
    And I'm viewing a combination mixes list containing
      | name       | user   |
      | Cola       | user2  |
    And The list contains 1 mixes

  Scenario: View details for combination with 1 mix but no reviews when not logged in
    Given I'm not logged in
    When I view the details for combination "WhiskeyCola"
    Then I'm viewing combinations details including
      | name          | alcohol      | mix       |
      | WhiskeyCola   | Whiskey      | Cola      |
    And There is no "edit" link available
    And I'm viewing a combination reviews list containing
      | rating          | comment       | user          |
    And The list contains 0 reviews
    And I'm viewing a combination mixes list containing
      | name       | user   |
      | Cola       | user2  |
    And The list contains 1 mixes
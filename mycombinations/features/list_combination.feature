Feature: List Combinations
  In order to keep myself up to date about restaurants registered in myrestaurants
  As a user
  I want to list the last 5 registered restaurants

  Background: There are 6 registered restaurants by same user
    Given Exists a user "user" with password "password"
    And Exists restaurant registered by "user"
      | name            | date        |
      | WhiskeyCola     | 2023-05-18  |
      | GinCola         | 2023-05-10  |
      | GinOrange       | 2023-05-08  |
      | RumCola         | 2023-05-08  |
      | GinLemon        | 2023-05-08  |

  Scenario: List the last five
    When I list combinations
    Then I'm viewing a list containing
      | name            |
      | WhiskeyCola     |
      | GinCola         |
      | GinOrange       |
      | RumCola         |
      | GinLemon        |
    And The list contains 5 combinations

  Scenario: List the last five
    Given Exists combination registered by "user"
      | name            | date        |
      | PacharanOrange  | 2023-05-08  |
    When I list combinations
    Then I'm viewing a list containing
      | name            |
      | WhiskeyCola     |
      | GinCola         |
      | GinOrange       |
      | RumCola         |
      | GinLemon        |
    And The list contains 5 combinations
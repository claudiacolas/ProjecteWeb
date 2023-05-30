Feature: View Brand
  In order to know about a brand
  As a user
  I want to view the registered brand details

  Background: There is one brand with 2 alcohols and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists brand registered by "user1"
      | name        |      
      | Negrita     | 
    And Exists alcohol at brand "Negrita" by "user1"
      | name        |
      | Rum         |
    And Exists brand at alcohol "Rum" by "user2"
      | name        |
      | Bacardi     |

  Scenario: View details about owned brand
    Given I login as user "user1" with password "password"
    When I view the details for brand "Negrita"
    Then I'm viewing brand details including
      | name      |
      | Negrita   |
    And There is "edit" link available

  Scenario: View details about brand but not logged in
    Given I'm not logged in
    When I view the details for brand "Negrita"
    Then I'm viewing brand details including
      | name      |
      | Negrita   |
    And There is no "edit" link available

  Scenario: View details about other user brand
      Given I login as user "user1" with password "password"
    When I view the details for brand "Bacardi"
    Then I'm viewing brand details including
      | name         |
      | Bacardi      |
    And There is no "edit" link available
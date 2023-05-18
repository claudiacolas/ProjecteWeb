Feature: Edit Combination
  In order to keep updated my previous registers about combinations
  As a user
  I want to edit a combination register I created

  Background: There are registered users and a combination by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists combination registered by "user1"
      | name         | alcohol   | mix         |
      | Roncola      | Ron       | CocaCola    |

  Scenario: Edit owned combination registry mix
    Given I login as user "user1" with password "password"
    When I edit the combination with name "Roncola"
      | mix         |
      | CocaCola    |
    Then I'm viewing the details page for combination by "user1"
      | name         | alcohol   | mix         |
      | Roncola      | Ron       | CocaCola    |
    And There are 1 combinations

  Scenario: Try to edit combination but not logged in
    Given I'm not logged in
    When I view the details for combination "Roncola"
    Then There is no "edit" link available

  Scenario: Try to edit combination but not the owner no edit button
    Given I login as user "user2" with password "password"
    When I view the details for combination "Roncola"
    Then There is no "edit" link available

  Scenario: Force edit combination but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the restaurant with name "Roncola"
      | mix        |
      | CocaCola   |
    Then Server responds with page containing "403 Forbidden"
    When I view the details for restaurant "Roncola"
    Then I'm viewing the details page for combination by "user1"
      | name         | alcohol   | mix         |
      | Roncola      | Ron       | CocaCola    |
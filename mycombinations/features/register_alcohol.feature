Feature: Register Alcohol
    In order to keep track of the alcohols I try
    As a user
    I want to register a alcohol together with its brand details

 Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just alcohol name
    Given I login as user "user" with password "password"
    When I register alcohol
      | name        |
      | Gin |
    Then I'm viewing the details page for alcohol by "user"
      | name        |
      | Gin  |
    And There are 1 alcohol
    
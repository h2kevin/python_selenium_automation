Feature: Tests for Target Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Search for a product
    Then Verify that correct search results shown

  Scenario: User can search for a product2
    Given Open target main page
    When Search for a product
    Then Verify that correct search results shown

 Scenario: User can see Cart Empty message
    Given Open target main page
    When Click on cart icon
    Then Verify Cart Empty message shown

 Scenario: user can see the sign in form opened
   Given Open target main page
   When CLick Sign in
   Then Verify Sign in form is opened

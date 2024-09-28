Feature: Tests for Target Search functionality

  Scenario: User can search for a coffee
    Given Open target main page
    When Search for a coffee
    Then Verify that correct search results shown for coffee


  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for tea

# 1 update Target product search test case homework lesson 4
  Scenario: User can search for a coffee
    Given Open target main page
    When Search for a laptop
    Then Verify that correct search results shown for laptop

# 1 update Target product search test case homework lesson 4
  Scenario: User can search for a coffee
    Given Open target main page
    When Search for a iphone
    Then Verify that correct search results shown for iphone



#  Scenario: User can see Cart Empty message
#    Given Open target main page
#    When Click on cart icon
#    Then Verify cart Empty message shown
  Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify that correct search results shown for <search_result>
    Examples:
    |search_word  |search_result |
    |coffee       |coffee        |
    |tea          |tea           |
    |mug          |mug           |
    |sugar        |sugar         |

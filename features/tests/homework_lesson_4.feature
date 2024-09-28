# 2 create a test case will open the target circle page
Feature: user can open the Target Circle page and verify there are 10 benefit cells
  Scenario: Verify header has correct amount links
    Given Open Target main page
    When User can open the Target Circle page
    Then Verify Target Circle page has 10 benefit cells


# 3  add any Target's product into the cart, and make sure it's there
  Scenario: add Target's product into the cart, and make sure it's there
    Given Open target main page
    When search for a knife
    Then Verify knife is in the shopping cart



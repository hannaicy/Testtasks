Feature: feature to test Amazon search

  Scenario Outline: Validate Amazon search is working
    Given browser is open
    And user is on Amazon search page and accepts the cookies
    When user enters "<thing>"  in search box and hits enter
    And clicks Sort by: Price: Low to High button
    And clicks the first "<thing>"  product
    And clicks the show all option
    And clicks add to cart of the first "<thing>"  product and check the price
    Then user clicks the cart

       Examples:
        | thing    |
        | snickers |
        | skittles |
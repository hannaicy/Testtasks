# Testtasks
Test tasks from Appsfactory

Challenge 1: Cucumber web test automation suite 

# Introduction
 The Amazonsearch.feature file includes:
- Open the driver and browser
- direct to amazon website
- search the "snickers" product
- get the search result by clicking Sorted by: Price Low to High
- add the "snickers" product in the shopping cart
- search the "skittels" product
- get the search result by clicking Sorted by: Price Low to High
- add the "skittles" product in the shopping cart
- And checkout
- When user is not loged in, it directes to log in page


# Setup
- Make sure you have python installed
- Make sure you habe Pycharm IDE installed
- Install selenium library in cmd using $ pip install selenium
- Install behave in cmd using $ pip install behave

- In python project settings -> Project Intepreter install selenium, behave and allure-behave package

# Create
- Create "Features" folder to store feature files, here the feature file is called Amazonsearch.feature
- Create "steps" folder in side the "Features" folder, here the steps file is called Amazonsteps.py
 
# Run
- In Terminal use command:  behave Features/Amazonsearch.feature
- In Terminal use command:  behave -f allure-behave.formatter:AllureFormatter -o reports/Features/Amazonsearch.feature,
  it will create a folder called "reports" with json reports



Challenge 2: Tools I recommand and CI pipline



Challenge 3: The next big thing in Software Testing
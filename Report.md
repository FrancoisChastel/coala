# Report for assignment 3

## Project

Name: Coala

URL: https://github.com/coala/coala

Coala is a unified interface for checking (linting) and fixing code. It supports many popular programming languages such as Java, C/C++, Python, JavaScript, and many others. It is an out of box product that can be intergrated with any text editor and CI, and allows results to be returned in JSON or customized to the users specific needs.

## Selected issue(s)

Title: Use unittest.mock

URL: https://github.com/coala/coala/issues/1882

This issue required developers to go into a list of about one hundred files and refactor the tests in these files. Specifically, the tests needed to utilize the unittest.mock method of the unittest library in order to remove the dependencies from current unit tests. This makes the unit tests more independent and more of unit tests rather than integration tests when relying on dependencies.

## Onboarding experience

Did it build as documented?
    
Since we were refactoring tests and the documentation for the entire program was immense, we looked specifically at building the enviornment for testing. This enviornment built exactly as documented. We set up a virtual enviornment and installed all dependencies into this enviornment with very simple comands. From there we simply needed to run pytest and we were running the tests.

## Requirements affected by functionality being refactored
Since only the method of object creation for dependency objects in unit tests of the code were changed and the library being used is already a requirement, no requirements to the project are affected by our refactoring.

## Existing test cases relating to refactored code
SettingTest Suite of tests
LineParserTest Suite of tests
ConfParserTest Suite of tests

## The refactoring carried out
We refactored various tests suites to utilize the unittest.mock method in order to create mock class and module objects. This is in contrast to the previous method wherbey the class and module objects were manually created and used for testing. This serves to make the tests more independent and less reliant on module and class dependencies. It creates a separation of unit tests from integration tests. No UML diagram provided because no classes were changed since we were only refactoring tests.

## Test logs

Overall results with link to a copy of the logs (before/after refactoring).

The refactoring itself is documented by the git log.

Before log for all tests: https://github.com/FrancoisChastel/coala/blob/master/tests/logs/BeforeTest.log

File: settings/SettingTest.py
Log before refactoring: https://github.com/FrancoisChastel/coala/blob/master/tests/logs/SettingTest.log
Log after refactoring: https://github.com/FrancoisChastel/coala/blob/master/tests/logs/SettingTestPost.log

File: parsing/LineParserTest.py
Log before refactoring: https://github.com/FrancoisChastel/coala/blob/master/tests/logs/ParsingTestBef.log
Log after refactoring: https://github.com/FrancoisChastel/coala/blob/master/tests/logs/ParsingTestAft.log

File: parsing/ConfParsingTest.py
Log before refactoring: https://github.com/FrancoisChastel/coala/blob/master/tests/logs/ParsingTestBef.log
Log after refactoring: https://github.com/FrancoisChastel/coala/blob/master/tests/logs/ParsingTestAft.log

## Effort spent

Preface:
Due to how large the repo was and finding an appropriate issue later than we would have liked with the help of course staff, we broke up into two different teams: An understanding team and an implemenatation team. Francios and Brian made up the understanding team. Their job was to read the issue, code, documentation, etc and figure out what was going on in the code and what needed to be done given the issue description. Jiayu and Anu made up the implemenation team. Their job was to write the code and implement what the understanding team deemed was necessary. They spent their time playing with the unittest library and figuring out how it works in actual implemenation. The work ended up being divded pretty evenly, with a little more on the implementation side. 

For each team member, how much time was spent in

1. plenary discussions/meetings;
    All Members: 6 hours

2. discussions within parts of the group;
    Brian - Francios: 4 hours
    Anu - Jiayu: 2 hours
    

3. reading documentation;
    Brian: 15 hours
    Francios: 12 hours
    Anu: 4 Hours
    Jiayu: 3 hours

4. configuration;
    All Members: 2 hours

5. analyzing code/output;
    Brian: 12 hours
    Francios: 16 hours

6. writing documentation;
    Brian: 1 hours
    Francious: 1 hours

7. writing code;
    Jiayu: 18 hours
    Anu: 17 hours

8. running code?
    Anu: 9 hours
    Jiayu: 8 hours
    

## Overall experience

What are your main take-aways from this project? What did you learn?

Overall this project seemed a lot easier on the surface than it actually turned out to be. As a group, we didn't think working on an open source project would be too difficult, as some of us had open source experience, and others had industry experience with this type of development. In the end, however, we realized that an open source library like Coala can be extremely challenging to understand. A lot of work for our project in terms of implementation took place towards the very end. This was due to the immense amount of time it took everyone to become familiar with the code, libraries, dependencies, etc invlolved with the project. Having a dedicated group to just reading code was probably the most important part of the entire project for use because they acted as a resource for the coders to lean on when they were blocked. Overall, our conclusions about this project is that the behind the scenes work in a setting like this are extremely important in order to have a good foundation for the software to be written. Understanding is the key in these enviornments. 

We did not complete this issue. In the time we had, we managed to successfully refactor three of the one hundred files lists. We knew going in to this issue that we would not complete it, but we expected to finish more than three files. Unfortunately we did not. We beleive that there is still about 90% of the work remaining on this issue. The learning curve is steep for this, but once that is overcome the act of refactoring these tests becomes much easier.

Is there something special you want to mention here?
While the commits may not be balanced on the repository, we want to stress that the work was evenly distrubuted among group members. The strategy for dividing the work into the two groups was agreed upon in the beginning of the project and we stand firmly by this division, as our understanding group was an extremely valuable resource to us.

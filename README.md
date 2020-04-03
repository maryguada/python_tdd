# python_tdd
Learning about test driven development in Python 

Test Driven Development is a methodology designed to create a test ahead of time , and then proceed to writing out our code that satisfies that test. 
This way we consider as many edge cases at the outset of a problem and then design a more robust solution geared toward working with the edges. 

TDD simple terms: writing a test case for the code before you even write the code. 

AGILE Development Process 
There is something called the : 

SCRUM PROCESS - where developers commit to the code that they will deliver during the current sprint. 

Developers work on the code that they committed to making adjustments as they go, based on the feedback of their stakeholders, managers. etc. 
RETROSPECTIVE - after each sprint, developers give each other feedback about their work. 

The Sprints continue until product is delivered. 

In agile developement, continous integration is needed to maintain the code. 
CONTINOUS DELIVERY - lets developers code within each sprint and not after each sprint. This gets the product 
faster to the stakeholders in tiny bits/ small features/ rather than the whole product. 

Think of it as a small plates restaurant where you can get small plates/ small parts of the product/ 
delivering each one ready rather than delivering the meal all at once. 

________________________________ TDD vs. Non-TDD ________________________________ 

In broad strokes, the steps of a TDD development cycle is as follows:

1) Define a test, ideally with multiple different inputs and outputs
2) Write just enough code to satisfy the test
3) Run the new test to see if the code passes
    - If test passes, continue
    -If test fails, revisit code and change only what is necessary to pass test
4) Run all exisiting tests to make sure that the previous tests still all pass
5) Refactor

________________________________ UNIT TESTS ________________________________ 

ASSERT METHODS 
Asserting a Result
Now that we have the structure of our test, it is time to start validating that are existing code works. To do this, there is a set of methods that the TestCase class provides, known as assert methods.

Assert Methods
Method	                 Checks That	            New In
assertEqual(a,b)	    a == b	
assertNotEqual(a,b)	    a != b	
assertTrue(x)	        bool(x) is True	
assertFalse(x)	        bool(x) is False	
assertIs(a, b)	        a is b              	3.1
assertIsNot(a, b)	     a is not b	            3.1
assertIsNone(x)	        x is None	            3.1
assertIsNotNone(x)	    x is not None	        3.1
assertIn(a, b)      	a in b              	3.1
assertNotIn(a, b)	    a not in b          	3.1
assertIsInstance(a, b)	isinstance(a, b)    	3.2
assertNotIsInstance(a, b)|| not isinstance(a, b) || 3.2
There are quite a few different options, and the usage of each depends on the scenario. 

SUMMARY 
1. `import unittest` and create a class that inherits from `unittest.TestCase`
2. Define a method beginning with `test` so it will get run by TestCase
3. Determine which assert method is most appropriate for the function we are testing
4. Create a few different asserts in our test method so we can test different inputs in one go
5. Run the tests with `python -m unittest first_test.py` and see the result

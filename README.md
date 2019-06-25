# differentiator

This python program can be used to differentiate n-th degree polynomials. 

The program makes use of the NumPy package which is available at https://pypi.org/project/numpy/ 

# How does it work?

The user enters the coefficients of the polynomial. These coefficients are stored in a list. 
A second list stores the exponents e.g. in the case of x^2, 2 is the exponent. 
The derivative of x^n is given by n*x^(n-1). 
The derivative of a constant is zero. ... (&)
Initially both lists contain the (n+1) items where n is the highest degree of the polynomial. We use the remove method to remove the first entry of both lists. This is due to (&).
The multiply function from NumPy is used to multiply the coefficient list with the exponent list. The array is called result.

A note on result formatting:

The result is displayed as ax^0 + bx^1 + cx^2 +... 

A temporary list (temp_list) is created to store ax^0 , bx^1, ... separately. 
A for loop is used to print ax^0 + bx^1 + cx^2 

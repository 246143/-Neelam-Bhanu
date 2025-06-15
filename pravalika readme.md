This C++ program implements a template-based Matrix class that supports:

Matrix creation

Basic operations: Addition, Subtraction, and Multiplication

Output via overloaded << operator

Proper error handling for dimension mismatches

It also includes a comprehensive main() test with valid and edge cases.

✅ Key Features
Generic class using template<typename T> — works with int, float, etc.

Internal storage using vector<vector<T>>

Operator overloading for:

+ matrix addition

- matrix subtraction

* matrix multiplication

Custom output using operator<< to format matrix printing
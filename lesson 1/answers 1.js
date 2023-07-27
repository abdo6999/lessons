//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//

// 1. Data Types and typeof Operator (#010)
// Q: How can you determine the data type of a variable in JavaScript using the typeof operator? Provide an example.

// A: You can use the typeof operator to determine the data type of a variable in JavaScript. It returns a string representing the data type of the variable.

// Example:
const name = "John";
const age = 30;
const isStudent = true;

console.log(typeof name);       // Output: "string"
console.log(typeof age);        // Output: "number"
console.log(typeof isStudent);  // Output: "boolean"

// Explanation: In this example, we have three variables of different data types: name (string), age (number), and isStudent (boolean). We use the typeof operator with each variable and log the results to the console. The output shows the data types of the variables.


// Q: What are the different data types that exist in JavaScript? List at least five of them and provide a brief description of each.

// A: JavaScript has several data types, and they can be categorized as follows:

// 1. Primitive Data Types:
//    a. Number: Represents numeric values, e.g., 5, 3.14.
//    b. String: Represents textual data, e.g., "Hello", 'JavaScript'.
//    c. Boolean: Represents a logical value, either true or false.
//    d. Undefined: Represents a variable that has been declared but not assigned a value.
//    e. Null: Represents an intentional absence of a value.

// 2. Composite Data Types (Reference Types):
//    f. Object: Represents a collection of key-value pairs, e.g., {name: "John", age: 30}.
//    g. Array: Represents a list of elements, e.g., [1, 2, 3].
//    h. Function: Represents a reusable block of code that can be invoked by its name.

// Example:
const num = 42;
const greeting = "Hello";
const isActive = true;
let x;
const person = { name: "John", age: 30 };
const numbers = [1, 2, 3];
function sayHello() {
  console.log("Hello!");
}

console.log(typeof num);      // Output: "number"
console.log(typeof greeting); // Output: "string"
console.log(typeof isActive); // Output: "boolean"
console.log(typeof x);        // Output: "undefined"
console.log(typeof person);   // Output: "object"
console.log(typeof numbers);  // Output: "object"
console.log(typeof sayHello); // Output: "function"

// Explanation: In this example, we have variables of different data types, and we use the typeof operator to determine their types. The output shows the data types of each variable according to the descriptions provided above.



//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//


// 2. Variables Introduction (#011)
// Q: Create two variables, firstName and lastName, and assign your first name and last name to them, respectively.
// Q: Concatenate the two variables and store the result in a new variable called fullName. Output the fullName using console.log().

// A: We will create two variables, firstName and lastName, and assign values to them.
const firstName = "John";
const lastName = "Doe";

// Then, we will concatenate the two variables using the + operator and store the result in the fullName variable.
const fullName = firstName + " " + lastName;

// Finally, we will output the value of fullName using console.log().
console.log(fullName); // Output: "John Doe"

// Explanation: In this example, we created two variables, firstName and lastName, containing the first name and last name, respectively. We concatenated the two variables using the + operator and stored the result in the fullName variable. The console.log() statement then outputs the full name "John Doe".



//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//



// 3. Identifiers Name Conventions And Rules (#012)
// Q: What are the naming conventions for JavaScript identifiers (variables, functions, etc.)? Provide at least three rules.

// A: JavaScript identifiers (e.g., variables, functions, etc.) follow these naming conventions:
// 1. They must start with a letter (a-z, A-Z) or an underscore (_).
// 2. They can contain letters, digits (0-9), and underscores.
// 3. Identifiers are case-sensitive, meaning "myVar" and "myvar" are considered different.

// Example:
let myVar1 = 10;
const _userName = "JohnDoe";
function calculateSum(num1, num2) {
  return num1 + num2;
}

// Explanation: In this example, we have followed the naming conventions for identifiers. "myVar1" starts with a letter, "_userName" starts with an underscore, and "calculateSum" is a function name that uses camelCase and starts with a lowercase letter.

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//

// 4. Var, Let, Const Compare (#013)
// Q: Declare a variable using var, let, and const, and try to reassign values to each of them. Explain the differences in behavior.

// A: We will declare variables using var, let, and const, and then try to reassign values to each of them.

// Using var:
var x = 5;
x = 10; // Reassigning value to x
console.log(x); // Output: 10

// Using let:
let y = 15;
y = 20; // Reassigning value to y
console.log(y); // Output: 20

// Using const:
const z = 25;
z = 30; // Trying to reassign value to z (Error: Assignment to constant variable)
console.log(z);

// Explanation: In this example, we declared variables x, y, and z using var, let, and const, respectively. We were able to reassign values to x and y without any errors. However, when trying to reassign a value to a const variable z, it resulted in an error because const variables cannot be reassigned.


//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//
// 5. String Syntax And Character Escape Sequences (#014)
// Q: Create a string variable containing the following sentence: "I love JavaScript programming!".
// Q: Using escape sequences, add a new line character between "love" and "JavaScript", and print the modified string.

// A: We will create a string variable and use the escape sequence '\n' to add a new line character between "love" and "JavaScript".

// Create the string variable:
const sentence = "I love JavaScript programming!";

// Using the escape sequence '\n' to add a new line between "love" and "JavaScript":
const modifiedSentence = "I love\nJavaScript programming!";

// Output the modified string:
console.log(modifiedSentence);

// Explanation: In this example, we created a string variable called "sentence" with the original sentence. We then used the escape sequence '\n' to add a new line character between "love" and "JavaScript", creating the "modifiedSentence" variable. The console.log() statement then outputs the modified sentence with a new line between "love" and "JavaScript".

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//
// 6. Concatenation (#015)
// Q: Create two variables, num1 and num2, and assign them two numbers of your choice.
// Q: Concatenate these two variables as strings and store the result in a new variable called result.
// Q: Output the result using console.log().

// A: We will create two variables, num1 and num2, and assign them numbers of our choice.
const num1 = 10;
const num2 = 20;

// We will then concatenate these two variables as strings and store the result in a new variable called "result".
const result = num1.toString() + num2.toString();

// Finally, we will output the result using console.log().
console.log(result); // Output: "1020"

// Explanation: In this example, we created two variables, num1 and num2, and assigned them the numbers 10 and 20, respectively. We used the toString() method to convert these numbers into strings and then concatenated them using the + operator, storing the result in the "result" variable. The console.log() statement then outputs the concatenated string "1020".


//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//
// 7. Template Literals Template Strings (#016)
// Q: Create three variables: name, age, and profession, and assign values to them.
// Q: Use template literals to form a sentence using these variables, and output it using console.log().

// A: We will create three variables, name, age, and profession, and assign values to them.
const name = "John";
const age = 30;
const profession = "Software Engineer";

// We will then use template literals to form a sentence using these variables.
const sentence = `My name is ${name}. I am ${age} years old, and I work as a ${profession}.`;

// Finally, we will output the sentence using console.log().
console.log(sentence);

// Explanation: In this example, we created three variables, name, age, and profession, with their respective values. We used template literals (enclosed by backticks) to form a sentence that includes the values of these variables using placeholder `${}` syntax. The console.log() statement then outputs the complete sentence.

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//
// 8. Variable And Concatenation Challenge (#017)
// Q: Given the following variables:
//    var firstName = "John";
//    var lastName = "Doe";
//    var country = "USA";
//    var city = "New York";
//    var age = 30;
// Q: Create a sentence using the above variables to introduce yourself. The output should be in the format: "My name is John Doe. I am 30 years old. I live in New York, USA."

// A: We will use the given variables to create a sentence introducing the person.

// Given variables:
var firstName = "John";
var lastName = "Doe";
var country = "USA";
var city = "New York";
var age = 30;

// Forming the sentence using the variables:
var introduction = `My name is ${firstName} ${lastName}. I am ${age} years old. I live in ${city}, ${country}.`;

// Output the sentence:
console.log(introduction);

// Explanation: In this example, we used the given variables to form a sentence using template literals. The resulting sentence introduces the person with their name, age, and location, following the specified format.

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//
// 9. Arithmetic Operators (#018)
// Q: Create two variables, num1 and num2, and assign them two numbers of your choice.
// Q: Perform addition, subtraction, multiplication, division, and modulo operations on these two variables.
// Q: Output the results using console.log().

// A: We will create two variables, num1 and num2, and assign them numbers of our choice.
const num1 = 10;
const num2 = 5;

// Perform addition:
const sum = num1 + num2;
console.log(`Sum: ${sum}`); // Output: "Sum: 15"

// Perform subtraction:
const difference = num1 - num2;
console.log(`Difference: ${difference}`); // Output: "Difference: 5"

// Perform multiplication:
const product = num1 * num2;
console.log(`Product: ${product}`); // Output: "Product: 50"

// Perform division:
const quotient = num1 / num2;
console.log(`Quotient: ${quotient}`); // Output: "Quotient: 2"

// Perform modulo (remainder) operation:
const remainder = num1 % num2;
console.log(`Remainder: ${remainder}`); // Output: "Remainder: 0"

// Explanation: In this example, we performed various arithmetic operations on the variables num1 and num2 and outputted the results using console.log().

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//
// 10. Unary Plus And Negation Operators (#019)
// Q: Create a variable, num, and assign it a positive number.
// Q: Use the unary plus and unary negation operators to print the number as both positive and negative values.

// A: We will create a variable "num" and assign it a positive number. Then, we will use the unary plus and unary negation operators to print the number as both positive and negative values.

// Create the variable and assign a positive number:
const num = 42;

// Use unary plus to print the number as positive:
console.log(`Positive Number: +${num}`); // Output: "Positive Number: +42"

// Use unary negation to print the number as negative:
console.log(`Negative Number: -${num}`); // Output: "Negative Number: -42"

// Explanation: In this example, we used the unary plus (+) and unary negation (-) operators to print the number "42" as both positive and negative values.

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//

// 11. Type Coercion (#020)
// Q: Given the following variables:
//    var value1 = "5";
//    var value2 = 9;
// Q: Perform addition on these variables. What is the result, and why?

// A: We will perform addition on the given variables and analyze the result.

// Given variables:
var value1 = "5";
var value2 = 9;

// Perform addition on the variables:
const result = value1 + value2;

// Output the result:
console.log(result); // Output: "59"

// Explanation: In this example, the variable "value1" contains a string "5", and the variable "value2" contains a number 9. When performing addition, JavaScript performs type coercion and converts the number 9 to a string and concatenates it with the string "5", resulting in the concatenated string "59".

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//
// 12. Assignment Operators (#021)
// Q: Create a variable, score, and set its value to 10.
// Q: Using assignment operators, update the score variable to double its value and output the result using console.log().

// A: We will create a variable "score" and set its initial value to 10. Then, we will use the assignment operator to update the "score" variable and double its value.

// Create the variable and set its initial value:
let score = 10;

// Double the value of "score" using the assignment operator:
score *= 2;

// Output the updated value of "score":
console.log(`Updated Score: ${score}`); // Output: "Updated Score: 20"

// Explanation: In this example, we used the assignment operator (*=) to double the value of the "score" variable. The console.log() statement then outputs the updated value of "score", which is 20.

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------//













/* This file contains functions to validate web form input
   Alter functions as needed for your purposes

   A bit on regexps:
   * enclosed within a leading /^ and an ending $/
   * can string together various regexps e.g. [A-Za-z] gives all letters
   * special characters in regexps: [ \ ^ . | $ * + ? and ( )

   Useful JavaScript regular expressions are:
   [A-Z]  Capital letters only
   [a-z]  lower case letters only
   [0-9]  Numbers only
   \s whitespace (space, tab, newline, etc)
   \w word character (letter, number, underscore)
   \n newline
   ^ beginning of string
   $ end of string
   Special use of ^: [^abc] means NOT abc

   regexp matches for more complicated things:
   [ABC] any single char in the set
   [ABC]+ one or more chars in the set
   \d digits  (\D for non-digit)
   \r carriage return
   . - Matches any character, except for line breaks if dotall is false.
   * - Matches 0 or more of the preceding character.
   + - Matches 1 or more of the preceding character.
   ? - Preceding character is optional. Matches 0 or 1 occurrence

   More here: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
*/

// CHECK INPUT HAS LETTERS (caps or not) AND SPACE
function checkAlpha(inp)
{
  var allowedvals = /^[A-Za-z\s]+$/;   // allowed values go in regexp here
  if(inp.value.match(allowedvals))
  {
    return true;
  }
  else
  {
    alert('Input must have letters only');
    inp.focus();
    return false;
  }
}

// CHECK INPUT HAS LETTERS (caps or not) AND NUMBERS ONLY
function checkAlphaNum(inp)
{
  var allowedvals = /^[A-Za-z\d]+$/;     // allowed values go in regexp here
  if(inp.value.match(allowedvals))
  {
    return true;
  }
  else
  {
    alert('Input must have letters or numbers only');
    inp.focus();
    return false;
  }
}

function checkNum(inp)
{
  var numbers = /^[0-9]+$/;             // or you could use \d
  if(inp.value.match(numbers))
  {
    return true;
  }
  else
  {
    alert('Input must have numeric characters only');
    inp.focus();
    return false;
  }
}

// CHECK EMAIL FORMAT
// a more complicated check because email addresses have a specific format:
// email addresses should be word characters and may contain periods or dashes,
// then an @ then word chars
// and lastly a period followed by two or three letters
function checkEmail(userEmail)
{
  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.[A-Za-z]{2,3})+$/;
  if(userEmail.value.match(mailformat))
  {
    return true;
  }
  else
  {
    alert("You have entered an invalid email address!");
    userEmail.focus();
    return false;
  }
}

// CHECK INPUT LENGTH BETWEEN MIN AND MAX LENGTH
// can be used for things like user id or passwords
function checkLength(inp,inp_min,inp_max)
{
  var inp_len = inp.value.length;
  if (inp_len == 0 || inp_len >= inp_min || inp_len < inp_max)
  {
    alert("Input length must be between "+inp_min+" and "+inp_max);
    inp.focus();
    return false;
  }
  return true;
}

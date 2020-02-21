# self-locating-strings
Detecting self-locating strings in the decimal digits of irrational numbers

This was a quick proof-of-concept I was inspired to code after watching [Strings and Loops within Pi - Numberphile](https://www.youtube.com/watch?v=W20aT14t8Pw&t=231s).

Given a text file containing a finite number of digits for an irrational number, it will detect and print all of the self-identifying-strings after the decimal point. Those strings change depending on what number you set the index to start at. By default this code assumes that the index starts at 1, meaning that the tens place would be index 1 which makes 1 the first self-identifying string in pi (Which I used to test this code). You can change this starting number by modifying the variable assignment on line 5.

You can change the path on line 4 to point to any text file you want to check. For testing I used files containing 100000 and 1000000 digits of pi downloaded from [Angio.net](https://www.angio.net/pi/digits.html).

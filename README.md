# self-locating-strings
Detecting self-locating strings in the decimal digits of irrational numbers

This was a quick proof-of-concept developed after watching [Strings and Loops within Pi - Numberphile](https://www.youtube.com/watch?v=W20aT14t8Pw&t=231s).

Given a text file containing a a finite number of digits for an irrational number, it will detect and print all the self-identifying-strings after the decimal point. Those strings change depending on what number you assume the index to start at. By default this code assumes that the index starts at 1, meaning that the tens place would be index 1 and therefore the first self-identifying-string in pi (Which I used to test this code). Y

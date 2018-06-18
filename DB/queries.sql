--Race :
Select *
From information
Where race = aRace;

--Age:
Select *
From information
Where age num1 and num2;
--Count :
Select *
From information
Where count Between num1 and num2;

--Income: 
Select *
From information
Where Income Between num1 and num2;

--Race and Age:
Select *
From information
Where age Between num1 and num2
AND race = aRace;

--Race and Count:
Select *
From information
Where race = a Race
AND count between num1 and num2;

--Race and  Income:
Select *
From information
Where race = aRace
AND income Between num1 and num2;

--Age and count:
Select *
From information
Where age Between num1 and num2
AND count between num1 and num2;

--Age and income:
Select *
From information
Where age Between num1 and num2;

10. Count and income:
Select *
From information
Where count between num1 and num2
AND income between num1 and num2;

--Race, age and count:
Select *
From information
Where age between num1 and num2
AND count between num1 and num2
AND race = aRace;

--Race, age, and income:
Select *
From information
Where race = aRace
AND age between num1 and num2
AND income between num1 and num2;

--Age, count, and income:
Select *
From information
Where count between num1 and num2
AND age between num1 and num2
AND income between num1 and num2;

--Race, age, count, and  income:
Select *
From information
Where race = aRace
AND age between num1 and num2
AND count between num1 and num2
AND income between num1 and num2
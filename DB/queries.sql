--Race :
Select *
From information
Where race = aRace;

--Age:
Select *
From information
Where age num1 and num2;

--population :
Select *
From information
Where population Between num1 and num2;

--Income: 
Select *
From information
Where Income Between num1 and num2;

--Race and Age:
Select *
From information
Where age Between num1 and num2
AND race = aRace;

--Race and population:
Select *
From information
Where race = a Race
AND population between num1 and num2;

--Race and  Income:
Select *
From information
Where race = aRace
AND income Between num1 and num2;

--Age and population:
Select *
From information
Where age Between num1 and num2
AND population between num1 and num2;

--Age and income:
Select *
From information
Where age Between num1 and num2;

10. population and income:
Select *
From information
Where population between num1 and num2
AND income between num1 and num2;

--Race, age and population:
Select *
From information
Where age between num1 and num2
AND population between num1 and num2
AND race = aRace;

--Race, age, and income:
Select *
From information
Where race = aRace
AND age between num1 and num2
AND income between num1 and num2;

--Age, population, and income:
Select *
From information
Where population between num1 and num2
AND age between num1 and num2
AND income between num1 and num2;

--Race, age, population, and  income:
Select *
From information
Where race = aRace
AND age between num1 and num2
AND population between num1 and num2
AND income between num1 and num2
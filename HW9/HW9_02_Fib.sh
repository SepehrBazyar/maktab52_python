#!/bin/bash
#Written by: Sepehr Bazyar
read -p "Please Enter N th of the Fib Sequence: " n #get input with print a message(-p)
a=1 #smaller numbers
b=1 #bigger numbers
echo "Fib($n) = " > "Fib.txt" #clear file with echo > mode into the file
for (( counter=0; counter < $n; counter++ )) #for loop to n times
do
	if [ $counter -gt 0 ]; #write comma after first numbers that mean counter not 0
	then
		echo ", " >> "Fib.txt" #append comma into the file with echo >> mode
	fi
	echo $a >> "Fib.txt" #write smaller number before change number next round
	c=$(($a+$b)) #calculate bigger numbers for example: c = a + b = 2 + 3 = 5
	a=$b #swap a and b because now b is smaller for example a = b = 3
	b=$c #b is c value because this is bigger than old b for exmaple b = c = 5
done


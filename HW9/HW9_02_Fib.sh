#!/bin/bash
#Written by: Sepehr Bazyar
read -p "Please Enter N th of the Fib Sequence: " n
a=1
b=1
echo "Fib($n) = " > "Fib.txt"
for (( counter=0; counter < $n; counter++ ))
do
	if [ $counter -gt 0 ];
	then
		echo ", " >> "Fib.txt"
	fi
	echo $a >> "Fib.txt"
	c=$(($a+$b))
	a=$b
	b=$c
done

#!/bin/bash
#Written by: Sepehr Bazyar
read -p "Please Enter N th of the Fib Sequence: " n
a=1
b=1
for (( counter=0; counter < $n; counter++ ))
do
	echo $a
	c=$(($a+$b))
	a=$b
	b=$c
done

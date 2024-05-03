#!/bin/bash
for i in 1 2 3 4 5
do
    echo "Test: $i"    
    python3 Lab_1A.py   
    python3 Lab_1B.py 
    python3 Lab_1C.py 
    sleep 5
done


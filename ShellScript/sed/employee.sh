awk '{print}' employee.txt > employee.out
awk '/manager/ {print}' employee.txt >> employee.out
awk '{print $1,$4}' employee.txt  >> employee.out
awk '{print NR,$0}' employee.txt  >> employee.out
awk '{print $1,$NF}' employee.txt  >> employee.out
awk 'NR==3, NR==6 {print NR,$0}' employee.txt  >> employee.out




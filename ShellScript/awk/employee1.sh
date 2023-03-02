awk '{print NR "- " $1 }' employee1.in > employee1.out
awk '{print $2}' employee1.in >>  employee1.out
awk 'NF < 0'  employee1.in >>  employee1.out
awk '{ if (length($0) > max) max = length($0) } END { print max }' employee1.in >>  employee1.out
awk 'END { print NR }' employee1.in >>  employee1.out
awk 'length($0) > 10'  employee1.in >>  employee1.out
awk '{ if($3 == "B6") print $0;}'  employee1.in >>  employee1.out
awk 'BEGIN { for(i=1;i<=6;i++) print "square of", i, "is",i*i; }' >> employee1.out



# Remove duplicated IP Addresses

file=$1
output=./new_file.log
new_file=/tmp/output_1.txt

awk '{ a[i++] = $0 } END { for (j=i-1; j>=0;) print a[j--] }' $file > $output
awk '{ map[$1]=$0 } END { for ( i in map) { print map[i] } }' $output > $new_file

rm -f $output
cat $new_file
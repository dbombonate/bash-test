
#!/bin/bash

rm -f servers_version.txt

while IFS= read -r line
do
  ip=$(ping -c1 $line | grep from | awk '{print $5}' | sed 's/(//g' | sed 's/)//g' | sed 's/://g')
  hour=$(date +%H:%M:%S)
  date=$(date +%D)
  osVersion=$(ssh myuser@$line 'uname -a')
  echo $hour $date $line $ip $osVersion >> servers_version.txt
done < $1
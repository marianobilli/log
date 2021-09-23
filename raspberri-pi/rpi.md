### Measure temperature
```
#!/bin/bash
for f in {1..7}
do
	clear
	echo "execution $f"
	sysbench --test=cpu --cpu-max-prime=25000 --num-threads=4 run
done
vcgencmd measure_tempe
```

### To ssh
remember to drop the empty `ssh` file on the sd

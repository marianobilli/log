to check under replicated blocks
```
hdfs fsck -blocks | grep "Under replicated"
```

to extract the block id of under replicated blocks
```
hdfs fsck -blocks | grep "Under replicated" | sed -r 's/.*(blk_.*)_.*/\1/' | tee file.txt
```

to print status of a given block
```
hdfs fsck -blockId
```
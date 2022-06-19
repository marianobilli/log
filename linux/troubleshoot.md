# find if a process was killed by the oom-killer

```
dmesg | egrep -i 'killed process'

# this is related to the overcommit of memory configured in
/proc/sys/vm/overcommit_memory
/proc/sys/vm/overcommit_ratio
```

These messages might also be in 
```
grep -i 'killed process' /var/log/messages
grep -i 'killed process' /var/log/syslog
```

# Test smtp server (mutt client)
Docker image: `teske/mutter`
```
# in the container...
echo 'set smtp_url="smtp://email-smtp.eu-west-1.amazonaws.com:587/"' > ~/.muttrc
echo "this is a test body" | mutt -s "This is a test subject" "an.email@domain.com" 
```

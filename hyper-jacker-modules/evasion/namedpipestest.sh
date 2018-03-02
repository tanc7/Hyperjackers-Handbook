
$pipe=testpipe2
mkfifo $pipe
inst1='cd /var/log;egrep -irna 'priority: 1' &'
inst2='read output <$pipe'

eval $inst1 &
eval $inst2 &
print $output

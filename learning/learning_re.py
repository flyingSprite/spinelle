import re

# Match format 'MSGID [SUBSCRIBE-DATA] MSG'
pattern = re.compile('(\S+) \[([\S]*|(\S+)([\s\S]*)(\S+))\]( (\S[\s\S]*))?$')

result = pattern.match('1 [s] s s ')

if result:
    print('Match successful.')
else:
    print('Match fail.')

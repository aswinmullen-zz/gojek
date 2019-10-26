import re
keywords = ['opened', 'sshd:session']
with open('/var/log/auth.log', 'r') as f1:
    for line in f1:
      if all(re.search(r, line) for r in keywords):
        print(line)

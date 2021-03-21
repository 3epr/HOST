import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.1.51', username="root", password='18021987', look_for_keys=False,  allow_agent=False)
client.exec_command('cp -a /mnt/HD/HD_a2/hosts /etc/')
client.close()

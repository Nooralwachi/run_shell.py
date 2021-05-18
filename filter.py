import subprocess, os
def filter(filename):
	with open(filename, 'r') as f, open('error_log.txt', 'w') as fw:
		for line in f:
			lines=line.strip().split(', ')
			if int(lines[2]) >=85:
				print(lines[0], lines[3])


		subprocess.run("awk -F, '$3>=85 {print $1 $4}' log.txt", shell=True)
		os.system("awk -F, '$3>=85 {print $1 , $4}' log.txt")

		# subprocess.run("ls -z 2>&1 | tee error_log.txt", shell=True)
		
		cmd= subprocess.run('this-command-does-not-exist', capture_output=True,shell=True)
		fw.write(cmd.stderr.decode('utf-8'))
filter('log.txt')
import subprocess

subprocess.Popen( 'dpkg -i *deb',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate('N\n')

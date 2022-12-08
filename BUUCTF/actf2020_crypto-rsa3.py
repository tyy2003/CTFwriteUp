from math import isqrt
from gmpy2 import next_prime
from Crypto.Util.number import *

n = 177606504836499246970959030226871608885969321778211051080524634084516973331441644993898029573612290095853069264036530459253652875586267946877831055147546910227100566496658148381834683037366134553848011903251252726474047661274223137727688689535823533046778793131902143444408735610821167838717488859902242863683
c = 1457390378511382354771000540945361168984775052693073641682375071407490851289703070905749525830483035988737117653971428424612332020925926617395558868160380601912498299922825914229510166957910451841730028919883807634489834128830801407228447221775264711349928156290102782374379406719292116047581560530382210049
e = 65537
x = isqrt(n)
q = next_prime(x)
p = n//q
# print(p, q)
# p = 13326909050357447643526585836833969378078147057723054701432842192988717649385731430095055622303549577233495793715580004801634268505725255565021519817179231 
# q = 13326909050357447643526585836833969378078147057723054701432842192988717649385731430095055622303549577233495793715580004801634268505725255565021519817179293
d = inverse(e, (p-1)*(q-1))
m = pow(c, d, n)
flag = long_to_bytes(m).decode()
print(flag) # actf{p_and_q_should_not_be_so_close_in_value}
from gmpy2 import *
import binascii

e = mpz(284100478693161642327695712452505468891794410301906465434604643365855064101922252698327584524956955373553355814138784402605517536436009073372339264422522610010012877243630454889127160056358637599704871937659443985644871453345576728414422489075791739731547285138648307770775155312545928721094602949588237119345)
n = mpz(468459887279781789188886188573017406548524570309663876064881031936564733341508945283407498306248145591559137207097347130203582813352382018491852922849186827279111555223982032271701972642438224730082216672110316142528108239708171781850491578433309964093293907697072741538649347894863899103340030347858867705231)
c = mpz(350429162418561525458539070186062788413426454598897326594935655762503536409897624028778814302849485850451243934994919418665502401195173255808119461832488053305530748068788500746791135053620550583421369214031040191188956888321397450005528879987036183922578645840167009612661903399312419253694928377398939392827)
p = mpz(18489327396055733397216193236128138397765028288613793035021305599301380136673327250408422592244732819005905679957567952974717041052102175277835219391448987)
q = mpz(25336772790324258952117622504537139442881120269760383961991795601846585772802865528712760553670210656524156997774484665833049279421936394718949688217533213)
phi_n = (p-1)*(q-1)
d = invert(e, phi_n) 
m = powmod(c, d, n)  # m = c^d%n
flag = binascii.unhexlify(hex(m)[2:]).decode('utf-8')
print(flag) # flag{very_biiiiig_e}
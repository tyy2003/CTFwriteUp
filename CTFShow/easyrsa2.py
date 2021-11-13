from gmpy2 import *
import binascii

e = mpz(65537)
n = mpz(23686563925537577753047229040754282953352221724154495390687358877775380147605152455537988563490716943872517593212858326146811511103311865753018329109314623702207073882884251372553225986112006827111351501044972239272200616871716325265416115038890805114829315111950319183189591283821793237999044427887934536835813526748759612963103377803089900662509399569819785571492828112437312659229879806168758843603248823629821851053775458651933952183988482163950039248487270453888288427540305542824179951734412044985364866532124803746008139763081886781361488304666575456680411806505094963425401175510416864929601220556158569443747)
c = mpz(1627484142237897613944607828268981193911417408064824540711945192035649088104133038147400224070588410335190662682231189997580084680424209495303078061205122848904648319219646588720994019249279863462981015329483724747823991513714172478886306703290044871781158393304147301058706003793357846922086994952763485999282741595204008663847963539422096343391464527068599046946279309037212859931303335507455146001390326550668531665493245293839009832468668390820282664984066399051403227990068032226382222173478078505888238749583237980643698405005689247922901342204142833875409505180847943212126302482358445768662608278731750064815)
p = mpz(149751992878258417619955913803349588855907883795437275015624379454686823076475394292360761230383018058515386650339444595246524276345367505681814522035068825010950620582957883108812048922184886717309007677307472277565963907119402324227023856527902596769190955018836727291623263893333224367236239361837356140243)
q = mpz(158171944628434297901073909637722153795182500207437382406943949068719041821522249518991083268349210029996372436712077867872196821502572326830142173784785697378334976861590406851563704862868317200039579262508714027560242806981225550090918382144776028695390747339519174603519115397094447596926441933797085906929)
phi_n = (p-1)*(q-1)
d = invert(e, phi_n) 
m = powmod(c, d, n)  # m = c^d%n
flag = binascii.unhexlify(hex(m)[2:]).decode('utf-8')
print(flag) # flag{m0_bv_hv_sv}
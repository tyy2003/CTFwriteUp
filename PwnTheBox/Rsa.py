from Crypto.Util.number import bytes_to_long, long_to_bytes
from gmpy2 import *

c2 = 979153370552535153498477459720877329811204688208387543826122582132404214848454954722487086658061408795223805022202997613522014736983452121073860054851302343517756732701026667062765906277626879215457936330799698812755973057557620930172778859116538571207100424990838508255127616637334499680058645411786925302368790414768248611809358160197554369255458675450109457987698749584630551177577492043403656419968285163536823819817573531356497236154342689914525321673807925458651854768512396355389740863270148775362744448115581639629326362342160548500035000156097215446881251055505465713854173913142040976382500435185442521721
n2 = 12806210903061368369054309575159360374022344774547459345216907128193957592938071815865954073287532545947370671838372144806539753829484356064919357285623305209600680570975224639214396805124350862772159272362778768036844634760917612708721787320159318432456050806227784435091161119982613987303255995543165395426658059462110056431392517548717447898084915167661172362984251201688639469652283452307712821398857016487590794996544468826705600332208535201443322267298747117528882985955375246424812616478327182399461709978893464093245135530135430007842223389360212803439850867615121148050034887767584693608776323252233254261047
m2 = bytes_to_long(b'BJD'*32)
# print(m2) 
# m2 = 402017913579464308549065187632311712702457024609243629355239472425901405342857173163318953042818239800250726439867872520201555400267080696314487494273728199047706293587181667486153447024103148497383783335982253445744950705916103236
for i in range(100000):
    if pow(m2, i, n2) == c2:
        e = i
        break
# print(e) 
# e = 52361
n1 = 13508774104460209743306714034546704137247627344981133461801953479736017021401725818808462898375994767375627749494839671944543822403059978073813122441407612530658168942987820256786583006947001711749230193542370570950705530167921702835627122401475251039000775017381633900222474727396823708695063136246115652622259769634591309421761269548260984426148824641285010730983215377509255011298737827621611158032976420011662547854515610597955628898073569684158225678333474543920326532893446849808112837476684390030976472053905069855522297850688026960701186543428139843783907624317274796926248829543413464754127208843070331063037
q = gcd(n1, n2)
# print(q)
# q = 99855353761764939308265951492116976798674681282941462516956577712943717850048051273358745095906207085170915794187749954588685850452162165059831749303473106541930948723000882713453679904525655327168665295207423257922666721077747911860159181041422993030618385436504858943615630219459262419715816361781062898911
p1 = n1//q
# print(p1)
# p1 = 135283423427545651023916134156519717109709399113553907832988770259402226695880524199087896377303631866790192008529658716376684328032075836094156150811025163336681163420875451747389868549203081743561907379260240665153166927504059379076555558704275659133135906827306189040804323574468819553401905127999523676067
c1 = 12641635617803746150332232646354596292707861480200207537199141183624438303757120570096741248020236666965755798009656547738616399025300123043766255518596149348930444599820675230046423373053051631932557230849083426859490183732303751744004874183062594856870318614289991675980063548316499486908923209627563871554875612702079100567018698992935818206109087568166097392314105717555482926141030505639571708876213167112187962584484065321545727594135175369233925922507794999607323536976824183162923385005669930403448853465141405846835919842908469787547341752365471892495204307644586161393228776042015534147913888338316244169120
d = invert(e, (p1-1)*(q-1))
m1 = pow(c1, d, n1)
flag = long_to_bytes(m1).decode().replace('BJD', 'flag')
print(flag) # flag{p_is_common_divisor}
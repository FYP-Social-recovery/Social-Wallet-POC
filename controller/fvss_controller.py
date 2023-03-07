import random
import math
from decimal import Decimal
import time
from Crypto.Util.number import *

class VSS_Controller:

    # first few primes
    first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                        31, 37, 41, 43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97, 101, 103,
                        107, 109, 113, 127, 131, 137, 139,
                        149, 151, 157, 163, 167, 173, 179,
                        181, 191, 193, 197, 199, 211, 223,
                        227, 229, 233, 239, 241, 251, 257,
                        263, 269, 271, 277, 281, 283, 293,
                        307, 311, 313, 317, 331, 337, 347, 349]



    def __init__(self) -> None:
        pass

    def nBitRandom(self,n):
        return random.randrange(2**(n-1)+1, 2**n - 1)

    # finding a coprime to all the gievn primes (n bit)
    def getLowLevelPrime(self,n):
        while True:
            # large random number
            pcandidate = self.nBitRandom(n)

            # Test divisibility with the gievn prime list
            for divisor in self.__class__.first_primes_list:
                if pcandidate % divisor == 0 and divisor**2 <= pcandidate:
                    break
            else:
                return pcandidate

    #rabin miller primarlity test
    def isMillerRabinPassed(self,mrcandidate):
        maxDivisionsByTwo = 0
        ecandidate = mrcandidate-1
        while ecandidate % 2 == 0:
            ecandidate >>= 1
            maxDivisionsByTwo += 1
        assert (2**maxDivisionsByTwo * ecandidate == mrcandidate-1)

        def trialComposite(round_tester):
            if pow(round_tester, ecandidate, mrcandidate) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2**i * ecandidate, mrcandidate) == mrcandidate-1:
                    return False
            return True

        # number of trials here
        numberOfRabinTrials = 20
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrcandidate)
            if trialComposite(round_tester):
                return False
        return True
    
    def largePrime(self):
        while True:
            n = 128
            prime_candidate = self.getLowLevelPrime(n)
            if not self.isMillerRabinPassed(prime_candidate):
                continue
            else:
                return prime_candidate
                break

    def find_generator(self,prime, prime_factors):
        for i in range(1000):
            generator = random.randrange(1, prime-1)
            for p_factor in prime_factors:  # check for each prime factor of Euler Totient of prime
                # divide Euler Totient of p by prime factor
                j = int((prime-1)/p_factor)
                e = pow(generator, j, prime)  # (generator**j)%prime
                if e == 1:  # if e=1 not a generator
                    break
            else:
                return generator

    def prime_factors(self,n):
        prime_factors_set = set()

        # Print the number of two's that divide n
        while n % 2 == 0:
            prime_factors_set.add(2)
            n = n / 2

        # n must be odd at this point
        for i in range(3, int(math.sqrt(n))+1, 2):

            # while i divides n , print i and divide n
            while n % i == 0:
                prime_factors_set.add(i)
                n = n / i

        # if n is a prime number greater than 2
        if n > 2:
            prime_factors_set.add(int(n))

        return prime_factors_set
    
    def isprime(self,n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        i = 3
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i = i + 2
        return True


    def initial(self,Z_lower=10000):
        #generate q bigger than z_lower
        q = self.largePrime()
        #q = 95575507822290034779886372913061420274676365488455261987395964641774104119687
        

        print("q = " + str(q))
        print("\nq is prime\n")

        # Find p and r
        r = 1
        while True:
            p = r*q + 1
            if self.isMillerRabinPassed(p):
                print("r = " + str(r))
                print("p = " + str(p))
                print("\np is prime\n")
                break
            r = r + 1

        g = self.find_generator(p, self.prime_factors(p-1))

        print("\ng = " + str(g) + "\n")

        return p, q, r, g


    def coeff(self,t, secret, FIELD_SIZE):
        coeff = [random.randrange(0, FIELD_SIZE) for _ in range(t-1)]
        coeff.append(secret)  # a0 is secret
        return coeff


    def f(self,x, coefficients, q):
        y = 0
        for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
            y += (x ** coefficient_index * coefficient_value)
        return y


    def commitment(self,coefficients, g, p):
        commitments = []
        for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
            #c = g ** coefficient_value % p
            c = pow(g, coefficient_value, p)
            commitments.append(c)
        return commitments


    def verification(self,g, commitments, i, p):
        v = 1
        for k, c in enumerate(commitments):
            #v = v * (c) ** (i ** k) % p
            v = v * pow(c, i ** k, p) % p
        return v


    def quick_pow(self,a, b, q):
        temp = 1
        for i in range(1, b+1):
            temp = temp * a % q
        return temp % q


    def reconstruct_secret(self, pool):
        sums = 0

        for j, share_j in enumerate(pool):
            xj, yj = share_j
            prod = 1

            for i, share_i in enumerate(pool):
                xi, _ = share_i
                if i != j:
                    prod *= ((xi)//(xi-xj))
            
            prod *= yj
            sums += prod
        return int(sums)

    def generate_shares(self,n, t, secret, p, q, r, g):
        FIELD_SIZE = q
        coefficients = self.coeff(t, secret, FIELD_SIZE)

        shares = []
        for i in range(1, n+1):
            f_i = self.f(i, coefficients, q)
            shares.append((i, f_i))

        commitments = self.commitment(coefficients, g, p)
        verifications = []
        for i in range(1, n+1):
            #check1 = g ** shares[i-1][1] % p
            check1 = pow(g, shares[i-1][1], p)
            check2 = self.verification(g, commitments, i, p)
            verifications.append(check2)
            #print("i-th share:", check1)
            #print("i-th verification:", check2)

        return shares, commitments, verifications


    def get_generated_shares(self,secret):
        shares_str=[]
        t, n = 2,3
        p, q, r, g = self.initial(10**2)
        shares, commitments, verifications = self.generate_shares(
            n, t, secret, p, q, r, g)

        for share in shares:
            shares_str.append(str(share))
            
        #print(
        #    f'Commitments: {", ".join(str(commitment) for commitment in commitments)}')
        #print(
        #    f'verifications: {", ".join(str(verification) for verification in verifications)}')
        return shares_str
            
    def recoverSecret(self,string_list):
        collected_shares = []
        t=2
        for i in string_list:
            i=i.split("(")
            i=i[1].split(")")
            i=i[0].split(",")
            share=tuple((int(i[0]),int(i[1])))
            collected_shares.append(share)
            #print(share)
        #print(collected_shares)
        pool = random.sample(collected_shares, t)

        secret_reconstructed = self.reconstruct_secret(pool)
        return secret_reconstructed

# vss=VSS_Controller()
# # vss.initial()
# share_list=vss.get_generated_shares(937129139155039330165631526289)


# print(share_list)
# #share_string=['(1, 6578889241063373618814799278512664690219537121584225863598628970422114152702603886643212322371345210913859819637819904480910953581820912982068141951166248)', '(2, 13157778482126747237629598557025329376490155668872822452625266156774410475273897597959090420158398714057036673020544992374569951038852261525525475598706453)',  '(3, 19736667723190120856444397835537994062760774216161419041651903343126706797845191309274968517945452217200213526403270080268228948495883610068982809246246658)']
# #print(vss.recoverSecret(share_string))
# #share_string=['(1, 3696617999365661557961716249366563061662254308441446999869622682127213008021963258188913203976722887593241958283255495337055053180849153492338578861194650)', '(2, 7393235998731323115923432498733126119375590042587264725167253580184608185912616341050492183369154067415800950311416174086858150236908742546066349418763257)', '(3, 11089853998096984673885148748099689177088925776733082450464884478242003363803269423912071162761585247238359942339576852836661247292968331599794119976331864)']
# #print(vss.recoverSecret(share_string))
# #share_list=['(1, 4579161071908851489075484130644360676566995852005110566289345384082348916622500115047754329072827157793370410890389004860498526806865911461266680764520800)', '(2, 9158322143817702978150968261288721352111341788996537832601688202765537320058993752705792202855659280579435675836770559425576159617223210684173081354811380)', '(3, 13737483215726554467226452391933082027655687725987965098914031021448725723495487390363830076638491403365500940783152113990653792427580509907079481945101960)']
# #share_list=['(1, 1696900373914889897544161808588998043930134448040157988581313221054959977490919135637933369193696726459637166620314419374032983325234984615675864168607333)', '(2, 3393800747829779795088323617177996087860268896080315977162626442109919954981838271275866738387393452919274333240628838748065966650469969231351728337214656)', '(3, 5090701121744669692632485425766994131790403344120473965743939663164879932472757406913800107581090179378911499860943258122098949975704953847027592505821979)']
# #share_list=['(1,1529358219)','(2,1804090979)','(3,2078823739)']
# #share_list=['(1, 414598935588642357729835999113030879012)', '(2, 488915504256346251996297390794293546569)', '(3, 563232072924050146262758782475556214126)']
# #share_list=['(1, 9676978131702039184437831297247410475604650385053423220777068846834730482968269438542594670357347552052011964691728943911511572853185166697586828635258071)', '(2, 35937666695192982314204421091316664169588482949197078473138363709094661409744362891694416750000409645508585069228046008706204656926308183452468891149595889)', '(3, 78782065690472829389299769382207761085900416266726595031655876370849610610459590534782800463513477988140402279864046010971331208344158614703256995846639497)']
# #share_list=['(1, 142104309330931654732907379338)', '(2, 310754042463443741406853837841)', '(3, 585177361911800597615383325844)', '(4, 965374267676002223358495843347)']
# print(vss.recoverSecret(share_list))
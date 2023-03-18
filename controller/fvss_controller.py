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
        numberOfRabinTrials = 30
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrcandidate)
            if trialComposite(round_tester):
                return False
        return True
    
    def largePrime(self):
        while True:
            n = 512
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
        #q = self.largePrime()
        q=8999556512368032697017128097574374399769695316317344581789539102340039278190399662105641330020233699175672708836915655500977456233047846907971722612868077
        

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
        return int(y)%q


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


    # def reconstruct_secret(self, pool):
    #     sums = 0
    #     q=338860914350317570641740174226607162069

    #     for j, share_j in enumerate(pool):
    #         xj, yj = share_j
    #         prod = 1

    #         for i, share_i in enumerate(pool):
    #             xi, _ = share_i
    #             if i != j:
    #                 prod *= ((xi)//(xi-xj))
    #                 print(prod)
            
    #         prod *= yj
    #         print(prod)
    #         sums += prod
    #     sums=sums%q
    #     return int(sums)
    def reconstruct_secret(self,pool):
        x_s,y_s = [],[]
        q=8999556512368032697017128097574374399769695316317344581789539102340039278190399662105641330020233699175672708836915655500977456233047846907971722612868077
        for share in pool:
            x_s.append(share[0])
            y_s.append(share[1])
        out = self._lagrange_interpolate(0, x_s, y_s, q)
        return out
    def _lagrange_interpolate(self,x, x_s, y_s, p):
        k = len(x_s)
        assert k == len(set(x_s)), "points must be distinct"
        def PI(vals):  # upper-case PI -- product of inputs
            accum = 1
            for v in vals:
                accum *= v
            return accum
        nums = []  # avoid inexact division
        dens = []
        for i in range(k):
            others = list(x_s)
            cur = others.pop(i)
            nums.append(PI(x - o for o in others))
            dens.append(PI(cur - o for o in others))
        den = PI(dens)
        num = sum([self._divmod(nums[i] * den * y_s[i] % p, dens[i], p)
                for i in range(k)])
        return (self._divmod(num, den, p) + p) % p
    
    def _divmod(self,num, den, p):
        inv, _ = self._extended_gcd(den, p)
        return num * inv
    def _extended_gcd(self,a, b):
        x = 0
        last_x = 1
        y = 1
        last_y = 0
        while b != 0:
            quot = a // b
            a, b = b, a % b
            x, last_x = last_x - quot * x, x
            y, last_y = last_y - quot * y, y
        return last_x, last_y
    
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
        # pool=[]
        # pool.append(collected_shares[0])
        # pool.append(collected_shares[1])
        # print(pool)
        secret_reconstructed = self.reconstruct_secret(pool)
        return secret_reconstructed

# vss=VSS_Controller()
# # vss.initial()
# share_list=vss.get_generated_shares(115792089237316195423570985008687907853269984665640564039457584007913129639936)
# #print(share_list)

# print(vss.recoverSecret(share_list))
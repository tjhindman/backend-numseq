from numseq.fib import fib
from numseq.geo import sqr, cube, tri
from numseq.prime import is_prime, prime


print ("Fibonacci")
for i in range(10):
    print ("{}: {}".format(i, fib(i)))


print("Geometric numbers (square, triangle, cube)")
for i in range(10):
    print ("{}: {} {} {}".format(i, sqr(i), tri(i), cube(i)))


print ("Primes")
prime_list = prime(1000)
for p in prime_list[-10:]:
    print (p)
print ("Is 999981 prime? {}".format(is_prime(999981)))
print ("Is 999983 prime? {}".format(is_prime(999983)))
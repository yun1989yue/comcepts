'''
HashTable

0. Challenges
simple example, keys are integers, we can use an array to implement hashtable
There are two challenges when we wanna generalize hashtable
1) we may not wish to use N space for only n items when n << N
2) keys may not be integers, we can use hash function to map general keys to indices

1. Hash Functions
1) Goal of hash function is to map each key k to an integer ranged in [N], where N is the capacity of bucket array for a hashtable
2) if two key have same hash value, there is a collision, it can be dealt with, but we would better avoid it.
3) a good hash function minimizes collisions and fast and easy to be computed
4) hash function h(k) consists of:
  1) hash code, map key to integer
  2) compression function, maps hash code within range [N]
  The advantage of separating hash code from compression function free

2. Hash Codes
key <-> Hash Code (not restricted to [N], even may be negative), need to minimize collision
'''

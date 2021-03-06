# https://community.topcoder.com/stat?c=problem_statement&pm=15211&rd=17370

# Function calculates all divisors greater than 1 of the sum of the input list.
# Sequence is passed in as input.
def calc_divisors(seq):

    seq_sum = sum(seq)
    divisors = []
    for i in range(2,seq_sum):
        if seq_sum % i == 0:
            divisors.append(i)
    
    return divisors

# Generator takes two inputs: sequence 'A' and list of potential GCDs for that
# sequence. Yields largest GCDs of sequence A.
def try_divisors(A,divisors):

    global maxDivisor

    # If largest succesful divisor is greater than higher than the highet we have
    # found so far, then update.
    if A == []:
        if max(divisors) > maxDivisor:
            maxDivisor = max(divisors)
        yield maxDivisor

    n = len(A)
    
    # Cycle through combinations of A[0] + A[i] and see whether the sum is divisible
    # by any number in divisors list. Add succesful divisors to newDivisors list.
    # If no succcesful divisors then yield 1. Otherwise try out succesful divisors
    # on remainder of the list.
    for i in range(1,n):
        newDivisors = []
        for divisor in divisors:
            if divisor > maxDivisor and (A[0] + A[i]) % divisor == 0:
                    newDivisors.append(divisor)
        if newDivisors == []:
            yield 1
        else:
            for item in try_divisors((A[1:i] + A[i+1:]),newDivisors):
                yield item
    

# different test input sequences
S = [46, 78, 133, 92, 1, 23, 29, 67, 43, 111, 3908, 276, 13, 359, 20, 21]
T = [5,4,13,2]
U = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 
65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]

maxDivisor = 1
choice = U
print([item for item in try_divisors(choice,calc_divisors(choice)) if item != 1])


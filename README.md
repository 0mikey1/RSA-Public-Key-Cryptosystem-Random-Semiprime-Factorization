# RSA-Public-Key-Cryptosystem-Random-Semiprime-Factorization
This is an assignment that I completed for Fundamentals of Blockchain Technologies (CIS4731). 


The security of RSA public key cryptosystem relies on the fact that prime factorization of large integers is practically 
unsolvable due to the high time-complexity of its solution. Here is the reason:



Part of RSA's public key is a semiprime number that is the product of two very large prime numbers p and q. Although  is 
publicly available, both and  must remain secret; otherwise, RSA's private key can be easily calculated and RSA's securi
ty gets compromised.



q1.py 
________________

q1.py implements an experiment to find the time complexity of finding prime factors p and q of a given semiprime number n so that 
n = p x q. The experiment factorizes random semiprime integers n with different length from 32-bits to 64-bits. The code outputs 
the average time it takes for the program to factorize random semiprime integers. 



q3.py 
________________

q3.py contains two functions: 

def rsa_message_sign(message: str, d: int, n: int) -> int:
digest = hashlib.sha256(message.encode("ascii", "ignore"))
return pow(int(digest.hexdigest(),16), d, n)
    
    
def rsa_signature_verify(message: str, signature: int, e: int, n: int) -> bool:
expected_digest = pow(signature, e, n)
digest = int(hashlib.sha256(message.encode("ascii", "ignore")).hexdigest(), 16)
return expected_digest == digest
    
(We assume that (n,e) is a valid public-key and (n,d) is its corresponding private-key of an RSA cryptosystem.)
    
    
The function "rsa_message_sign" first finds the digest of given message using SHA-256 and then signs/encrypts it
by raising it to the power of integer d mod n. 
    
    
The function "rsa_signature_verify" first decrypts the given signature by raising it to the power of e mod n. Then, it compares 
the result with the digest of given message using SHA-256. If the values are equal, the given signature is verified 
for the given message. Otherwise, the signature is not verified.
    
    
    







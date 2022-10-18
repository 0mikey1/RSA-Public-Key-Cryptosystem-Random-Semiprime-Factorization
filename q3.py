import hashlib

message = "Your checking account available balance is 12,444,290 dollars and 56 cents."
signature = 0x230e2ee7c95e6c1faae818682fa25f19d3148077de82a30c44618f397fb0309fc4fe545e6cda6c46dbe81aea4ad76cf3c6ed5066df1a6b1f187063d6cb3f8da69675e91cb9ffea6a79814bd27153f04cfd143d519f8ce0025cc1205c2472294343f14a2d041ddc3821359638638a96d58e6b99a904f6099eea9c74012dd64569
n = 0x97987cc9520bf98c049dd4fdd0b2ef50a8cd876bc89b3f43708a8d26e05a2923a312688cd2a50d8e01fa3e20181387d07e9b75d00ad07b2e302983cf16b56bb4dbeeeb2709a22053c44fc743abcac8fc8511b97062ac8c298feeebce70c6851a6752b4f27a8a0fbdd3b202e3e10ea48a912d31f96ecb7bf8fe86934a9b466b71
e = 0x10001
d = 0x95e378e699902b826d021d99846397ca19cd75eb756342ef0c7481d2019c43f6ef83010ad42fcc322ff45cbee0ef56a728b7cf8a0f5749a4468c95bd29397427f3316bbfa4902bb8cc5a6ea572ff24368f17ff952c6965ffc1d5d467ce06fab9e87833fe3438d1a69cfdac2c4e20fa0f5793fdbc1057073d3dbb12f613d52b9d


def rsa_message_sign(message: str, d: int, n: int) -> int:
    digest = hashlib.sha256(message.encode("ascii", "ignore"))
    return pow(int(digest.hexdigest(),16), d, n)


def rsa_signature_verify(message: str, signature: int, e: int, n: int) -> bool:
    expected_digest = pow(signature, e, n)
    digest = int(hashlib.sha256(message.encode("ascii", "ignore")).hexdigest(), 16)
    return expected_digest == digest


print(rsa_message_sign(message, d, n))
print(rsa_signature_verify(message,signature, e, n))
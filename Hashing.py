import hashlib as hl
# print(hl.algorithms_available)
# print("Guaranteed hash ")
# # print(hl.algorithms_guaranteed)
# message = 'the quick brown fox jumps over the lazy dog'
# hasher = hl.sha1(message.encode())
# print(hasher.hexdigest())
# message1 = 'the quick brown  fox jumps over the lazy dog'
# hasher1 = hl.sha1(message1.encode())
# print(hasher1.hexdigest())
message = 'Rouf'
hasher = hl.sha1(message.encode())
print(hasher.hexdigest())
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand_count = {}
        for i in hand:
            hand_count[i] = hand_count.get(i, 0) + 1
        
        hand_val = sorted(list(hand_count.keys()))

        while len(hand_val):
            key = hand_val[0]
            if hand_count[key] > 0:
                for i in range(groupSize):
                    key_count = hand_count.get(key + i, 0)
                    if key_count == 0:
                        return False
                    new_count = key_count - 1
                    hand_count[key + i] = new_count
                    if new_count == 0:
                        hand_val.remove(key + i)

        return True
                
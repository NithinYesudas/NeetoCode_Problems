class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        grumpySum = 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                grumpySum+=customers[i]
        satisfied = grumpySum
        for i in range(len(customers)):
            curr = grumpySum
            if grumpy[i]==0 or (customers[i]==0 and grumpy[i]==1):
                continue
            for j in range(i, min(len(customers),i+minutes)):
                if grumpy[j]==1:
                    curr+=customers[j]
            satisfied = max(curr,satisfied)
        return satisfied
        
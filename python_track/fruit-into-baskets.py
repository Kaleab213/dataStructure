class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left_pointer = answer = 0
        fruit_basket = defaultdict(int)
        for right_pointer in range(len(fruits)):
            fruit_basket[fruits[right_pointer]] += 1
            while len(fruit_basket) > 2:
                fruit_basket[fruits[left_pointer]] -= 1
                if fruit_basket[fruits[left_pointer]] == 0:
                    fruit_basket.pop(fruits[left_pointer])
                left_pointer += 1
            answer = max(answer, right_pointer - left_pointer + 1)
        return answer

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for rowidx in range(len(image)):
            image[rowidx] = image[rowidx][::-1]
            for colidx in range(len(image[0])):
                if image[rowidx][colidx]:
                    image[rowidx][colidx] = 0
                else:
                    image[rowidx][colidx] = 1
        return image
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_size = len(s)
        t_size = len(t)
        s_pointer = 0
        t_pointer = 0

        if s_size < t_size:
            return 0

        result_matrix = []
        for i in range(s_size):
            result_matrix.append([0]*t_size)

        starting_letter_count = 0
        while s_pointer < s_size:
            if s[s_pointer] == t[t_pointer]:
                starting_letter_count += 1
            result_matrix[s_pointer][t_pointer] = starting_letter_count
            s_pointer += 1
        for s_pointer in range(1, s_size):
            for t_pointer in range(1, t_size):
                result_matrix[s_pointer][t_pointer] = result_matrix[s_pointer - 1][t_pointer]
                if (s[s_pointer] == t[t_pointer]) :
                    if s[s_pointer] == t[t_pointer-1]:
                        result_matrix[s_pointer][t_pointer] += result_matrix[s_pointer-1][t_pointer - 1]
                    elif (t[t_pointer] != t[t_pointer - 1]):
                        result_matrix[s_pointer][t_pointer] += result_matrix[s_pointer][t_pointer - 1]
        return result_matrix[s_size-1][t_size-1]
class solution:
    def roman(self, x):
        r_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i_val = 0
        for i in range(len(x)):
            if i > 0 and r_val[x[i]] > r_val[x[i - 1]]:
                i_val += r_val[x[i]] - 2 * r_val[x[i - 1]]
            else:
                i_val += r_val[x[i]]
        return i_val
print(solution().roman(input()))        

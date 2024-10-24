# print('123456789abcde')
# print('|{:^12.7f}|'.format(-0.11241414691))

digits = '0123456789'

A = '456fgsg'
for i in A:
    if i in digits:
        A = A.replace(i, ' ')
    
print(A)
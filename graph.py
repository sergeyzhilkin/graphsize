
def fsize(a):
    f = []  # list of figures
     
     # check first list in a
    for i,v in enumerate(a[0]):
        if v == 1:
            if i == 0:
                f.append([[i],1])
            else:
                 # check left 
                if a[0][i - 1] == 1:
                    for index_f, figure in enumerate(f):
                        if (i - 1) in figure[0]:
                            f[index_f][0].append(i)
                            f[index_f][1] = f[index_f][1] + 1
                else:
                    f.append([[i],1])
     
     # check all other lists in a        
    for k in range(1,len(a)):
        for i,v in enumerate(a[k]):
            check_top = False
            left_fig_index = 'none'
            if v == 0:
                for index_f, figure in enumerate(f):
                    if i in figure[0]:
                        f[index_f][0].remove(i)
            if v == 1:
                 # check left 
                if i != 0:  
                    if a[k][i - 1] == 1:
                        for index_f, figure in enumerate(f):
                            if (i - 1) in figure[0]:
                                if i not in figure[0]:
                                    f[index_f][0].append(i)
                                left_fig_index = index_f
                                f[index_f][1] = f[index_f][1] + 1
                 # check top
                for index_f, figure in enumerate(f):
                    if i in figure[0]:
                        check_top = True
                        if left_fig_index == 'none':
                            f[index_f][1] = f[index_f][1] + 1  
                        if index_f != left_fig_index and left_fig_index != 'none':
                             # merge left figure and figure
                            f[left_fig_index][0].extend(f[index_f][0])
                            f[left_fig_index][1] = f[left_fig_index][1] + f[index_f][1]
                            f[left_fig_index][0].remove(i)
                            left_fig_index == 'none'
                            del f[index_f]
                if left_fig_index == 'none' and check_top == False:
                    f.append([[i],1])  
    b = []
    for i in f:
        b.append(i[1])    

    for i in range(len(a)):
        print(a[i])
    print(' ')
    print(f'number of figures: {len(f)}')
    print(f'size of the biggest figure: {max(b)}')

if __name__ == '__main__':
    a = [
         [1,1,0,0,1],
         [1,1,0,0,0],
         [0,0,0,1,0],
         [0,0,1,1,1],
         [0,0,0,1,0]
    ]
    fsize(a)         

import matplotlib.pyplot as plt
import numpy as np

plt.subplot()
'''
#Sorted List
plt.plot([350 ,426 ,164 ,510 ,473 ,139 ,334 ,340 ,779 ,941 ,173 ,541 ,736 ,884 ],
         [258 , 168 ,461,67 ,298 ,655 ,640 ,640 ,392 ,218 ,956 ,826 ,769 ,795 ],
         color='green',label='Sorted List',marker='D', markersize=15)

#plt.xlabel('x axis')
'''

#Random List
plt.scatter([541, 334, 736, 350, 173, 779, 164, 941, 884, 340, 426, 473, 510, 139],
         [826, 640, 769, 258, 956, 392, 461, 218, 795, 640, 168, 298, 67, 655],
            c='b', alpha=1, marker='*')
plt.ylabel('14 Cities generated at random')
'''
#Opt_list with Matrix
plt.plot([350, 426, 779, 139, 473, 340, 334, 884, 736, 541, 173, 164, 510, 941],
         [258, 168, 392, 655, 298, 640, 640, 795, 769, 826, 956, 461, 67, 218],
         'c', marker='D', markersize=15, label='Opt_list with Matrix')

#Opt_list w/o matrix
plt.plot([350, 426, 510, 473, 779, 941, 884, 736, 541, 340, 334, 139, 164, 173],
         [258, 168, 67, 298, 392, 218, 795, 769, 826, 640, 640, 655, 461, 956],
         'm', marker='h', markersize=15, label='Opt_list w/o Matrix')
'''
plt.show()
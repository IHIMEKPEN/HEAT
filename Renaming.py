import os


def rename():
     for count , filename in enumerate(os.listdir(r'/home/andre/Pictures/ose/')):
         dst='ose' + str(count) + '.jpg'
         src='/home/andre/Pictures/ose/' + filename
         dst='/home/andre/Pictures/ose/' + dst
         os.rename(src,dst)

rename()     

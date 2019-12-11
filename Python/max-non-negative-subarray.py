https://www.interviewbit.com/problems/max-non-negative-subarray/

class Solution:
    # @param A : list of integers
    # @return a list of integers

    def maxset(self, A):
        maxsumlist = []
        cursumlist = []

        maxsum = 0
        currsum = 0

        for i in A:
            if (i >= 0):
                currsum = currsum + i #add every element to current sum 
                cursumlist.append(i) #append it to current list 
                
                if(currsum > maxsum):
                    #if currsum is greater than previous global maximum sum
                    #replace it with current sum and list
                    maxsum = currsum
                    maxsumlist = cursumlist
                    
                elif(currsum == maxsum):
                    # in case if the sum remains same, but list size has increased, modify maxsumlist
                    if(len(cursumlist) > len(maxsumlist)):
                        maxsumlist = cursumlist
                    
            elif(i<0):
                #if current sum is negative, empty the current list
                currsum = 0
                cursumlist = []
                    
        return maxsumlist
        
        

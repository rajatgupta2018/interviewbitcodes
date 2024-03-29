https://www.interviewbit.com/problems/min-steps-in-infinite-grid/


int Solution::coverPoints(vector<int> &A, vector<int> &B) {
    int dist=0;
    
    for (int i=0;i<A.size()-1;i++)
    {
        if( abs(A[i]-A[i+1]) <= abs(B[i]-B[i+1])    )
            dist+=abs(B[i]-B[i+1]);
        else
            dist+=abs(A[i]-A[i+1]);
    }
    return dist;

}

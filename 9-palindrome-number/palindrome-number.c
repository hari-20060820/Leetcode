bool isPalindrome(int x) {
    long int sum=0;
    long int cp=x;
    while(x!=0)
    {
        sum=sum*10+(x%10);
        x=x/10;
    }
    if(sum==cp&& cp>=0)
    return true;
    else
    return false;
}
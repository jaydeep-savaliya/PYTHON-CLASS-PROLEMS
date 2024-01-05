def digital_root(n):
    ans = 0
    while n>0:
        ans+=n%10
        n=n//10
    return ans if ans<=9 else digital_root(ans)
print(digital_root(451515))
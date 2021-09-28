#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
const int N=1010,inf=0x3f3f3f3f,mod=1000007;
int n,m,res;
int a[N],dp[N][N];//dp[i][j]表示以a[i]结尾长度为j的子序列个数

int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>a[i],dp[i][1]=1;//初始化
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            for(int k=1;k<i;k++){
                if(a[i]>a[k])
                    dp[i][j]+=dp[k][j-1];
            }
        }
    }
    for(int i=1;i<=n;i++){
        res=(res+dp[i][m])%mod;
    }
    cout<<res<<endl;
return 0;
}


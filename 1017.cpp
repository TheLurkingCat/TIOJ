#include <iostream>
#include <cstdio>

using namespace std;

int T, N;
int S[2000000], min_value[2000000], max_value[2000000];

int main()
{
    scanf("%d", & T);
    while(T--)
    {
        int ans = 0;
        scanf("%d", & N);
        for(int i=0; i < N; i++)
        scanf("%d", & S[i]);
        max_value[0] = S[0];

        for(int i=1; i < N; i++)
        max_value[i] = max(max_value[i-1], S[i]);

        min_value[N-1] = S[N-1];

        for(int i=N-2; i >= 0; i--)
        min_value[i] = min(min_value[i+1], S[i]);

        for(int i=1;
            i < N-1;
            i++)
        if(S[i] > max_value[i-1] && S[i] < min_value[i+1]) ans++;

        printf("%d\n", ans);
    }
}

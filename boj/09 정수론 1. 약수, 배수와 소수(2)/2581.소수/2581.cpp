#include <iostream>
#include <vector>

using namespace std;

vector<int> sieve(int n){
  vector<bool> is_prime(n + 1, true);

  if(n >= 0)  is_prime[0] = false;
  if(n >= 1)  is_prime[1] = false;

  for(int i = 2; (long long)i * i <= n; i++){
    if(is_prime[i]){
      for(long long j = (long long) i * i; j <= n; j += i){
        is_prime[j] = false;
      }
    }
  }

  vector<int> primes;
  for(int i = 2; i <= n; i++)
    if(is_prime[i]) primes.push_back(i);
  
  return primes;
}

int main(){
  int m, n;
  cin >> m >> n;

  vector<int> primes = sieve(n);

  int sum_p = 0, min_p = -1;
  for(int i = 0; i < primes.size(); i++){
    if(primes[i] >= m){
      if(min_p == -1) min_p = primes[i];
      sum_p += primes[i];
    }
  }
  if(min_p == -1) cout << -1;
  else  cout << sum_p << '\n' << min_p;
}
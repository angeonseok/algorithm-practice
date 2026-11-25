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
  int n;
  cin >> n;

  vector<int> primes = sieve(n);

  for(auto x : primes){
    if(x * x > n)  break;

    while(n % x == 0){
      cout << x << '\n';
      n /= x;
    }
  }

  if(n > 1) cout << n;
}
#include <iostream>
#include <time.h>
using namespace std;

int lucky_number = (time(0) % 10) + 1;
int start = 5 ;
int score;

bool play_again ()
{
  char ans;
  cout << "_____________________________________" << endl;
  cout << "Do you want to play again?.....(Y/N): " << endl;
  cout << "_____________________________________" << endl;
  cin >> ans;
   switch (ans)
   {
    case 'Y' :
    {
      cout << "Great!! Lets Play Again....." << endl;
      cout << endl;
      return true;
    }
    case 'N' :
    {
      cout << endl;
      cout << "Thanks For Playing The Game :)" << endl;
      return false;
    }
    default:
    {
      cout <<"Invalid Input! Please try again... " << endl;
      play_again();
    }
   }
   return 0;
}

bool guessing ()
{
int guess ;
cout << "________________________" << endl;
cout << "Guess the Lucky Number : " ;
cin >> guess ;
cout << endl;

if (guess > 10 || 0 > guess )
{
 cout << "Invalid Number! " << endl;
 cout << "Please enter a number between 1 and 10 only" << endl;
 cout << endl;
 guessing();
}
else
{
    cout << "So your Guess Is ==> " << guess << endl;
    if(guess == lucky_number)
    {
        cout << "****************************************" << endl;
        cout << "YOU ARE LUCKY! , YOU GUESSED IT RIGHT :D" << endl; 
        cout << "****************************************" << endl;
        cout << endl;
        cout << "Your SCORE is ==> " <<  score << endl;
        cout << endl;
        bool answer = play_again();
        return answer;
    }
    else 
    {
        cout << "OOPS! YOU GUESSED IT WRONG, TRY AGAIN " << endl;
        cout << endl;
        score  = score - 1 ;
        cout << "CHANCES LEFT ==> " << score ;
        cout << endl ;
        if (score == 0)
        {
          cout << "..................................." << endl;
          cout << "YOU ARE UNLUCKY!, YOU LOST THE GAME " << endl ;
          cout << "..................................." << endl ;
         bool answer = play_again();
         return answer ;
        }
        else 
        {
          guessing();
        }
    }
}
}

int main ()
{
score = start;
cout << lucky_number << endl;
cout << "----------------------------" << endl;
cout << "** WELCOME TO THE GAME! **" << endl ;
cout << "----------------------------" << endl ;
cout << endl;
cout << "You have 5 chances to win the game" << endl ;
cout << "The Number will be between 1 and 10 " << endl ;
cout << "******BEST OF LUCK!******" << endl ;
cout << endl;
bool user_choice = guessing();

if (user_choice)
{
  main();
}
else
{
  return 0;
}

}


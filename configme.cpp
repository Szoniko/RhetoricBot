#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string auth;
char redditCommands;
string client_id;
string client_secret;
string user_agent;
string username;
string password;
string prefix;

int main()
{
    cout << "Hi, this program is the config for your discord bot. (none of this will be shared)\n";
    
    //discord
    ofstream file;
    file.open("config.py");
    cout << "First of all, what is you discord bot token: ";
    cin >> auth;
   
   //importing hypixel
    file << "import hypixel\n\nauth = \"" + auth + "\"\n\n";

    //reddit
    cout << "\nGreat, next you will need to put in your reddit information to use reddit commands in the future. (memes, etx)\nWould you like reddit commands in your bot? y/n: ";
    cin >> redditCommands;

    switch (redditCommands)
    {
        case 'y':
            file << "reddit = praw.Reddit(\n";
            cout << "\nclient id (found under apps on your reddit account): ";
            cin >> client_id; file << "    client_id=\"" + client_id + "\",\n";
            cout << "\nclient secret (found under apps on your reddit account): ";
            cin >> client_secret; file << "    client_secret=\"" + client_secret + "\",\n";
            cout << "\nuser agent (this can be anything): ";
            cin >> user_agent; file << "    user_agent=\"" + user_agent + "\",\n";
            cout << "\nusername: ";
            cin >> username; file << "    username=\"" + username + "\",\n";
            cout << "\npassword: ";
            cin >> password; file << "    password=\"" + password + "\")\n";
            break;
        
        case 'n':
            break;
        
        default:
            cout << "That's invalid. I will take that as a no.";
            break;

    }

    //prefix
    cout << "\nWhat would you like the prefix of your bot to be: ";
    cin >> prefix; file << "\ncommand_prefix = \"" + prefix + "\"";

    //closing the file
    file.close();

    //goodbye
    cout << "\nYou should be ready to run you bot! (of course with no commands yet.)";
}

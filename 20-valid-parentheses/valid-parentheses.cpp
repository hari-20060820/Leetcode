#define MAXI 20000
class Solution {
public:
    char stack[MAXI];
    int pointer = 0;

    void push(char ch) {
        if (pointer < MAXI) {pointer++;
            stack[pointer] = ch;
            
        } else
            return;
    }
    char pop() {
        char ch;
        if (pointer > 0) {
            ch = stack[pointer];
            pointer--;
        }
         

        return ch;
    }
    bool isValid(string s) {
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                push(s[i]);
            }
            
            if (!(s[i] == '(' || s[i] == '{' || s[i] == '[')) {
                if(pointer==0)
            {
                return false;
            }
                char ch = pop();
                if ((ch == '(' && s[i] != ')') || (ch == '{' && s[i] != '}') ||
                    (ch == '[' && s[i] != ']')) { // the false need to verified only once so
                                     // we can use this for our program.
                    return false;
                }
            }
        }
        return pointer==0;
    }
};
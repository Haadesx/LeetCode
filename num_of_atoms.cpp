// Given a string formula representing a chemical formula, return the count of each atom.

// The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

// One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

// For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
// Two formulas are concatenated together to produce another formula.

// For example, "H2O2He3Mg4" is also a formula.
// A formula placed in parentheses, and a count (optionally added) is also a formula.

// For example, "(H2O2)" and "(H2O2)3" are formulas.
// Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

// The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

// Example 1:

// Input: formula = "H2O"
// Output: "H2O"
// Explanation: The count of elements are {'H': 2, 'O': 1}.
// Example 2:

// Input: formula = "Mg(OH)2"
// Output: "H2MgO2"
// Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
// Example 3:

// Input: formula = "K4(ON(SO3)2)2"
// Output: "K4N2O14S4"
// Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

// Constraints:

// 1 <= formula.length <= 1000
// formula consists of English letters, digits, '(', and ')'.
// formula is always valid.














#include <iostream>
#include <string>
#include <stack>
#include <map>
#include <cctype>
#include <algorithm>

class Solution {
public:
    std::string countOfAtoms(std::string formula) {
        std::stack<std::map<std::string, int>> stk;
        stk.push({});
        int n = formula.size();
        
        for (int i = 0; i < n; ) {
            if (formula[i] == '(') {
                stk.push({});
                i++;
            } else if (formula[i] == ')') {
                auto top = stk.top();
                stk.pop();
                i++;
                int count = 0;
                while (i < n && isdigit(formula[i])) {
                    count = count * 10 + formula[i] - '0';
                    i++;
                }
                if (count == 0) count = 1;
                for (auto &[atom, cnt] : top) {
                    stk.top()[atom] += cnt * count;
                }
            } else {
                int start = i++;
                while (i < n && islower(formula[i])) i++;
                std::string atom = formula.substr(start, i - start);
                int count = 0;
                while (i < n && isdigit(formula[i])) {
                    count = count * 10 + formula[i] - '0';
                    i++;
                }
                if (count == 0) count = 1;
                stk.top()[atom] += count;
            }
        }
        
        auto &final_counts = stk.top();
        std::string result;
        for (auto &pair : final_counts) {
            result += pair.first;
            if (pair.second > 1) result += std::to_string(pair.second);
        }
        return result;
    }
};

int main() {
    Solution solution;
    std::cout << solution.countOfAtoms("H2O") << std::endl;         // "H2O"
    std::cout << solution.countOfAtoms("Mg(OH)2") << std::endl;     // "H2MgO2"
    std::cout << solution.countOfAtoms("K4(ON(SO3)2)2") << std::endl; // "K4N2O14S4"
    return 0;
}

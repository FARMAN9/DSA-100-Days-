def isomorphic_strings(s, t):
    # Check if lengths are equal; if not, the strings can't be isomorphic
    if len(s) != len(t):
        return False
    
    # Create dictionaries to map characters from s to t and t to s
    hashtable = {}
    hashtable2 = {}

    # Iterate through the entire length of the strings
    for i in range(len(s)):
        charS = s[i]
        charT = t[i]

        # Update mappings if not already present
        if charS not in hashtable:
            hashtable[charS] = charT

        if charT not in hashtable2:
            hashtable2[charT] = charS

        # If there is a mismatch in the mappings, return False
        if hashtable[charS] != charT or hashtable2[charT] != charS:
            return False

    # If no mismatches found, the strings are isomorphic
    return True

# Example usage
print(isomorphic_strings('abcd', 'efgh'))  # Output: True




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = len(set(zip(s,t)))
        b = len(set(s))
        c = len(set(t))
        return a == b == c
"""
Filename : galeShapley.py
Author : Archit Satish Joshi
Description : Python implementation of Gale-Shapley algorithm for stable
              matching.
Language : python3
Revisions :
v1.0 - Basic algorithm structure
v1.1 - Moved to class structure
v1.2 - Testing and Debugging complete
"""

"""
Implementation of the Gale-Shapley algorithm for stable matching.
Reference - Algorithm Design (1st Edition) by Jon Kleinberg and Eva Tardos 2005
Page Number - Page 6
"""


class StableMatching:
    """
    Class to solve the stable matching problem
    """

    __slots__ = 'free', 'matched', 'responders', 'requestors'
    """
    free : list of free requestors
    matched : ordered pair of currently matched requestors (men) and responders 
    (women)
    requestors : preference list of requestors (men)
    responders : preference list of responders (women)
    """

    def __init__(self):
        """
        Constructor.

        :return: None
        """
        self.free = []
        self.matched = []
        self.requestors = {}
        self.responders = {}

    def parseInput(self):
        """
        Function to parse input.
        Create preference list for requestors and responders.
        Complexity : O(n^2)

        :return: None
        """

        n = int(input("Enter total number of men and women : "))
        # preference list for requestor / men
        print("\nPreference list for requestors")
        for i in range(n):
            x = input(f"Insert preference list for man {i + 1} : ").split()
            lst = [int(y) for y in x]
            self.requestors[i+1] = lst

        # preference list for responder / women
        print("\nPreference list for responders")
        for i in range(n):
            y = input(f"Insert preference list for woman {i + 1} :").split()
            lst = [int(x) for x in y]
            self.responders[i+1] = lst

    def galeShapley(self):
        """
        Wrapper function to initiate stable matching using gale shapley
        algorithm.

        :return: None
        """
        # Initially all requestors are free
        for requestor in self.requestors.keys():
            self.free.append(requestor)

        # Continue matching until no requestor is free
        while len(self.free) > 0:
            self._galeShapley(self.free[0])

    def _galeShapley(self, requestor):
        """
        Gale Shapley algorithm to find a stable matching given requestor and
        responder preference lists.

        :param requestor: requestor chosen from the pool of free requestors
        :return: None
        """
        for preference in self.requestors[requestor]:
            # Case 1: Check if the preference is already matched
            current_match = self.getCurrentMatch(preference)

            # If the current requestor's preference doesnt have a match,
            # they can be matched
            if not current_match:
                self.matched.append([requestor, preference])
                self.free.remove(requestor)
                break

            # Preference is already matched. Check responder preferences
            else:

                # Get ranking of responders current match and check for upgrade
                current_idx = self.responders[preference].index(
                    current_match[0])
                new_idx = self.responders[preference].index(requestor)

                # Case 2 : Current requestor is lower ranked than existing match
                if new_idx < current_idx:
                    # Remove current match and add requestor to free list
                    self.free.append(current_match[0])
                    self.matched.remove(current_match)

                    self.free.remove(requestor)
                    self.matched.append([requestor, preference])
                    break

                # Case 3 : Preference is happy with current match
                else:
                    # Do nothing
                    pass

    def getCurrentMatch(self, responder):
        """
        Helper function to check if the current responder is already matched to
        any requestor.

        :param responder:
        :return:
        """

        for match in self.matched:
            if match[1] == responder:
                return match


def main():
    s = StableMatching()
    s.parseInput()
    s.galeShapley()
    print("\nStable Matching (requestor, responder) : ")
    print(s.matched)


if __name__ == "__main__":
    main()
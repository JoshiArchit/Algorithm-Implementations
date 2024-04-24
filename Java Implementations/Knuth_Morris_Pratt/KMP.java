package Knuth_Morris_Pratt;

/**
 * KMP.java
 * Author : Archit Joshi
 * Version :
 * Revisions :
 */

public class KMP {

    /**
     * Naive approach to find all occurrences of a substring in a string
     * Complexity : O(mn) where n is the length of the original string and
     * m is the length of the substring
     */
    public static void findSubstring( String str1, String str2 ) {

        int n = str1.length();
        int m = str2.length();
        for( int i = 0; i <= n - m; i++ ) {
            int j;
            for( j = 0; j < m; j++ ) {
                if( str1.charAt( i + j ) != str2.charAt( j ) ) {
                    break;
                }
            }
            if( j == m ) {
                System.out.println( "Substring found at index " + i );
            }
        }
    }

    /**
     * KMP algorithm to find all occurrences of a substring in a string
     * Complexity : O(n + m) where n is the length of the original string and
     * m is the length of the substring
     */
    public static void findSubstringKMP(String str1, String str2){
        int n = str1.length();
        int m = str2.length();

        // Construct the LPS(The Longest Prefix Suffix) array
        int[] lps = new int[m];
        // Length of the previous longest prefix suffix
        int len = 0;
        // The loop calculates lps[i] for i = 1 to m-1
        int i = 1;
        while(i < m) {
            // If the characters match, increment the length and store it in
            // the LPS array (helps in backtracking)

            // For easier debugging
            char c1 = str2.charAt( i );
            char c2 = str2.charAt( len );
            if (c1 == c2) {
                len++;
                lps[i] = len;
                // Move to the next character
                i++;
            } else {
                // If the characters do not match
                if (len != 0) {
                    // Backtrack to the previous character
                    len = lps[len - 1];
                } else {
                    // If the length is 0, store 0 in the LPS array
                    lps[i] = 0;
                    i++;
                }
            }
        }

        // Use the LPS array to find the substring
        int i1 = 0;
        int i2 = 0;

        // Loop through the original string
        while(i1 < n) {
            // For easier debugging
            char c1 = str1.charAt( i1 );
            char c2 = str2.charAt( i2 );
            // If the characters match, increment both i1 and i2
            if(c1 == c2) {
                i1 ++;
                i2 ++;
            } else {
                // Characters don't match
                if(i2 != 0) {
                    // Backtrack to the previous character
                    i2 = lps[i2 - 1];
                } else {
                    // Move to the next character
                    i1 ++;
                }
            }
        }

        // If the substring is found
        if(i2 == m) {
            System.out.println("Substring found at index " + (i1 - i2));
        }

    }

    public static void main( String[] args ) {
        // Original large string
        String str1 = "ababcabcabababd";
        // Substring to be matched
        String str2 = "ababd";
        // Find the substring using the naive approach
        findSubstring( str1, str2 );
        // Find the substring using the KMP algorithm
        findSubstringKMP( str1, str2 );
    }
}
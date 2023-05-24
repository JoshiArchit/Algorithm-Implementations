<b>Problem Description :</b>

Given an equal number of men and women to be paired for marriage, each man ranks all the women in order of his preference and each women ranks all the men in order of her preference.

A stable set of engagements for marriage is one where no man prefers a women over the one he is engaged to, where that other woman also prefers that man over the one she is engaged to. I.e. with consulting marriages, there would be no reason for the engagements between the people to change.

Gale and Shapley proved that there is a stable set of engagements for any set of preferences and the first link above gives their algorithm for finding a set of stable engagements.

<b>Input Specifications :</b>
1. 'n' number of men and women.
2. Dictionary 'requestors' which contains the preference 
   list 
   for each 
   man (requestor).
   <p>a. The woman the i<sup>th</sup> man prefers the most will be at 
   preference[i][0].</p>
   <p>b. The woman the i<sup>th</sup> man prefers the least will be at
   preference[i][n-1].</p>
3. Dictionary 'responders' which contains the preference 
   list 
   for each 
   woman (responder).
   <p>a. The man the i<sup>th</sup> woman prefers the most will be at 
   preference[i][0].</p>
   <p>b. The man the i<sup>th</sup> woman prefers the least will be at
   preference[i][n-1].</p>
<p>Preferences are labelled from 1 to n.</p>
<p>Preference input for the i<sup>th</sup> man/woman is a list of integers 
given in a 
single 
line separated by space</p>


---

<p>Expected console text for input from the console -</p>
Enter total number of men and women : 5

Preference list for requestors
<p>Insert preference list for man 1 : 2 1 4 5 3
<p>Insert preference list for man 2 : 4 2 1 3 5
<p>Insert preference list for man 3 : 2 5 3 4 1
<p>Insert preference list for man 4 : 1 4 3 2 5
<p>Insert preference list for man 5 : 2 4 1 5 3

Preference list for responders
<p>Insert preference list for woman 1 :5 1 2 4 3</p>
<p>Insert preference list for woman 2 :3 2 4 1 5</p>
<p>Insert preference list for woman 3 :2 3 4 5 1</p>
<p>Insert preference list for woman 4 :1 5 4 3 2</p>
<p>Insert preference list for woman 5 :4 2 5 3 1</p>

---



<b>Pseudo Code</b>
```commandline
Initially all m ∈ M and w ∈ W are free
While there is a man m who is free and hasn’t proposed to
every woman
    Choose such a man m
    Let w be the highest-ranked woman in m’s preference list
        to whom m has not yet proposed
    If w is free then
        (m, w) become engaged
    Else w is currently engaged to m′
        If w prefers m′ to m then
            m remains free
        Else w prefers m to m′
            (m, w) become engaged
            m′ becomes free
        Endif
    Endif
Endwhile
Return the set S of engaged pairs
```



Additional information can be reviewed in the sources from README.md
# Artificial Intelligence and Logic Programming Assignment 1 automarker #
1. Download student files from FEN.
2. To generate tests do:
    ```
    ./automark.sh gentest
    ```
  make sure that `test1.pl` is in the same directory as `automark.sh`

3. Do `./automark.sh /path/to/ASGNM1`.

## Answers comparison ##
If you need to compare answers for the *q4* then do the following in `swipl` interpreter:
```
['ailp/library/assignment1_automarkrc.pl'].

ailp_start_position(A),q4a(B),answerQ4a(A,B).
ailp_start_position(A),q4b(B),answerQ4b(A,B).
ailp_start_position(A),q4c(B),answerQ4c(A,B).
ailp_start_position(A),q4d(B),answerQ4d(A,B).

ailp_start_position(A),q4a(B),reverse(B,C),answerQ4a(A,C).
ailp_start_position(A),q4b(B),reverse(B,C),answerQ4b(A,C).
ailp_start_position(A),q4c(B),reverse(B,C),answerQ4c(A,C).
ailp_start_position(A),q4d(B),reverse(B,C),answerQ4d(A,C).
```

## Marking criteria ##
The mark break-down is as follows:
```
Q1:    1
Q2a:   1
Q2b:   1
Q3:    1
Q4a:   2
Q4b:   2
Q4c:   2
Q4d:   2
Q5a:   3
Q5b:   3
Q6:    5
Extra: 2
```

Part of the assignment needs to be marked manually. In the section below there is an example output for one student. This is generated by the automarker, and then the marks at the top are added; Q's 5 and 6 are marked manually.  
If part of the Q4 is wrong it is advised to check why and if the answer is almost correct give 1 or 2 marks; e.g. if the path is right but in reverse.  
Sometimes the automarker fails because the answers are malformated, in which case they need manual marking.

## Example auto-marker output ##
```
Marks breakdown
q1: 1/1 
q2a: 1/1 
q2b: 1/1 
q3: 1/1 
q4a: 2/2 
q4b: 2/2 
q4c: 2/2 
q4d: 2/2 
q5a: 3/3 
q5b: 3/3 
q6: 3/5 
extra: 0/2 
Total: 21/25

=-=-=-=-=-=-=-= Output of automark follows =-=-=-=-=-=-=-=


*** Queries for q1 ***

LISTING answers to ?-q1(A).
     q1(ailp_start_position(A)).


*** Queries for q2a ***

LISTING answers to ?-q2a(A).
     q2a(new_pos(p(1, 1), e, A)).


*** Queries for q2b ***

LISTING answers to ?-q2b(A).
     q2b(19).


*** Queries for q3 ***

CHECKING answers to ?-q3(A).
     [[s, e, w, n]].
ALL ANSWERS CORRECT.



*** Queries for q4a ***

CHECKING answers to ?-q4a(A).
     [[p(4, 1), p(4, 2), p(4, 3), p(4, 4), p(3, 4), p(2, 4), p(1, 4), p(1, 3), p(2, 3), p(3, 3), p(3, 2), p(2, 2), p(1, 2), p(1, 1), p(2, 1), p(3, 1)]].
ALL ANSWERS CORRECT.



*** Queries for q4b ***

CHECKING answers to ?-q4b(A).
     [[p(4, 1), p(4, 2), p(4, 3), p(4, 4), p(3, 4), p(2, 4), p(1, 4), p(1, 3), p(2, 3), p(3, 3), p(3, 2), p(2, 2), p(2, 1), p(3, 1)]].
ALL ANSWERS CORRECT.



*** Queries for q4c ***

CHECKING answers to ?-q4c(A).
     [[p(4, 1), p(4, 2), p(4, 3), p(4, 4), p(3, 4), p(2, 4), p(1, 4), p(1, 3), p(2, 3), p(3, 3), p(3, 2), p(2, 2), p(1, 2), p(1, 1), p(2, 1), p(3, 1)]].
ALL ANSWERS CORRECT.



*** Queries for q4d ***

CHECKING answers to ?-q4d(A).
     [[p(4, 1), p(4, 2), p(4, 3), p(4, 4), p(3, 4), p(2, 4), p(1, 4), p(1, 3), p(2, 3), p(3, 3), p(3, 2), p(3, 1), p(2, 1), p(2, 2), p(1, 2), p(1, 1)]].
ALL ANSWERS CORRECT.


Q5a. CORRECT

Q5b. CORRECT

Q6. Does not output path.

```
% Facts about family members
% Basic facts (example family tree - you should replace with your own family members)
male(Gideon).
male(Shlomi).
male(Rafi).
male(Omer).
male(Dan).
female(Haya).
female(Shira).
female(Dana).
female(Neta).
female(Maya).
female(Sharon).


% Parent relationships
parent(Gideon, Dana).
parent(Gideon, Shira).
parent(Haya, Dana).
parent(Haya, Shira).
parent(Rafi, Omer).
parent(Rafi, Neta).
parent(Dana, Omer).
parent(Dana, Neta).
parent(Shlomi, Maya).
parent(Shlomi, Sharon).
parent(Shlomi, Dan).
parent(Shira, Maya).
parent(Shira, Sharon).
parent(Shira, Dan).

% Marriage relationships (male always first parameter)
married(Gideon, Haya).
married(Shlomi, Shira).
married(Rafi, Dana).

% Family relationship rules
% 1. Father
father(X, Y) :- male(X), parent(X, Y).

% 2. Mother
mother(X, Y) :- female(X), parent(X, Y).

% 3. Son
son(X, Y) :- male(X), parent(Y, X).

% 4. Daughter
daughter(X, Y) :- female(X), parent(Y, X).

% 5. Grandfather
grandfather(X, Y) :- male(X), parent(X, Z), parent(Z, Y).

% 6. Grandmother
grandmother(X, Y) :- female(X), parent(X, Z), parent(Z, Y).

% 7. Grandson
grandson(X, Y) :- male(X), parent(Z, X), parent(Y, Z).

% 8. Granddaughter
granddaughter(X, Y) :- female(X), parent(Z, X), parent(Y, Z).

% 9. Siblings
sibling(X, Y) :- parent(Z, X), parent(Z, Y).

% 10. Uncle by marriage (no blood relation)
uncle_by_marriage(X, Y) :- male(X), married(X, Z), sibling(Z, W), parent(W, Y).

% 11. Female cousin
female_cousin(X, Y) :- female(X), parent(P1, X), parent(P2, Y), sibling(P1, P2).

% 12. Brother-in-law
brother_in_law(X, Y) :- male(X), (married(X, Z), sibling(Z, Y) ; sibling(X, Z), married(Z, Y)).

% 13. Niece
niece(X, Y) :- female(X), parent(Z, X), sibling(Z, Y).

% 14. Second cousins
second_cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    parent(GP1, P1),
    parent(GP2, P2),
    sibling(GP1, GP2).

% List operations
% 1. Reverse
reverse([], []).
reverse([H|T], Z) :- reverse(T, RT), append(RT, [H], Z).

% 2. Member
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

% 3. Palindrome
palindrome(L) :- reverse(L, L).

% 4. Sorted
sorted([]).
sorted([_]).
sorted([X,Y|T]) :- X =< Y, sorted([Y|T]).

% Permutation
permutation([], []).
permutation([H|T], P) :- permutation(T, PT), insert(H, PT, P).

% Insert an element into every possible position in the list
insert(X, L, [X|L]).
insert(X, [H|T], [H|R]) :- insert(X, T, R).

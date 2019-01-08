# ANCC Automatically Generated Documentation
## Raw Grammar
```
1. program → declaration-list EOF
2. declaration-list → declaration-list declaration | declaration
3. declaration → var-declaration | fun-declaration
4. var-declaration → type-specifier ID ; | type-specifier ID [ NUM ] ;
5. type-specifier → int | void
6. fun-declaration → type-specifier ID ( params ) compound-stmt
7. params → param-list | void
8. param-list → param-list , param | param
9. param → type-specifier ID | type-specifier ID [ ]
10. compound-stmt → { declaration-list statement-list }
11. statement-list → statement-list statement | ε
12. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
13. expression-stmt → expression ; | continue ; | break ; | ;
14. selection-stmt → if ( expression ) statement else statement
15. iteration-stmt → while ( expression ) statement
16. return-stmt → return ; | return expression ;
17. switch-stmt → switch ( expression ) { case-stmts default-stmt }
18. case-stmts → case-stmts case-stmt | ε
19. case-stmt → case NUM : statement-list
20. default-stmt → default : statement-list | ε
21. expression → var = expression | simple-expression
22. var → ID | ID [ expression ]
23. simple-expression → additive-expression RELOP additive-expression | additive-expression
24. additive-expression → additive-expression addop term | term
25. addop → + | -
26. term → term * factor | factor
27. factor → ( expression ) | var | call | NUM
28. call → ID ( args )
29. args → arg-list | ε
30. arg-list → arg-list , expression | expression
```
## Recursion Free Grammar
```
1. program → declaration-list EOF
2. declaration-list → declaration declaration-list-prime
3. declaration-list-prime → declaration declaration-list-prime | ε
4. declaration → var-declaration | fun-declaration
5. var-declaration → type-specifier ID rest-of-var-declaration
6. rest-of-var-declaration → ; | [ NUM ] ;
7. type-specifier → int | void
8. fun-declaration → type-specifier ID ( params ) compound-stmt
9. params → param-list | void
10. param-list → param param-list-prime
11. param-list-prime → , param param-list-prime | ε
12. param → type-specifier ID rest-of-param
13. rest-of-param → ε | [ ]
14. compound-stmt → { declaration-list statement-list }
15. statement-list → statement-list-prime
16. statement-list-prime → statement statement-list-prime | ε
17. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
18. expression-stmt → expression ; | continue ; | break ; | ;
19. selection-stmt → if ( expression ) statement else statement
20. iteration-stmt → while ( expression ) statement
21. return-stmt → return rest-of-return-stmt
22. rest-of-return-stmt → ; | expression ;
23. switch-stmt → switch ( expression ) { case-stmts default-stmt }
24. case-stmts → case-stmts-prime
25. case-stmts-prime → case-stmt case-stmts-prime | ε
26. case-stmt → case NUM : statement-list
27. default-stmt → default : statement-list | ε
28. expression → var = expression | simple-expression
29. var → ID rest-of-var
30. rest-of-var → ε | [ expression ]
31. simple-expression → additive-expression rest-of-simple-expression
32. rest-of-simple-expression → RELOP additive-expression | ε
33. additive-expression → term additive-expression-prime
34. additive-expression-prime → addop term additive-expression-prime | ε
35. addop → + | -
36. term → factor term-prime
37. term-prime → * factor term-prime | ε
38. factor → ( expression ) | var | call | NUM
39. call → ID ( args )
40. args → arg-list | ε
41. arg-list → expression arg-list-prime
42. arg-list-prime → , expression arg-list-prime | ε
```
## Predictable Grammar
```
1. program → declaration-list EOF
2. declaration-list → declaration declaration-list-prime
3. declaration-list-prime → declaration declaration-list-prime | ε
4. declaration → var-declaration | fun-declaration
5. var-declaration → type-specifier ID rest-of-var-declaration
6. rest-of-var-declaration → ; | [ NUM ] ;
7. type-specifier → int | void
8. fun-declaration → type-specifier ID ( params ) compound-stmt
9. params → param-list | void
10. param-list → param param-list-prime
11. param-list-prime → , param param-list-prime | ε
12. param → type-specifier ID rest-of-param
13. rest-of-param → ε | [ ]
14. compound-stmt → { declaration-list statement-list }
15. statement-list → statement-list-prime
16. statement-list-prime → statement statement-list-prime | ε
17. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
18. expression-stmt → expression ; | continue ; | break ; | ;
19. selection-stmt → if ( expression ) statement else statement
20. iteration-stmt → while ( expression ) statement
21. return-stmt → return rest-of-return-stmt
22. rest-of-return-stmt → ; | expression ;
23. switch-stmt → switch ( expression ) { case-stmts default-stmt }
24. case-stmts → case-stmts-prime
25. case-stmts-prime → case-stmt case-stmts-prime | ε
26. case-stmt → case NUM : statement-list
27. default-stmt → default : statement-list | ε
28. expression → var = expression | simple-expression
29. var → ID rest-of-var
30. rest-of-var → ε | [ expression ]
31. simple-expression → additive-expression rest-of-simple-expression
32. rest-of-simple-expression → RELOP additive-expression | ε
33. additive-expression → term additive-expression-prime
34. additive-expression-prime → addop term additive-expression-prime | ε
35. addop → + | -
36. term → factor term-prime
37. term-prime → * factor term-prime | ε
38. factor → ( expression ) | var | call | NUM
39. call → ID ( args )
40. args → arg-list | ε
41. arg-list → expression arg-list-prime
42. arg-list-prime → , expression arg-list-prime | ε
```
## First and Follow
|Non-terminal|First|Follow|
|:----------:|:---:|:----:|
|simple-expression|( NUM ID|) ] ; ,|
|rest-of-param|ε [|) ,|
|args|( ε NUM ID|)|
|declaration|int void|EOF while NUM } return int switch void { ( continue break ID if ;|
|statement-list-prime|( while NUM return continue break ID ε switch if ; {|case default }|
|additive-expression|( NUM ID|) ] RELOP ; ,|
|rest-of-var|ε [|- ) ] + RELOP ; , * =|
|rest-of-return-stmt|( NUM ; ID|while NUM } return switch { ( continue case break ID default if ; else|
|statement|( while NUM return continue break ID switch if ; {|while NUM } return switch { ( continue case break ID default if ; else|
|arg-list|( NUM ID|)|
|expression-stmt|( NUM ; continue break ID|while NUM } return switch { ( continue case break ID default if ; else|
|selection-stmt|if|while NUM } return switch { ( continue case break ID default if ; else|
|declaration-list-prime|int ε void|( EOF while NUM } return continue break ID switch if ; {|
|case-stmts|ε case|default }|
|iteration-stmt|while|while NUM } return switch { ( continue case break ID default if ; else|
|params|int void|)|
|term|( NUM ID|- ) ] + RELOP ; ,|
|default-stmt|default ε|}|
|return-stmt|return|while NUM } return switch { ( continue case break ID default if ; else|
|var-declaration|int void|EOF while NUM } return int switch void { ( continue break ID if ;|
|case-stmts-prime|ε case|default }|
|switch-stmt|switch|while NUM } return switch { ( continue case break ID default if ; else|
|case-stmt|case|default } case|
|expression|( NUM ID|) ] ; ,|
|fun-declaration|int void|EOF while NUM } return int switch void { ( continue break ID if ;|
|type-specifier|int void|ID|
|addop|- +|( NUM ID|
|arg-list-prime|ε ,|)|
|compound-stmt|{|EOF while NUM } return int switch void { ( continue case break ID default if ; else|
|rest-of-var-declaration|; [|EOF while NUM } return int switch void { ( continue break ID if ;|
|param-list|int void|)|
|additive-expression-prime|ε - +|RELOP ) ] ; ,|
|rest-of-simple-expression|RELOP ε|) ] ; ,|
|param|int void|, )|
|param-list-prime|ε ,|)|
|factor|( NUM ID|- ) ] + RELOP ; , *|
|declaration-list|int void|( EOF while NUM } return continue break ID switch if ; {|
|statement-list|while NUM return switch { ( continue break ID ε if ;|case default }|
|var|ID|- ) ] + RELOP ; , * =|
|call|ID|- ) ] + RELOP ; , *|
|term-prime|ε *|- ) ] + RELOP ; ,|
|program|int void||

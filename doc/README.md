# ANCC Automatically Generated Documentation
## Raw Grammar
```
1. program → declaration-list EOF
2. declaration-list → declaration-list declaration | ε
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
2. declaration-list → declaration-list-prime
3. declaration-list-prime → declaration declaration-list-prime | ε
4. declaration → var-declaration | fun-declaration
5. var-declaration → type-specifier ID ; | type-specifier ID [ NUM ] ;
6. type-specifier → int | void
7. fun-declaration → type-specifier ID ( params ) compound-stmt
8. params → param-list | void
9. param-list → param param-list-prime
10. param-list-prime → , param param-list-prime | ε
11. param → type-specifier ID | type-specifier ID [ ]
12. compound-stmt → { declaration-list statement-list }
13. statement-list → statement-list-prime
14. statement-list-prime → statement statement-list-prime | ε
15. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
16. expression-stmt → expression ; | continue ; | break ; | ;
17. selection-stmt → if ( expression ) statement else statement
18. iteration-stmt → while ( expression ) statement
19. return-stmt → return ; | return expression ;
20. switch-stmt → switch ( expression ) { case-stmts default-stmt }
21. case-stmts → case-stmts-prime
22. case-stmts-prime → case-stmt case-stmts-prime | ε
23. case-stmt → case NUM : statement-list
24. default-stmt → default : statement-list | ε
25. expression → var = expression | simple-expression
26. var → ID | ID [ expression ]
27. simple-expression → additive-expression RELOP additive-expression | additive-expression
28. additive-expression → term additive-expression-prime
29. additive-expression-prime → addop term additive-expression-prime | ε
30. addop → + | -
31. term → factor term-prime
32. term-prime → * factor term-prime | ε
33. factor → ( expression ) | var | call | NUM
34. call → ID ( args )
35. args → arg-list | ε
36. arg-list → expression arg-list-prime
37. arg-list-prime → , expression arg-list-prime | ε
```
## Partially Factored Grammar
```
1. program → declaration-list EOF
2. declaration-list → declaration-list-prime
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
2. declaration-list → declaration-list-prime
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
|additive-expression|( NUM|) , ; RELOP ]|
|additive-expression-prime|+ - ε|) , ; RELOP ]|
|addop|+ -|( NUM|
|arg-list|( ID NUM|)|
|arg-list-prime|, ε|)|
|args|( ID NUM ε|)|
|bracket-id-additive-expression|bracket-var|) , ; RELOP ]|
|bracket-id-expression|( ID NUM bracket-var|) , ; ]|
|bracket-id-factor|bracket-var|) * + , - ; RELOP ]|
|bracket-id-simple-expression|bracket-var|) , ; ]|
|bracket-id-term|bracket-var|) + , - ; RELOP ]|
|bracket-reference|bracket-var|) * + , - ; RELOP ]|
|call|(|) * + , - ; RELOP ]|
|case-stmt|case|case default }|
|case-stmts|case ε|default }|
|case-stmts-prime|case ε|default }|
|compound-stmt|{|( ; EOF ID NUM break case continue default else if int return switch void while { }|
|declaration|( ; [|( ; EOF ID NUM break continue if int return switch void while { }|
|declaration-list|int void ε|( ; EOF ID NUM break continue if return switch while { }|
|declaration-list-prime|int void ε|( ; EOF ID NUM break continue if return switch while { }|
|default-stmt|default ε|}|
|expression|( ID NUM|) , ; ]|
|expression-stmt|( ; ID NUM break continue|( ; ID NUM break case continue default else if return switch while { }|
|factor|( NUM|) * + , - ; RELOP ]|
|fun-declaration|(|( ; EOF ID NUM break continue if int return switch void while { }|
|id-additive-expression|( * + - ε|) , ; RELOP ]|
|id-expression|( * + - = RELOP [ ε|) , ; ]|
|id-factor|( ε|) * + , - ; RELOP ]|
|id-simple-expression|( * + - RELOP ε|) , ; ]|
|id-term|( * ε|) + , - ; RELOP ]|
|int-starting-param-list|int|)|
|iteration-stmt|while|( ; ID NUM break case continue default else if return switch while { }|
|param|int void|) ,|
|param-list-prime|, ε|)|
|params|int void|)|
|program|EOF int void||
|reference|( ε|) * + , - ; RELOP ]|
|rest-of-param|[ ε|) ,|
|rest-of-return-stmt|( ; ID NUM|( ; ID NUM break case continue default else if return switch while { }|
|rest-of-simple-expression|RELOP ε|) , ; ]|
|rest-of-var|ε|) * + , - ; = RELOP ]|
|rest-of-var-declaration|; [|( ; EOF ID NUM break continue if int return switch void while { }|
|rest-of-void-starting-param-list|ID ε|)|
|return-stmt|return|( ; ID NUM break case continue default else if return switch while { }|
|selection-stmt|if|( ; ID NUM break case continue default else if return switch while { }|
|simple-expression|( NUM|) , ; ]|
|statement|( ; ID NUM break continue if return switch while {|( ; ID NUM break case continue default else if return switch while { }|
|statement-list|( ; ID NUM break continue if return switch while { ε|case default }|
|statement-list-prime|( ; ID NUM break continue if return switch while { ε|case default }|
|switch-stmt|switch|( ; ID NUM break case continue default else if return switch while { }|
|term|( NUM|) + , - ; RELOP ]|
|term-prime|* ε|) + , - ; RELOP ]|
|type-specifier|int void|ID|
|var|ε|) * + , - ; = RELOP ]|
|var-declaration|; [|( ; EOF ID NUM break continue if int return switch void while { }|
|void-starting-param-list|void|)|

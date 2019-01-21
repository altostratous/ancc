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
2. declaration-list → type-specifier ID declaration declaration-list | ε
3. declaration → var-declaration | fun-declaration
4. var-declaration → ; | [ NUM ] ;
6. type-specifier → int | void
7. fun-declaration → ( params ) compound-stmt
8. params → int-starting-param-list | void-starting-param-list
10. void-starting-param-list → void rest-of-void-starting-param-list
11. rest-of-void-starting-param-list → ID rest-of-param param-list-prime | ε
12. int-starting-param-list → int ID rest-of-param param-list-prime
13. param-list-prime → , param param-list-prime | ε
14. param → type-specifier ID rest-of-param
15. rest-of-param → ε | [ ]
16. compound-stmt → { declaration-list statement-list }
18. statement-list → statement statement-list | ε
19. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
20. expression-stmt → expression ; | continue ; | break ; | ;
21. selection-stmt → if ( expression ) statement else statement
22. iteration-stmt → while ( expression ) statement
23. return-stmt → return rest-of-return-stmt
24. rest-of-return-stmt → ; | expression ;
25. switch-stmt → switch ( expression ) { case-stmts default-stmt }
27. case-stmts → case-stmt case-stmts | ε
28. case-stmt → case NUM : statement-list
29. default-stmt → default : statement-list | ε
30. expression → simple-expression | ID id-expression
31. id-expression → = expression | id-simple-expression | [ expression ] bracket-id-expression
32. bracket-id-expression → = expression | ε
35. simple-expression → additive-expression rest-of-simple-expression
36. id-simple-expression → id-additive-expression rest-of-simple-expression
38. rest-of-simple-expression → RELOP addop-relop-rest | ε
39. addop-relop-rest → additive-expression | ID id-additive-expression
39. additive-expression → term additive-expression-prime
40. id-additive-expression → id-term additive-expression-prime
42. additive-expression-prime → addop addop-relop-rest | ε
43. addop → + | -
44. term → factor term-prime
45. id-term → reference term-prime
37. term-prime → * term | * ID id-term | ε
47. factor → ( expression ) | NUM
50. reference → call | ε
52. call → ( args )
53. args → arg-list | ε
54. arg-list → expression arg-list-prime
55. arg-list-prime → , expression arg-list-prime | ε
```
## State Diagram
```

program
1 (program) to -> [(declaration-list, 2 (program))]
2 (program) to -> [(EOF, 3 (program) (success))]
3 (program) (success)

declaration-list
4 (declaration-list) to -> [(type-specifier, 5 (declaration-list)), ((), 9 (declaration-list) (success))]
5 (declaration-list) to -> [(ID, 6 (declaration-list))]
9 (declaration-list) (success)
6 (declaration-list) to -> [(declaration, 7 (declaration-list))]
7 (declaration-list) to -> [(declaration-list, 8 (declaration-list) (success))]
8 (declaration-list) (success)

declaration
10 (declaration) to -> [(var-declaration, 11 (declaration) (success)), (fun-declaration, 12 (declaration) (success))]
11 (declaration) (success)
12 (declaration) (success)

var-declaration
13 (var-declaration) to -> [(;, 14 (var-declaration) (success)), ([, 15 (var-declaration))]
14 (var-declaration) (success)
15 (var-declaration) to -> [(NUM, 16 (var-declaration))]
16 (var-declaration) to -> [(], 17 (var-declaration))]
17 (var-declaration) to -> [(;, 18 (var-declaration) (success))]
18 (var-declaration) (success)

type-specifier
19 (type-specifier) to -> [(int, 20 (type-specifier) (success)), (void, 21 (type-specifier) (success))]
20 (type-specifier) (success)
21 (type-specifier) (success)

fun-declaration
22 (fun-declaration) to -> [((, 23 (fun-declaration))]
23 (fun-declaration) to -> [(params, 24 (fun-declaration))]
24 (fun-declaration) to -> [(), 25 (fun-declaration))]
25 (fun-declaration) to -> [(compound-stmt, 26 (fun-declaration) (success))]
26 (fun-declaration) (success)

params
27 (params) to -> [(int-starting-param-list, 28 (params) (success)), (void-starting-param-list, 29 (params) (success))]
28 (params) (success)
29 (params) (success)

void-starting-param-list
30 (void-starting-param-list) to -> [(void, 31 (void-starting-param-list))]
31 (void-starting-param-list) to -> [(rest-of-void-starting-param-list, 32 (void-starting-param-list) (success))]
32 (void-starting-param-list) (success)

rest-of-void-starting-param-list
33 (rest-of-void-starting-param-list) to -> [(ID, 34 (rest-of-void-starting-param-list)), ((), 37 (rest-of-void-starting-param-list) (success))]
34 (rest-of-void-starting-param-list) to -> [(rest-of-param, 35 (rest-of-void-starting-param-list))]
37 (rest-of-void-starting-param-list) (success)
35 (rest-of-void-starting-param-list) to -> [(param-list-prime, 36 (rest-of-void-starting-param-list) (success))]
36 (rest-of-void-starting-param-list) (success)

int-starting-param-list
38 (int-starting-param-list) to -> [(int, 39 (int-starting-param-list))]
39 (int-starting-param-list) to -> [(ID, 40 (int-starting-param-list))]
40 (int-starting-param-list) to -> [(rest-of-param, 41 (int-starting-param-list))]
41 (int-starting-param-list) to -> [(param-list-prime, 42 (int-starting-param-list) (success))]
42 (int-starting-param-list) (success)

param-list-prime
43 (param-list-prime) to -> [(,, 44 (param-list-prime)), ((), 47 (param-list-prime) (success))]
44 (param-list-prime) to -> [(param, 45 (param-list-prime))]
47 (param-list-prime) (success)
45 (param-list-prime) to -> [(param-list-prime, 46 (param-list-prime) (success))]
46 (param-list-prime) (success)

param
48 (param) to -> [(type-specifier, 49 (param))]
49 (param) to -> [(ID, 50 (param))]
50 (param) to -> [(rest-of-param, 51 (param) (success))]
51 (param) (success)

rest-of-param
52 (rest-of-param) to -> [((), 53 (rest-of-param) (success)), ([, 54 (rest-of-param))]
53 (rest-of-param) (success)
54 (rest-of-param) to -> [(], 55 (rest-of-param) (success))]
55 (rest-of-param) (success)

compound-stmt
56 (compound-stmt) to -> [({, 57 (compound-stmt))]
57 (compound-stmt) to -> [(declaration-list, 58 (compound-stmt))]
58 (compound-stmt) to -> [(statement-list, 59 (compound-stmt))]
59 (compound-stmt) to -> [(}, 60 (compound-stmt) (success))]
60 (compound-stmt) (success)

statement-list
61 (statement-list) to -> [(statement, 62 (statement-list)), ((), 64 (statement-list) (success))]
62 (statement-list) to -> [(statement-list, 63 (statement-list) (success))]
64 (statement-list) (success)
63 (statement-list) (success)

statement
65 (statement) to -> [(expression-stmt, 66 (statement) (success)), (compound-stmt, 67 (statement) (success)), (selection-stmt, 68 (statement) (success)), (iteration-stmt, 69 (statement) (success)), (return-stmt, 70 (statement) (success)), (switch-stmt, 71 (statement) (success))]
66 (statement) (success)
67 (statement) (success)
68 (statement) (success)
69 (statement) (success)
70 (statement) (success)
71 (statement) (success)

expression-stmt
72 (expression-stmt) to -> [(expression, 73 (expression-stmt)), (continue, 75 (expression-stmt)), (break, 77 (expression-stmt)), (;, 79 (expression-stmt) (success))]
73 (expression-stmt) to -> [(;, 74 (expression-stmt) (success))]
75 (expression-stmt) to -> [(;, 76 (expression-stmt) (success))]
77 (expression-stmt) to -> [(;, 78 (expression-stmt) (success))]
79 (expression-stmt) (success)
74 (expression-stmt) (success)
76 (expression-stmt) (success)
78 (expression-stmt) (success)

selection-stmt
80 (selection-stmt) to -> [(if, 81 (selection-stmt))]
81 (selection-stmt) to -> [((, 82 (selection-stmt))]
82 (selection-stmt) to -> [(expression, 83 (selection-stmt))]
83 (selection-stmt) to -> [(), 84 (selection-stmt))]
84 (selection-stmt) to -> [(statement, 85 (selection-stmt))]
85 (selection-stmt) to -> [(else, 86 (selection-stmt))]
86 (selection-stmt) to -> [(statement, 87 (selection-stmt) (success))]
87 (selection-stmt) (success)

iteration-stmt
88 (iteration-stmt) to -> [(while, 89 (iteration-stmt))]
89 (iteration-stmt) to -> [((, 90 (iteration-stmt))]
90 (iteration-stmt) to -> [(expression, 91 (iteration-stmt))]
91 (iteration-stmt) to -> [(), 92 (iteration-stmt))]
92 (iteration-stmt) to -> [(statement, 93 (iteration-stmt) (success))]
93 (iteration-stmt) (success)

return-stmt
94 (return-stmt) to -> [(return, 95 (return-stmt))]
95 (return-stmt) to -> [(rest-of-return-stmt, 96 (return-stmt) (success))]
96 (return-stmt) (success)

rest-of-return-stmt
97 (rest-of-return-stmt) to -> [(;, 98 (rest-of-return-stmt) (success)), (expression, 99 (rest-of-return-stmt))]
98 (rest-of-return-stmt) (success)
99 (rest-of-return-stmt) to -> [(;, 100 (rest-of-return-stmt) (success))]
100 (rest-of-return-stmt) (success)

switch-stmt
101 (switch-stmt) to -> [(switch, 102 (switch-stmt))]
102 (switch-stmt) to -> [((, 103 (switch-stmt))]
103 (switch-stmt) to -> [(expression, 104 (switch-stmt))]
104 (switch-stmt) to -> [(), 105 (switch-stmt))]
105 (switch-stmt) to -> [({, 106 (switch-stmt))]
106 (switch-stmt) to -> [(case-stmts, 107 (switch-stmt))]
107 (switch-stmt) to -> [(default-stmt, 108 (switch-stmt))]
108 (switch-stmt) to -> [(}, 109 (switch-stmt) (success))]
109 (switch-stmt) (success)

case-stmts
110 (case-stmts) to -> [(case-stmt, 111 (case-stmts)), ((), 113 (case-stmts) (success))]
111 (case-stmts) to -> [(case-stmts, 112 (case-stmts) (success))]
113 (case-stmts) (success)
112 (case-stmts) (success)

case-stmt
114 (case-stmt) to -> [(case, 115 (case-stmt))]
115 (case-stmt) to -> [(NUM, 116 (case-stmt))]
116 (case-stmt) to -> [(:, 117 (case-stmt))]
117 (case-stmt) to -> [(statement-list, 118 (case-stmt) (success))]
118 (case-stmt) (success)

default-stmt
119 (default-stmt) to -> [(default, 120 (default-stmt)), ((), 123 (default-stmt) (success))]
120 (default-stmt) to -> [(:, 121 (default-stmt))]
123 (default-stmt) (success)
121 (default-stmt) to -> [(statement-list, 122 (default-stmt) (success))]
122 (default-stmt) (success)

expression
124 (expression) to -> [(simple-expression, 125 (expression) (success)), (ID, 126 (expression))]
125 (expression) (success)
126 (expression) to -> [(id-expression, 127 (expression) (success))]
127 (expression) (success)

id-expression
128 (id-expression) to -> [(=, 129 (id-expression)), (id-simple-expression, 131 (id-expression) (success)), ([, 132 (id-expression))]
129 (id-expression) to -> [(expression, 130 (id-expression) (success))]
131 (id-expression) (success)
132 (id-expression) to -> [(expression, 133 (id-expression))]
130 (id-expression) (success)
133 (id-expression) to -> [(], 134 (id-expression))]
134 (id-expression) to -> [(bracket-id-expression, 135 (id-expression) (success))]
135 (id-expression) (success)

bracket-id-expression
136 (bracket-id-expression) to -> [(=, 137 (bracket-id-expression)), ((), 139 (bracket-id-expression) (success))]
137 (bracket-id-expression) to -> [(expression, 138 (bracket-id-expression) (success))]
139 (bracket-id-expression) (success)
138 (bracket-id-expression) (success)

simple-expression
140 (simple-expression) to -> [(additive-expression, 141 (simple-expression))]
141 (simple-expression) to -> [(rest-of-simple-expression, 142 (simple-expression) (success))]
142 (simple-expression) (success)

id-simple-expression
143 (id-simple-expression) to -> [(id-additive-expression, 144 (id-simple-expression))]
144 (id-simple-expression) to -> [(rest-of-simple-expression, 145 (id-simple-expression) (success))]
145 (id-simple-expression) (success)

rest-of-simple-expression
146 (rest-of-simple-expression) to -> [(RELOP, 147 (rest-of-simple-expression)), ((), 149 (rest-of-simple-expression) (success))]
147 (rest-of-simple-expression) to -> [(addop-relop-rest, 148 (rest-of-simple-expression) (success))]
149 (rest-of-simple-expression) (success)
148 (rest-of-simple-expression) (success)

addop-relop-rest
150 (addop-relop-rest) to -> [(additive-expression, 151 (addop-relop-rest) (success)), (ID, 152 (addop-relop-rest))]
151 (addop-relop-rest) (success)
152 (addop-relop-rest) to -> [(id-additive-expression, 153 (addop-relop-rest) (success))]
153 (addop-relop-rest) (success)

additive-expression
154 (additive-expression) to -> [(term, 155 (additive-expression))]
155 (additive-expression) to -> [(additive-expression-prime, 156 (additive-expression) (success))]
156 (additive-expression) (success)

id-additive-expression
157 (id-additive-expression) to -> [(id-term, 158 (id-additive-expression))]
158 (id-additive-expression) to -> [(additive-expression-prime, 159 (id-additive-expression) (success))]
159 (id-additive-expression) (success)

additive-expression-prime
160 (additive-expression-prime) to -> [(addop, 161 (additive-expression-prime)), ((), 163 (additive-expression-prime) (success))]
161 (additive-expression-prime) to -> [(addop-relop-rest, 162 (additive-expression-prime) (success))]
163 (additive-expression-prime) (success)
162 (additive-expression-prime) (success)

addop
164 (addop) to -> [(+, 165 (addop) (success)), (-, 166 (addop) (success))]
165 (addop) (success)
166 (addop) (success)

term
167 (term) to -> [(factor, 168 (term))]
168 (term) to -> [(term-prime, 169 (term) (success))]
169 (term) (success)

id-term
170 (id-term) to -> [(reference, 171 (id-term))]
171 (id-term) to -> [(term-prime, 172 (id-term) (success))]
172 (id-term) (success)

term-prime
173 (term-prime) to -> [(*, 174 (term-prime)), (*, 176 (term-prime)), ((), 179 (term-prime) (success))]
174 (term-prime) to -> [(term, 175 (term-prime) (success))]
176 (term-prime) to -> [(ID, 177 (term-prime))]
179 (term-prime) (success)
175 (term-prime) (success)
177 (term-prime) to -> [(id-term, 178 (term-prime) (success))]
178 (term-prime) (success)

factor
180 (factor) to -> [((, 181 (factor)), (NUM, 184 (factor) (success))]
181 (factor) to -> [(expression, 182 (factor))]
184 (factor) (success)
182 (factor) to -> [(), 183 (factor) (success))]
183 (factor) (success)

reference
185 (reference) to -> [(call, 186 (reference) (success)), ((), 187 (reference) (success))]
186 (reference) (success)
187 (reference) (success)

call
188 (call) to -> [((, 189 (call))]
189 (call) to -> [(args, 190 (call))]
190 (call) to -> [(), 191 (call) (success))]
191 (call) (success)

args
192 (args) to -> [(arg-list, 193 (args) (success)), ((), 194 (args) (success))]
193 (args) (success)
194 (args) (success)

arg-list
195 (arg-list) to -> [(expression, 196 (arg-list))]
196 (arg-list) to -> [(arg-list-prime, 197 (arg-list) (success))]
197 (arg-list) (success)

arg-list-prime
198 (arg-list-prime) to -> [(,, 199 (arg-list-prime)), ((), 202 (arg-list-prime) (success))]
199 (arg-list-prime) to -> [(expression, 200 (arg-list-prime))]
202 (arg-list-prime) (success)
200 (arg-list-prime) to -> [(arg-list-prime, 201 (arg-list-prime) (success))]
201 (arg-list-prime) (success)
```
## First and Follow
|Non-terminal|First|Follow|
|:----------:|:---:|:----:|
|additive-expression|( NUM|) , ; RELOP ]|
|additive-expression-prime|+ - ε|) , ; RELOP ]|
|addop|+ -|( ID NUM|
|addop-relop-rest|( ID NUM|) , ; RELOP ]|
|arg-list|( ID NUM|)|
|arg-list-prime|, ε|)|
|args|( ID NUM ε|)|
|bracket-id-expression|= ε|) , ; ]|
|call|(|) * + , - ; RELOP ]|
|case-stmt|case|case default }|
|case-stmts|case ε|default }|
|compound-stmt|{|( ; EOF ID NUM break case continue default else if int return switch void while { }|
|declaration|( ; [|( ; EOF ID NUM break continue if int return switch void while { }|
|declaration-list|int void ε|( ; EOF ID NUM break continue if return switch while { }|
|default-stmt|default ε|}|
|expression|( ID NUM|) , ; ]|
|expression-stmt|( ; ID NUM break continue|( ; ID NUM break case continue default else if return switch while { }|
|factor|( NUM|) * + , - ; RELOP ]|
|fun-declaration|(|( ; EOF ID NUM break continue if int return switch void while { }|
|id-additive-expression|( * + - ε|) , ; RELOP ]|
|id-expression|( * + - = RELOP [ ε|) , ; ]|
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
|rest-of-void-starting-param-list|ID ε|)|
|return-stmt|return|( ; ID NUM break case continue default else if return switch while { }|
|selection-stmt|if|( ; ID NUM break case continue default else if return switch while { }|
|simple-expression|( NUM|) , ; ]|
|statement|( ; ID NUM break continue if return switch while {|( ; ID NUM break case continue default else if return switch while { }|
|statement-list|( ; ID NUM break continue if return switch while { ε|case default }|
|switch-stmt|switch|( ; ID NUM break case continue default else if return switch while { }|
|term|( NUM|) + , - ; RELOP ]|
|term-prime|* ε|) + , - ; RELOP ]|
|type-specifier|int void|ID|
|var-declaration|; [|( ; EOF ID NUM break continue if int return switch void while { }|
|void-starting-param-list|void|)|

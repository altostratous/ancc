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
3. declaration-list-prime → type-specifier ID declaration declaration-list-prime | ε
4. declaration → var-declaration | fun-declaration
5. var-declaration → rest-of-var-declaration
6. rest-of-var-declaration → ; | [ NUM ] ;
7. type-specifier → int | void
8. fun-declaration → ( params ) compound-stmt
9. params → int-starting-param-list | void-starting-param-list
10. void-starting-param-list → void rest-of-void-starting-param-list
11. rest-of-void-starting-param-list → ID rest-of-param param-list-prime | ε
12. int-starting-param-list → int ID rest-of-param param-list-prime
13. param-list-prime → , param param-list-prime | ε
14. param → type-specifier ID rest-of-param
15. rest-of-param → ε | [ ]
16. compound-stmt → { declaration-list statement-list }
17. statement-list → statement-list-prime
18. statement-list-prime → statement statement-list-prime | ε
19. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
20. expression-stmt → expression ; | continue ; | break ; | ;
21. selection-stmt → if ( expression ) statement else statement
22. iteration-stmt → while ( expression ) statement
23. return-stmt → return rest-of-return-stmt
24. rest-of-return-stmt → ; | expression ;
25. switch-stmt → switch ( expression ) { case-stmts default-stmt }
26. case-stmts → case-stmts-prime
27. case-stmts-prime → case-stmt case-stmts-prime | ε
28. case-stmt → case NUM : statement-list
29. default-stmt → default : statement-list | ε
30. expression → simple-expression | ID id-expression
31. id-expression → var = expression | id-simple-expression | [ bracket-id-expression
32. bracket-id-expression → expression ] = expression | bracket-id-simple-expression
33. var → rest-of-var
34. rest-of-var → ε
35. simple-expression → additive-expression rest-of-simple-expression
36. id-simple-expression → id-additive-expression rest-of-simple-expression
37. bracket-id-simple-expression → bracket-id-additive-expression rest-of-simple-expression
38. rest-of-simple-expression → RELOP additive-expression | ε
39. additive-expression → term additive-expression-prime
40. id-additive-expression → id-term additive-expression-prime
41. bracket-id-additive-expression → bracket-id-term additive-expression-prime
42. additive-expression-prime → addop term additive-expression-prime | ε
43. addop → + | -
44. term → factor term-prime
45. id-term → id-factor term-prime
46. bracket-id-term → bracket-id-factor term-prime
37. term-prime → * factor term-prime | ε
47. factor → ( expression ) | NUM
48. id-factor → reference
49. bracket-id-factor → bracket-reference
50. reference → var | call
51. bracket-reference → bracket-var
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
4 (declaration-list) to -> [(declaration-list-prime, 5 (declaration-list) (success))]
5 (declaration-list) (success)

declaration-list-prime
6 (declaration-list-prime) to -> [(type-specifier, 7 (declaration-list-prime)), ((), 10 (declaration-list-prime) (success))]
7 (declaration-list-prime) to -> [(ID, 8 (declaration-list-prime))]
10 (declaration-list-prime) (success)
8 (declaration-list-prime) to -> [(declaration, 9 (declaration-list-prime))]
9 (declaration-list-prime) to -> [(declaration-list-prime, 10 (declaration-list-prime) (success))]

declaration
11 (declaration) to -> [(var-declaration, 12 (declaration) (success)), (fun-declaration, 13 (declaration) (success))]
12 (declaration) (success)
13 (declaration) (success)

var-declaration
14 (var-declaration) to -> [(rest-of-var-declaration, 15 (var-declaration) (success))]
15 (var-declaration) (success)

rest-of-var-declaration
16 (rest-of-var-declaration) to -> [(;, 17 (rest-of-var-declaration) (success)), ([, 18 (rest-of-var-declaration))]
17 (rest-of-var-declaration) (success)
18 (rest-of-var-declaration) to -> [(NUM, 19 (rest-of-var-declaration))]
19 (rest-of-var-declaration) to -> [(], 20 (rest-of-var-declaration))]
20 (rest-of-var-declaration) to -> [(;, 21 (rest-of-var-declaration) (success))]
21 (rest-of-var-declaration) (success)

type-specifier
22 (type-specifier) to -> [(int, 23 (type-specifier) (success)), (void, 24 (type-specifier) (success))]
23 (type-specifier) (success)
24 (type-specifier) (success)

fun-declaration
25 (fun-declaration) to -> [((, 26 (fun-declaration))]
26 (fun-declaration) to -> [(params, 27 (fun-declaration))]
27 (fun-declaration) to -> [(), 28 (fun-declaration))]
28 (fun-declaration) to -> [(compound-stmt, 29 (fun-declaration) (success))]
29 (fun-declaration) (success)

params
30 (params) to -> [(int-starting-param-list, 31 (params) (success)), (void-starting-param-list, 32 (params) (success))]
31 (params) (success)
32 (params) (success)

void-starting-param-list
33 (void-starting-param-list) to -> [(void, 34 (void-starting-param-list))]
34 (void-starting-param-list) to -> [(rest-of-void-starting-param-list, 35 (void-starting-param-list) (success))]
35 (void-starting-param-list) (success)

rest-of-void-starting-param-list
36 (rest-of-void-starting-param-list) to -> [(ID, 37 (rest-of-void-starting-param-list)), ((), 39 (rest-of-void-starting-param-list) (success))]
37 (rest-of-void-starting-param-list) to -> [(rest-of-param, 38 (rest-of-void-starting-param-list))]
39 (rest-of-void-starting-param-list) (success)
38 (rest-of-void-starting-param-list) to -> [(param-list-prime, 39 (rest-of-void-starting-param-list) (success))]

int-starting-param-list
40 (int-starting-param-list) to -> [(int, 41 (int-starting-param-list))]
41 (int-starting-param-list) to -> [(ID, 42 (int-starting-param-list))]
42 (int-starting-param-list) to -> [(rest-of-param, 43 (int-starting-param-list))]
43 (int-starting-param-list) to -> [(param-list-prime, 44 (int-starting-param-list) (success))]
44 (int-starting-param-list) (success)

param-list-prime
45 (param-list-prime) to -> [(,, 46 (param-list-prime)), ((), 48 (param-list-prime) (success))]
46 (param-list-prime) to -> [(param, 47 (param-list-prime))]
48 (param-list-prime) (success)
47 (param-list-prime) to -> [(param-list-prime, 48 (param-list-prime) (success))]

param
49 (param) to -> [(type-specifier, 50 (param))]
50 (param) to -> [(ID, 51 (param))]
51 (param) to -> [(rest-of-param, 52 (param) (success))]
52 (param) (success)

rest-of-param
53 (rest-of-param) to -> [((), 52 (param) (success)), ([, 54 (rest-of-param))]
52 (param) (success)
54 (rest-of-param) to -> [(], 55 (rest-of-param) (success))]
55 (rest-of-param) (success)

compound-stmt
56 (compound-stmt) to -> [({, 57 (compound-stmt))]
57 (compound-stmt) to -> [(declaration-list, 58 (compound-stmt))]
58 (compound-stmt) to -> [(statement-list, 59 (compound-stmt))]
59 (compound-stmt) to -> [(}, 60 (compound-stmt) (success))]
60 (compound-stmt) (success)

statement-list
61 (statement-list) to -> [(statement-list-prime, 62 (statement-list) (success))]
62 (statement-list) (success)

statement-list-prime
63 (statement-list-prime) to -> [(statement, 64 (statement-list-prime)), ((), 65 (statement-list-prime) (success))]
64 (statement-list-prime) to -> [(statement-list-prime, 65 (statement-list-prime) (success))]
65 (statement-list-prime) (success)

statement
66 (statement) to -> [(expression-stmt, 67 (statement) (success)), (compound-stmt, 68 (statement) (success)), (selection-stmt, 69 (statement) (success)), (iteration-stmt, 70 (statement) (success)), (return-stmt, 71 (statement) (success)), (switch-stmt, 72 (statement) (success))]
67 (statement) (success)
68 (statement) (success)
69 (statement) (success)
70 (statement) (success)
71 (statement) (success)
72 (statement) (success)

expression-stmt
73 (expression-stmt) to -> [(expression, 74 (expression-stmt)), (continue, 76 (expression-stmt)), (break, 78 (expression-stmt)), (;, 80 (expression-stmt) (success))]
74 (expression-stmt) to -> [(;, 75 (expression-stmt) (success))]
76 (expression-stmt) to -> [(;, 77 (expression-stmt) (success))]
78 (expression-stmt) to -> [(;, 79 (expression-stmt) (success))]
80 (expression-stmt) (success)
75 (expression-stmt) (success)
77 (expression-stmt) (success)
79 (expression-stmt) (success)

selection-stmt
81 (selection-stmt) to -> [(if, 82 (selection-stmt))]
82 (selection-stmt) to -> [((, 83 (selection-stmt))]
83 (selection-stmt) to -> [(expression, 84 (selection-stmt))]
84 (selection-stmt) to -> [(), 85 (selection-stmt))]
85 (selection-stmt) to -> [(statement, 86 (selection-stmt))]
86 (selection-stmt) to -> [(else, 87 (selection-stmt))]
87 (selection-stmt) to -> [(statement, 88 (selection-stmt) (success))]
88 (selection-stmt) (success)

iteration-stmt
89 (iteration-stmt) to -> [(while, 90 (iteration-stmt))]
90 (iteration-stmt) to -> [((, 91 (iteration-stmt))]
91 (iteration-stmt) to -> [(expression, 92 (iteration-stmt))]
92 (iteration-stmt) to -> [(), 93 (iteration-stmt))]
93 (iteration-stmt) to -> [(statement, 94 (iteration-stmt) (success))]
94 (iteration-stmt) (success)

return-stmt
95 (return-stmt) to -> [(return, 96 (return-stmt))]
96 (return-stmt) to -> [(rest-of-return-stmt, 97 (return-stmt) (success))]
97 (return-stmt) (success)

rest-of-return-stmt
98 (rest-of-return-stmt) to -> [(;, 99 (rest-of-return-stmt) (success)), (expression, 100 (rest-of-return-stmt))]
99 (rest-of-return-stmt) (success)
100 (rest-of-return-stmt) to -> [(;, 101 (rest-of-return-stmt) (success))]
101 (rest-of-return-stmt) (success)

switch-stmt
102 (switch-stmt) to -> [(switch, 103 (switch-stmt))]
103 (switch-stmt) to -> [((, 104 (switch-stmt))]
104 (switch-stmt) to -> [(expression, 105 (switch-stmt))]
105 (switch-stmt) to -> [(), 106 (switch-stmt))]
106 (switch-stmt) to -> [({, 107 (switch-stmt))]
107 (switch-stmt) to -> [(case-stmts, 108 (switch-stmt))]
108 (switch-stmt) to -> [(default-stmt, 109 (switch-stmt))]
109 (switch-stmt) to -> [(}, 110 (switch-stmt) (success))]
110 (switch-stmt) (success)

case-stmts
111 (case-stmts) to -> [(case-stmts-prime, 112 (case-stmts) (success))]
112 (case-stmts) (success)

case-stmts-prime
113 (case-stmts-prime) to -> [(case-stmt, 114 (case-stmts-prime)), ((), 115 (case-stmts-prime) (success))]
114 (case-stmts-prime) to -> [(case-stmts-prime, 115 (case-stmts-prime) (success))]
115 (case-stmts-prime) (success)

case-stmt
116 (case-stmt) to -> [(case, 117 (case-stmt))]
117 (case-stmt) to -> [(NUM, 118 (case-stmt))]
118 (case-stmt) to -> [(:, 119 (case-stmt))]
119 (case-stmt) to -> [(statement-list, 120 (case-stmt) (success))]
120 (case-stmt) (success)

default-stmt
121 (default-stmt) to -> [(default, 122 (default-stmt)), ((), 124 (default-stmt) (success))]
122 (default-stmt) to -> [(:, 123 (default-stmt))]
124 (default-stmt) (success)
123 (default-stmt) to -> [(statement-list, 124 (default-stmt) (success))]

expression
125 (expression) to -> [(simple-expression, 126 (expression) (success)), (ID, 127 (expression))]
126 (expression) (success)
127 (expression) to -> [(id-expression, 128 (expression) (success))]
128 (expression) (success)

id-expression
129 (id-expression) to -> [(var, 130 (id-expression)), (id-simple-expression, 133 (id-expression) (success)), ([, 134 (id-expression))]
130 (id-expression) to -> [(=, 131 (id-expression))]
133 (id-expression) (success)
134 (id-expression) to -> [(bracket-id-expression, 135 (id-expression) (success))]
131 (id-expression) to -> [(expression, 132 (id-expression) (success))]
135 (id-expression) (success)
132 (id-expression) (success)

bracket-id-expression
136 (bracket-id-expression) to -> [(expression, 137 (bracket-id-expression)), (bracket-id-simple-expression, 141 (bracket-id-expression) (success))]
137 (bracket-id-expression) to -> [(], 138 (bracket-id-expression))]
141 (bracket-id-expression) (success)
138 (bracket-id-expression) to -> [(=, 139 (bracket-id-expression))]
139 (bracket-id-expression) to -> [(expression, 140 (bracket-id-expression) (success))]
140 (bracket-id-expression) (success)

var
142 (var) to -> [(rest-of-var, 143 (var) (success))]
143 (var) (success)

rest-of-var
144 (rest-of-var) to -> [((), 143 (var) (success))]
143 (var) (success)

simple-expression
145 (simple-expression) to -> [(additive-expression, 146 (simple-expression))]
146 (simple-expression) to -> [(rest-of-simple-expression, 147 (simple-expression) (success))]
147 (simple-expression) (success)

id-simple-expression
148 (id-simple-expression) to -> [(id-additive-expression, 149 (id-simple-expression))]
149 (id-simple-expression) to -> [(rest-of-simple-expression, 150 (id-simple-expression) (success))]
150 (id-simple-expression) (success)

bracket-id-simple-expression
151 (bracket-id-simple-expression) to -> [(bracket-id-additive-expression, 152 (bracket-id-simple-expression))]
152 (bracket-id-simple-expression) to -> [(rest-of-simple-expression, 153 (bracket-id-simple-expression) (success))]
153 (bracket-id-simple-expression) (success)

rest-of-simple-expression
154 (rest-of-simple-expression) to -> [(RELOP, 155 (rest-of-simple-expression)), ((), 156 (rest-of-simple-expression) (success))]
155 (rest-of-simple-expression) to -> [(additive-expression, 156 (rest-of-simple-expression) (success))]
156 (rest-of-simple-expression) (success)

additive-expression
157 (additive-expression) to -> [(term, 158 (additive-expression))]
158 (additive-expression) to -> [(additive-expression-prime, 159 (additive-expression) (success))]
159 (additive-expression) (success)

id-additive-expression
160 (id-additive-expression) to -> [(id-term, 161 (id-additive-expression))]
161 (id-additive-expression) to -> [(additive-expression-prime, 162 (id-additive-expression) (success))]
162 (id-additive-expression) (success)

bracket-id-additive-expression
163 (bracket-id-additive-expression) to -> [(bracket-id-term, 164 (bracket-id-additive-expression))]
164 (bracket-id-additive-expression) to -> [(additive-expression-prime, 165 (bracket-id-additive-expression) (success))]
165 (bracket-id-additive-expression) (success)

additive-expression-prime
166 (additive-expression-prime) to -> [(addop, 167 (additive-expression-prime)), ((), 169 (additive-expression-prime) (success))]
167 (additive-expression-prime) to -> [(term, 168 (additive-expression-prime))]
169 (additive-expression-prime) (success)
168 (additive-expression-prime) to -> [(additive-expression-prime, 169 (additive-expression-prime) (success))]

addop
170 (addop) to -> [(+, 171 (addop) (success)), (-, 172 (addop) (success))]
171 (addop) (success)
172 (addop) (success)

term
173 (term) to -> [(factor, 174 (term))]
174 (term) to -> [(term-prime, 175 (term) (success))]
175 (term) (success)

id-term
176 (id-term) to -> [(id-factor, 177 (id-term))]
177 (id-term) to -> [(term-prime, 178 (id-term) (success))]
178 (id-term) (success)

bracket-id-term
179 (bracket-id-term) to -> [(bracket-id-factor, 180 (bracket-id-term))]
180 (bracket-id-term) to -> [(term-prime, 181 (bracket-id-term) (success))]
181 (bracket-id-term) (success)

term-prime
182 (term-prime) to -> [(*, 183 (term-prime)), ((), 185 (term-prime) (success))]
183 (term-prime) to -> [(factor, 184 (term-prime))]
185 (term-prime) (success)
184 (term-prime) to -> [(term-prime, 185 (term-prime) (success))]

factor
186 (factor) to -> [((, 187 (factor)), (NUM, 190 (factor) (success))]
187 (factor) to -> [(expression, 188 (factor))]
190 (factor) (success)
188 (factor) to -> [(), 189 (factor) (success))]
189 (factor) (success)

id-factor
191 (id-factor) to -> [(reference, 192 (id-factor) (success))]
192 (id-factor) (success)

bracket-id-factor
193 (bracket-id-factor) to -> [(bracket-reference, 194 (bracket-id-factor) (success))]
194 (bracket-id-factor) (success)

reference
195 (reference) to -> [(var, 196 (reference) (success)), (call, 197 (reference) (success))]
196 (reference) (success)
197 (reference) (success)

bracket-reference
198 (bracket-reference) to -> [(bracket-var, 199 (bracket-reference) (success))]
199 (bracket-reference) (success)

call
200 (call) to -> [((, 201 (call))]
201 (call) to -> [(args, 202 (call))]
202 (call) to -> [(), 203 (call) (success))]
203 (call) (success)

args
204 (args) to -> [(arg-list, 205 (args) (success)), ((), 205 (args) (success))]
205 (args) (success)

arg-list
206 (arg-list) to -> [(expression, 207 (arg-list))]
207 (arg-list) to -> [(arg-list-prime, 208 (arg-list) (success))]
208 (arg-list) (success)

arg-list-prime
209 (arg-list-prime) to -> [(,, 210 (arg-list-prime)), ((), 212 (arg-list-prime) (success))]
210 (arg-list-prime) to -> [(expression, 211 (arg-list-prime))]
212 (arg-list-prime) (success)
211 (arg-list-prime) to -> [(arg-list-prime, 212 (arg-list-prime) (success))]
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

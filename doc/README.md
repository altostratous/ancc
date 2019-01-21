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
4. var-declaration → rest-of-var-declaration
5. rest-of-var-declaration → ; | [ NUM ] ;
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
38. rest-of-simple-expression → RELOP additive-expression | ε
39. additive-expression → term additive-expression-prime
40. id-additive-expression → id-term additive-expression-prime
42. additive-expression-prime → addop term additive-expression-prime | ε
43. addop → + | -
44. term → factor term-prime
45. id-term → reference term-prime
37. term-prime → * factor term-prime | ε
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
13 (var-declaration) to -> [(rest-of-var-declaration, 14 (var-declaration) (success))]
14 (var-declaration) (success)

rest-of-var-declaration
15 (rest-of-var-declaration) to -> [(;, 16 (rest-of-var-declaration) (success)), ([, 17 (rest-of-var-declaration))]
16 (rest-of-var-declaration) (success)
17 (rest-of-var-declaration) to -> [(NUM, 18 (rest-of-var-declaration))]
18 (rest-of-var-declaration) to -> [(], 19 (rest-of-var-declaration))]
19 (rest-of-var-declaration) to -> [(;, 20 (rest-of-var-declaration) (success))]
20 (rest-of-var-declaration) (success)

type-specifier
21 (type-specifier) to -> [(int, 22 (type-specifier) (success)), (void, 23 (type-specifier) (success))]
22 (type-specifier) (success)
23 (type-specifier) (success)

fun-declaration
24 (fun-declaration) to -> [((, 25 (fun-declaration))]
25 (fun-declaration) to -> [(params, 26 (fun-declaration))]
26 (fun-declaration) to -> [(), 27 (fun-declaration))]
27 (fun-declaration) to -> [(compound-stmt, 28 (fun-declaration) (success))]
28 (fun-declaration) (success)

params
29 (params) to -> [(int-starting-param-list, 30 (params) (success)), (void-starting-param-list, 31 (params) (success))]
30 (params) (success)
31 (params) (success)

void-starting-param-list
32 (void-starting-param-list) to -> [(void, 33 (void-starting-param-list))]
33 (void-starting-param-list) to -> [(rest-of-void-starting-param-list, 34 (void-starting-param-list) (success))]
34 (void-starting-param-list) (success)

rest-of-void-starting-param-list
35 (rest-of-void-starting-param-list) to -> [(ID, 36 (rest-of-void-starting-param-list)), ((), 39 (rest-of-void-starting-param-list) (success))]
36 (rest-of-void-starting-param-list) to -> [(rest-of-param, 37 (rest-of-void-starting-param-list))]
39 (rest-of-void-starting-param-list) (success)
37 (rest-of-void-starting-param-list) to -> [(param-list-prime, 38 (rest-of-void-starting-param-list) (success))]
38 (rest-of-void-starting-param-list) (success)

int-starting-param-list
40 (int-starting-param-list) to -> [(int, 41 (int-starting-param-list))]
41 (int-starting-param-list) to -> [(ID, 42 (int-starting-param-list))]
42 (int-starting-param-list) to -> [(rest-of-param, 43 (int-starting-param-list))]
43 (int-starting-param-list) to -> [(param-list-prime, 44 (int-starting-param-list) (success))]
44 (int-starting-param-list) (success)

param-list-prime
45 (param-list-prime) to -> [(,, 46 (param-list-prime)), ((), 49 (param-list-prime) (success))]
46 (param-list-prime) to -> [(param, 47 (param-list-prime))]
49 (param-list-prime) (success)
47 (param-list-prime) to -> [(param-list-prime, 48 (param-list-prime) (success))]
48 (param-list-prime) (success)

param
50 (param) to -> [(type-specifier, 51 (param))]
51 (param) to -> [(ID, 52 (param))]
52 (param) to -> [(rest-of-param, 53 (param) (success))]
53 (param) (success)

rest-of-param
54 (rest-of-param) to -> [((), 55 (rest-of-param) (success)), ([, 56 (rest-of-param))]
55 (rest-of-param) (success)
56 (rest-of-param) to -> [(], 57 (rest-of-param) (success))]
57 (rest-of-param) (success)

compound-stmt
58 (compound-stmt) to -> [({, 59 (compound-stmt))]
59 (compound-stmt) to -> [(declaration-list, 60 (compound-stmt))]
60 (compound-stmt) to -> [(statement-list, 61 (compound-stmt))]
61 (compound-stmt) to -> [(}, 62 (compound-stmt) (success))]
62 (compound-stmt) (success)

statement-list
63 (statement-list) to -> [(statement, 64 (statement-list)), ((), 66 (statement-list) (success))]
64 (statement-list) to -> [(statement-list, 65 (statement-list) (success))]
66 (statement-list) (success)
65 (statement-list) (success)

statement
67 (statement) to -> [(expression-stmt, 68 (statement) (success)), (compound-stmt, 69 (statement) (success)), (selection-stmt, 70 (statement) (success)), (iteration-stmt, 71 (statement) (success)), (return-stmt, 72 (statement) (success)), (switch-stmt, 73 (statement) (success))]
68 (statement) (success)
69 (statement) (success)
70 (statement) (success)
71 (statement) (success)
72 (statement) (success)
73 (statement) (success)

expression-stmt
74 (expression-stmt) to -> [(expression, 75 (expression-stmt)), (continue, 77 (expression-stmt)), (break, 79 (expression-stmt)), (;, 81 (expression-stmt) (success))]
75 (expression-stmt) to -> [(;, 76 (expression-stmt) (success))]
77 (expression-stmt) to -> [(;, 78 (expression-stmt) (success))]
79 (expression-stmt) to -> [(;, 80 (expression-stmt) (success))]
81 (expression-stmt) (success)
76 (expression-stmt) (success)
78 (expression-stmt) (success)
80 (expression-stmt) (success)

selection-stmt
82 (selection-stmt) to -> [(if, 83 (selection-stmt))]
83 (selection-stmt) to -> [((, 84 (selection-stmt))]
84 (selection-stmt) to -> [(expression, 85 (selection-stmt))]
85 (selection-stmt) to -> [(), 86 (selection-stmt))]
86 (selection-stmt) to -> [(statement, 87 (selection-stmt))]
87 (selection-stmt) to -> [(else, 88 (selection-stmt))]
88 (selection-stmt) to -> [(statement, 89 (selection-stmt) (success))]
89 (selection-stmt) (success)

iteration-stmt
90 (iteration-stmt) to -> [(while, 91 (iteration-stmt))]
91 (iteration-stmt) to -> [((, 92 (iteration-stmt))]
92 (iteration-stmt) to -> [(expression, 93 (iteration-stmt))]
93 (iteration-stmt) to -> [(), 94 (iteration-stmt))]
94 (iteration-stmt) to -> [(statement, 95 (iteration-stmt) (success))]
95 (iteration-stmt) (success)

return-stmt
96 (return-stmt) to -> [(return, 97 (return-stmt))]
97 (return-stmt) to -> [(rest-of-return-stmt, 98 (return-stmt) (success))]
98 (return-stmt) (success)

rest-of-return-stmt
99 (rest-of-return-stmt) to -> [(;, 100 (rest-of-return-stmt) (success)), (expression, 101 (rest-of-return-stmt))]
100 (rest-of-return-stmt) (success)
101 (rest-of-return-stmt) to -> [(;, 102 (rest-of-return-stmt) (success))]
102 (rest-of-return-stmt) (success)

switch-stmt
103 (switch-stmt) to -> [(switch, 104 (switch-stmt))]
104 (switch-stmt) to -> [((, 105 (switch-stmt))]
105 (switch-stmt) to -> [(expression, 106 (switch-stmt))]
106 (switch-stmt) to -> [(), 107 (switch-stmt))]
107 (switch-stmt) to -> [({, 108 (switch-stmt))]
108 (switch-stmt) to -> [(case-stmts, 109 (switch-stmt))]
109 (switch-stmt) to -> [(default-stmt, 110 (switch-stmt))]
110 (switch-stmt) to -> [(}, 111 (switch-stmt) (success))]
111 (switch-stmt) (success)

case-stmts
112 (case-stmts) to -> [(case-stmt, 113 (case-stmts)), ((), 115 (case-stmts) (success))]
113 (case-stmts) to -> [(case-stmts, 114 (case-stmts) (success))]
115 (case-stmts) (success)
114 (case-stmts) (success)

case-stmt
116 (case-stmt) to -> [(case, 117 (case-stmt))]
117 (case-stmt) to -> [(NUM, 118 (case-stmt))]
118 (case-stmt) to -> [(:, 119 (case-stmt))]
119 (case-stmt) to -> [(statement-list, 120 (case-stmt) (success))]
120 (case-stmt) (success)

default-stmt
121 (default-stmt) to -> [(default, 122 (default-stmt)), ((), 125 (default-stmt) (success))]
122 (default-stmt) to -> [(:, 123 (default-stmt))]
125 (default-stmt) (success)
123 (default-stmt) to -> [(statement-list, 124 (default-stmt) (success))]
124 (default-stmt) (success)

expression
126 (expression) to -> [(simple-expression, 127 (expression) (success)), (ID, 128 (expression))]
127 (expression) (success)
128 (expression) to -> [(id-expression, 129 (expression) (success))]
129 (expression) (success)

id-expression
130 (id-expression) to -> [(=, 131 (id-expression)), (id-simple-expression, 133 (id-expression) (success)), ([, 134 (id-expression))]
131 (id-expression) to -> [(expression, 132 (id-expression) (success))]
133 (id-expression) (success)
134 (id-expression) to -> [(expression, 135 (id-expression))]
132 (id-expression) (success)
135 (id-expression) to -> [(], 136 (id-expression))]
136 (id-expression) to -> [(bracket-id-expression, 137 (id-expression) (success))]
137 (id-expression) (success)

bracket-id-expression
138 (bracket-id-expression) to -> [(=, 139 (bracket-id-expression)), ((), 141 (bracket-id-expression) (success))]
139 (bracket-id-expression) to -> [(expression, 140 (bracket-id-expression) (success))]
141 (bracket-id-expression) (success)
140 (bracket-id-expression) (success)

simple-expression
142 (simple-expression) to -> [(additive-expression, 143 (simple-expression))]
143 (simple-expression) to -> [(rest-of-simple-expression, 144 (simple-expression) (success))]
144 (simple-expression) (success)

id-simple-expression
145 (id-simple-expression) to -> [(id-additive-expression, 146 (id-simple-expression))]
146 (id-simple-expression) to -> [(rest-of-simple-expression, 147 (id-simple-expression) (success))]
147 (id-simple-expression) (success)

rest-of-simple-expression
148 (rest-of-simple-expression) to -> [(RELOP, 149 (rest-of-simple-expression)), ((), 151 (rest-of-simple-expression) (success))]
149 (rest-of-simple-expression) to -> [(additive-expression, 150 (rest-of-simple-expression) (success))]
151 (rest-of-simple-expression) (success)
150 (rest-of-simple-expression) (success)

additive-expression
152 (additive-expression) to -> [(term, 153 (additive-expression))]
153 (additive-expression) to -> [(additive-expression-prime, 154 (additive-expression) (success))]
154 (additive-expression) (success)

id-additive-expression
155 (id-additive-expression) to -> [(id-term, 156 (id-additive-expression))]
156 (id-additive-expression) to -> [(additive-expression-prime, 157 (id-additive-expression) (success))]
157 (id-additive-expression) (success)

additive-expression-prime
158 (additive-expression-prime) to -> [(addop, 159 (additive-expression-prime)), ((), 162 (additive-expression-prime) (success))]
159 (additive-expression-prime) to -> [(term, 160 (additive-expression-prime))]
162 (additive-expression-prime) (success)
160 (additive-expression-prime) to -> [(additive-expression-prime, 161 (additive-expression-prime) (success))]
161 (additive-expression-prime) (success)

addop
163 (addop) to -> [(+, 164 (addop) (success)), (-, 165 (addop) (success))]
164 (addop) (success)
165 (addop) (success)

term
166 (term) to -> [(factor, 167 (term))]
167 (term) to -> [(term-prime, 168 (term) (success))]
168 (term) (success)

id-term
169 (id-term) to -> [(reference, 170 (id-term))]
170 (id-term) to -> [(term-prime, 171 (id-term) (success))]
171 (id-term) (success)

term-prime
172 (term-prime) to -> [(*, 173 (term-prime)), ((), 176 (term-prime) (success))]
173 (term-prime) to -> [(factor, 174 (term-prime))]
176 (term-prime) (success)
174 (term-prime) to -> [(term-prime, 175 (term-prime) (success))]
175 (term-prime) (success)

factor
177 (factor) to -> [((, 178 (factor)), (NUM, 181 (factor) (success))]
178 (factor) to -> [(expression, 179 (factor))]
181 (factor) (success)
179 (factor) to -> [(), 180 (factor) (success))]
180 (factor) (success)

reference
182 (reference) to -> [(call, 183 (reference) (success)), ((), 184 (reference) (success))]
183 (reference) (success)
184 (reference) (success)

call
185 (call) to -> [((, 186 (call))]
186 (call) to -> [(args, 187 (call))]
187 (call) to -> [(), 188 (call) (success))]
188 (call) (success)

args
189 (args) to -> [(arg-list, 190 (args) (success)), ((), 191 (args) (success))]
190 (args) (success)
191 (args) (success)

arg-list
192 (arg-list) to -> [(expression, 193 (arg-list))]
193 (arg-list) to -> [(arg-list-prime, 194 (arg-list) (success))]
194 (arg-list) (success)

arg-list-prime
195 (arg-list-prime) to -> [(,, 196 (arg-list-prime)), ((), 199 (arg-list-prime) (success))]
196 (arg-list-prime) to -> [(expression, 197 (arg-list-prime))]
199 (arg-list-prime) (success)
197 (arg-list-prime) to -> [(arg-list-prime, 198 (arg-list-prime) (success))]
198 (arg-list-prime) (success)
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
|rest-of-var-declaration|; [|( ; EOF ID NUM break continue if int return switch void while { }|
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

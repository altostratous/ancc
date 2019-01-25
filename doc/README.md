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
2. declaration-list → type-specifier #PushID ID declaration #PopID declaration-list | ε
3. declaration → var-declaration | fun-declaration
4. var-declaration → ; | [ #ArrayDefinition NUM ] ;
5. type-specifier → int | void
6. fun-declaration → ( params ) compound-stmt
7. params → int-starting-param-list | void-starting-param-list
8. void-starting-param-list → void rest-of-void-starting-param-list
9. rest-of-void-starting-param-list → ID rest-of-param param-list-prime | ε
10. int-starting-param-list → int ID rest-of-param param-list-prime
11. param-list-prime → , param param-list-prime | ε
12. param → type-specifier ID rest-of-param
13. rest-of-param → ε | [ ]
14. compound-stmt → { declaration-list statement-list }
15. statement-list → statement statement-list | ε
16. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
17. expression-stmt → expression ; #PopID  | continue ; #Continue | break ; #Break | ;
18. selection-stmt → if ( expression ) #IfSave statement #IfJumpSave else statement #IfJump
19. iteration-stmt → while #WhileLabel ( expression ) #WhileSave statement #While
20. return-stmt → return rest-of-return-stmt
21. rest-of-return-stmt → ; | expression ;
22. switch-stmt → switch #SwitchSave ( expression ) { case-stmts default-stmt } #Switch
23. case-stmts → case-stmt case-stmts | ε
24. case-stmt → case #CaseInsert NUM : statement-list
25. default-stmt → default #DefaultInsert : statement-list | ε
26. expression → simple-expression | #PushID ID id-expression
27. id-expression → = expression #Assign | id-simple-expression | [ expression ] bracket-id-expression
28. bracket-id-expression → = expression #AssignArray | #ArrayAccess id-simple-expression
29. simple-expression → additive-expression rest-of-simple-expression
30. id-simple-expression → id-additive-expression rest-of-simple-expression
31. rest-of-simple-expression → #PushRelOp RELOP addop-relop-rest #RelOp | ε
32. addop-relop-rest → additive-expression | #PushID ID addop-relop-rest-reference
32. addop-relop-rest-reference → id-additive-expression | [ expression ] #ArrayAccess id-additive-expression
33. additive-expression → term additive-expression-prime
34. id-additive-expression → id-term additive-expression-prime
35. additive-expression-prime → #PushAddOp + addop-relop-rest #AddOp | #PushSubOp - minus-expr | ε
36. minus-expr → term #AddOp additive-expression-prime | #PushID ID id-term #AddOp additive-expression-prime
37. term → factor term-prime
38. id-term → reference term-prime
39. term-prime → * mult-rest #MultOp | ε
40. mult-rest → term | #PushID ID id-term
41. factor → ( expression ) | #PushNum NUM
42. reference → call | ε
43. call → ( args ) #Print
44. args → arg-list | ε
45. arg-list → expression arg-list-prime
46. arg-list-prime → , expression arg-list-prime | ε```
## State Diagram
```

#AddOp
241 (#AddOp) to -> [((), 242 (#AddOp) (success))]
242 (#AddOp) (success)

#ArrayAccess
194 (#ArrayAccess) to -> [((), 195 (#ArrayAccess) (success))]
195 (#ArrayAccess) (success)

#ArrayDefinition
26 (#ArrayDefinition) to -> [((), 27 (#ArrayDefinition) (success))]
27 (#ArrayDefinition) (success)

#Assign
184 (#Assign) to -> [((), 185 (#Assign) (success))]
185 (#Assign) (success)

#AssignArray
192 (#AssignArray) to -> [((), 193 (#AssignArray) (success))]
193 (#AssignArray) (success)

#Break
94 (#Break) to -> [((), 95 (#Break) (success))]
95 (#Break) (success)

#CaseInsert
160 (#CaseInsert) to -> [((), 161 (#CaseInsert) (success))]
161 (#CaseInsert) (success)

#Continue
92 (#Continue) to -> [((), 93 (#Continue) (success))]
93 (#Continue) (success)

#DefaultInsert
168 (#DefaultInsert) to -> [((), 169 (#DefaultInsert) (success))]
169 (#DefaultInsert) (success)

#IfJump
111 (#IfJump) to -> [((), 112 (#IfJump) (success))]
112 (#IfJump) (success)

#IfJumpSave
109 (#IfJumpSave) to -> [((), 110 (#IfJumpSave) (success))]
110 (#IfJumpSave) (success)

#IfSave
107 (#IfSave) to -> [((), 108 (#IfSave) (success))]
108 (#IfSave) (success)

#MultOp
265 (#MultOp) to -> [((), 266 (#MultOp) (success))]
266 (#MultOp) (success)

#PopID
14 (#PopID) to -> [((), 15 (#PopID) (success))]
15 (#PopID) (success)

#Print
288 (#Print) to -> [((), 289 (#Print) (success))]
289 (#Print) (success)

#PushAddOp
239 (#PushAddOp) to -> [((), 240 (#PushAddOp) (success))]
240 (#PushAddOp) (success)

#PushID
12 (#PushID) to -> [((), 13 (#PushID) (success))]
13 (#PushID) (success)

#PushNum
278 (#PushNum) to -> [((), 279 (#PushNum) (success))]
279 (#PushNum) (success)

#PushRelOp
208 (#PushRelOp) to -> [((), 209 (#PushRelOp) (success))]
209 (#PushRelOp) (success)

#PushSubOp
243 (#PushSubOp) to -> [((), 244 (#PushSubOp) (success))]
244 (#PushSubOp) (success)

#RelOp
210 (#RelOp) to -> [((), 211 (#RelOp) (success))]
211 (#RelOp) (success)

#Switch
148 (#Switch) to -> [((), 149 (#Switch) (success))]
149 (#Switch) (success)

#SwitchSave
146 (#SwitchSave) to -> [((), 147 (#SwitchSave) (success))]
147 (#SwitchSave) (success)

#While
126 (#While) to -> [((), 127 (#While) (success))]
127 (#While) (success)

#WhileLabel
122 (#WhileLabel) to -> [((), 123 (#WhileLabel) (success))]
123 (#WhileLabel) (success)

#WhileSave
124 (#WhileSave) to -> [((), 125 (#WhileSave) (success))]
125 (#WhileSave) (success)

additive-expression
224 (additive-expression) to -> [(term, 225 (additive-expression))]
225 (additive-expression) to -> [(additive-expression-prime, 226 (additive-expression) (success))]
226 (additive-expression) (success)

additive-expression-prime
230 (additive-expression-prime) to -> [(#PushAddOp, 231 (additive-expression-prime)), (#PushSubOp, 235 (additive-expression-prime)), ((), 238 (additive-expression-prime) (success))]
231 (additive-expression-prime) to -> [(+, 232 (additive-expression-prime))]
235 (additive-expression-prime) to -> [(-, 236 (additive-expression-prime))]
238 (additive-expression-prime) (success)
232 (additive-expression-prime) to -> [(addop-relop-rest, 233 (additive-expression-prime))]
236 (additive-expression-prime) to -> [(minus-expr, 237 (additive-expression-prime) (success))]
233 (additive-expression-prime) to -> [(#AddOp, 234 (additive-expression-prime) (success))]
237 (additive-expression-prime) (success)
234 (additive-expression-prime) (success)

addop-relop-rest
212 (addop-relop-rest) to -> [(additive-expression, 213 (addop-relop-rest) (success)), (#PushID, 214 (addop-relop-rest))]
213 (addop-relop-rest) (success)
214 (addop-relop-rest) to -> [(ID, 215 (addop-relop-rest))]
215 (addop-relop-rest) to -> [(addop-relop-rest-reference, 216 (addop-relop-rest) (success))]
216 (addop-relop-rest) (success)

addop-relop-rest-reference
217 (addop-relop-rest-reference) to -> [(id-additive-expression, 218 (addop-relop-rest-reference) (success)), ([, 219 (addop-relop-rest-reference))]
218 (addop-relop-rest-reference) (success)
219 (addop-relop-rest-reference) to -> [(expression, 220 (addop-relop-rest-reference))]
220 (addop-relop-rest-reference) to -> [(], 221 (addop-relop-rest-reference))]
221 (addop-relop-rest-reference) to -> [(#ArrayAccess, 222 (addop-relop-rest-reference))]
222 (addop-relop-rest-reference) to -> [(id-additive-expression, 223 (addop-relop-rest-reference) (success))]
223 (addop-relop-rest-reference) (success)

arg-list
293 (arg-list) to -> [(expression, 294 (arg-list))]
294 (arg-list) to -> [(arg-list-prime, 295 (arg-list) (success))]
295 (arg-list) (success)

arg-list-prime
296 (arg-list-prime) to -> [(,, 297 (arg-list-prime)), ((), 300 (arg-list-prime) (success))]
297 (arg-list-prime) to -> [(expression, 298 (arg-list-prime))]
300 (arg-list-prime) (success)
298 (arg-list-prime) to -> [(arg-list-prime, 299 (arg-list-prime) (success))]
299 (arg-list-prime) (success)

args
290 (args) to -> [(arg-list, 291 (args) (success)), ((), 292 (args) (success))]
291 (args) (success)
292 (args) (success)

bracket-id-expression
186 (bracket-id-expression) to -> [(=, 187 (bracket-id-expression)), (#ArrayAccess, 190 (bracket-id-expression))]
187 (bracket-id-expression) to -> [(expression, 188 (bracket-id-expression))]
190 (bracket-id-expression) to -> [(id-simple-expression, 191 (bracket-id-expression) (success))]
188 (bracket-id-expression) to -> [(#AssignArray, 189 (bracket-id-expression) (success))]
191 (bracket-id-expression) (success)
189 (bracket-id-expression) (success)

call
283 (call) to -> [((, 284 (call))]
284 (call) to -> [(args, 285 (call))]
285 (call) to -> [(), 286 (call))]
286 (call) to -> [(#Print, 287 (call) (success))]
287 (call) (success)

case-stmt
154 (case-stmt) to -> [(case, 155 (case-stmt))]
155 (case-stmt) to -> [(#CaseInsert, 156 (case-stmt))]
156 (case-stmt) to -> [(NUM, 157 (case-stmt))]
157 (case-stmt) to -> [(:, 158 (case-stmt))]
158 (case-stmt) to -> [(statement-list, 159 (case-stmt) (success))]
159 (case-stmt) (success)

case-stmts
150 (case-stmts) to -> [(case-stmt, 151 (case-stmts)), ((), 153 (case-stmts) (success))]
151 (case-stmts) to -> [(case-stmts, 152 (case-stmts) (success))]
153 (case-stmts) (success)
152 (case-stmts) (success)

compound-stmt
65 (compound-stmt) to -> [({, 66 (compound-stmt))]
66 (compound-stmt) to -> [(declaration-list, 67 (compound-stmt))]
67 (compound-stmt) to -> [(statement-list, 68 (compound-stmt))]
68 (compound-stmt) to -> [(}, 69 (compound-stmt) (success))]
69 (compound-stmt) (success)

declaration
16 (declaration) to -> [(var-declaration, 17 (declaration) (success)), (fun-declaration, 18 (declaration) (success))]
17 (declaration) (success)
18 (declaration) (success)

declaration-list
4 (declaration-list) to -> [(type-specifier, 5 (declaration-list)), ((), 11 (declaration-list) (success))]
5 (declaration-list) to -> [(#PushID, 6 (declaration-list))]
11 (declaration-list) (success)
6 (declaration-list) to -> [(ID, 7 (declaration-list))]
7 (declaration-list) to -> [(declaration, 8 (declaration-list))]
8 (declaration-list) to -> [(#PopID, 9 (declaration-list))]
9 (declaration-list) to -> [(declaration-list, 10 (declaration-list) (success))]
10 (declaration-list) (success)

default-stmt
162 (default-stmt) to -> [(default, 163 (default-stmt)), ((), 167 (default-stmt) (success))]
163 (default-stmt) to -> [(#DefaultInsert, 164 (default-stmt))]
167 (default-stmt) (success)
164 (default-stmt) to -> [(:, 165 (default-stmt))]
165 (default-stmt) to -> [(statement-list, 166 (default-stmt) (success))]
166 (default-stmt) (success)

expression
170 (expression) to -> [(simple-expression, 171 (expression) (success)), (#PushID, 172 (expression))]
171 (expression) (success)
172 (expression) to -> [(ID, 173 (expression))]
173 (expression) to -> [(id-expression, 174 (expression) (success))]
174 (expression) (success)

expression-stmt
81 (expression-stmt) to -> [(expression, 82 (expression-stmt)), (continue, 85 (expression-stmt)), (break, 88 (expression-stmt)), (;, 91 (expression-stmt) (success))]
82 (expression-stmt) to -> [(;, 83 (expression-stmt))]
85 (expression-stmt) to -> [(;, 86 (expression-stmt))]
88 (expression-stmt) to -> [(;, 89 (expression-stmt))]
91 (expression-stmt) (success)
83 (expression-stmt) to -> [(#PopID, 84 (expression-stmt) (success))]
86 (expression-stmt) to -> [(#Continue, 87 (expression-stmt) (success))]
89 (expression-stmt) to -> [(#Break, 90 (expression-stmt) (success))]
84 (expression-stmt) (success)
87 (expression-stmt) (success)
90 (expression-stmt) (success)

factor
272 (factor) to -> [((, 273 (factor)), (#PushNum, 276 (factor))]
273 (factor) to -> [(expression, 274 (factor))]
276 (factor) to -> [(NUM, 277 (factor) (success))]
274 (factor) to -> [(), 275 (factor) (success))]
277 (factor) (success)
275 (factor) (success)

fun-declaration
31 (fun-declaration) to -> [((, 32 (fun-declaration))]
32 (fun-declaration) to -> [(params, 33 (fun-declaration))]
33 (fun-declaration) to -> [(), 34 (fun-declaration))]
34 (fun-declaration) to -> [(compound-stmt, 35 (fun-declaration) (success))]
35 (fun-declaration) (success)

id-additive-expression
227 (id-additive-expression) to -> [(id-term, 228 (id-additive-expression))]
228 (id-additive-expression) to -> [(additive-expression-prime, 229 (id-additive-expression) (success))]
229 (id-additive-expression) (success)

id-expression
175 (id-expression) to -> [(=, 176 (id-expression)), (id-simple-expression, 179 (id-expression) (success)), ([, 180 (id-expression))]
176 (id-expression) to -> [(expression, 177 (id-expression))]
179 (id-expression) (success)
180 (id-expression) to -> [(expression, 181 (id-expression))]
177 (id-expression) to -> [(#Assign, 178 (id-expression) (success))]
181 (id-expression) to -> [(], 182 (id-expression))]
178 (id-expression) (success)
182 (id-expression) to -> [(bracket-id-expression, 183 (id-expression) (success))]
183 (id-expression) (success)

id-simple-expression
199 (id-simple-expression) to -> [(id-additive-expression, 200 (id-simple-expression))]
200 (id-simple-expression) to -> [(rest-of-simple-expression, 201 (id-simple-expression) (success))]
201 (id-simple-expression) (success)

id-term
257 (id-term) to -> [(reference, 258 (id-term))]
258 (id-term) to -> [(term-prime, 259 (id-term) (success))]
259 (id-term) (success)

int-starting-param-list
47 (int-starting-param-list) to -> [(int, 48 (int-starting-param-list))]
48 (int-starting-param-list) to -> [(ID, 49 (int-starting-param-list))]
49 (int-starting-param-list) to -> [(rest-of-param, 50 (int-starting-param-list))]
50 (int-starting-param-list) to -> [(param-list-prime, 51 (int-starting-param-list) (success))]
51 (int-starting-param-list) (success)

iteration-stmt
113 (iteration-stmt) to -> [(while, 114 (iteration-stmt))]
114 (iteration-stmt) to -> [(#WhileLabel, 115 (iteration-stmt))]
115 (iteration-stmt) to -> [((, 116 (iteration-stmt))]
116 (iteration-stmt) to -> [(expression, 117 (iteration-stmt))]
117 (iteration-stmt) to -> [(), 118 (iteration-stmt))]
118 (iteration-stmt) to -> [(#WhileSave, 119 (iteration-stmt))]
119 (iteration-stmt) to -> [(statement, 120 (iteration-stmt))]
120 (iteration-stmt) to -> [(#While, 121 (iteration-stmt) (success))]
121 (iteration-stmt) (success)

minus-expr
245 (minus-expr) to -> [(term, 246 (minus-expr)), (#PushID, 249 (minus-expr))]
246 (minus-expr) to -> [(#AddOp, 247 (minus-expr))]
249 (minus-expr) to -> [(ID, 250 (minus-expr))]
247 (minus-expr) to -> [(additive-expression-prime, 248 (minus-expr) (success))]
250 (minus-expr) to -> [(id-term, 251 (minus-expr))]
248 (minus-expr) (success)
251 (minus-expr) to -> [(#AddOp, 252 (minus-expr))]
252 (minus-expr) to -> [(additive-expression-prime, 253 (minus-expr) (success))]
253 (minus-expr) (success)

mult-rest
267 (mult-rest) to -> [(term, 268 (mult-rest) (success)), (#PushID, 269 (mult-rest))]
268 (mult-rest) (success)
269 (mult-rest) to -> [(ID, 270 (mult-rest))]
270 (mult-rest) to -> [(id-term, 271 (mult-rest) (success))]
271 (mult-rest) (success)

param
57 (param) to -> [(type-specifier, 58 (param))]
58 (param) to -> [(ID, 59 (param))]
59 (param) to -> [(rest-of-param, 60 (param) (success))]
60 (param) (success)

param-list-prime
52 (param-list-prime) to -> [(,, 53 (param-list-prime)), ((), 56 (param-list-prime) (success))]
53 (param-list-prime) to -> [(param, 54 (param-list-prime))]
56 (param-list-prime) (success)
54 (param-list-prime) to -> [(param-list-prime, 55 (param-list-prime) (success))]
55 (param-list-prime) (success)

params
36 (params) to -> [(int-starting-param-list, 37 (params) (success)), (void-starting-param-list, 38 (params) (success))]
37 (params) (success)
38 (params) (success)

program
1 (program) to -> [(declaration-list, 2 (program))]
2 (program) to -> [(EOF, 3 (program) (success))]
3 (program) (success)

reference
280 (reference) to -> [(call, 281 (reference) (success)), ((), 282 (reference) (success))]
281 (reference) (success)
282 (reference) (success)

rest-of-param
61 (rest-of-param) to -> [((), 62 (rest-of-param) (success)), ([, 63 (rest-of-param))]
62 (rest-of-param) (success)
63 (rest-of-param) to -> [(], 64 (rest-of-param) (success))]
64 (rest-of-param) (success)

rest-of-return-stmt
131 (rest-of-return-stmt) to -> [(;, 132 (rest-of-return-stmt) (success)), (expression, 133 (rest-of-return-stmt))]
132 (rest-of-return-stmt) (success)
133 (rest-of-return-stmt) to -> [(;, 134 (rest-of-return-stmt) (success))]
134 (rest-of-return-stmt) (success)

rest-of-simple-expression
202 (rest-of-simple-expression) to -> [(#PushRelOp, 203 (rest-of-simple-expression)), ((), 207 (rest-of-simple-expression) (success))]
203 (rest-of-simple-expression) to -> [(RELOP, 204 (rest-of-simple-expression))]
207 (rest-of-simple-expression) (success)
204 (rest-of-simple-expression) to -> [(addop-relop-rest, 205 (rest-of-simple-expression))]
205 (rest-of-simple-expression) to -> [(#RelOp, 206 (rest-of-simple-expression) (success))]
206 (rest-of-simple-expression) (success)

rest-of-void-starting-param-list
42 (rest-of-void-starting-param-list) to -> [(ID, 43 (rest-of-void-starting-param-list)), ((), 46 (rest-of-void-starting-param-list) (success))]
43 (rest-of-void-starting-param-list) to -> [(rest-of-param, 44 (rest-of-void-starting-param-list))]
46 (rest-of-void-starting-param-list) (success)
44 (rest-of-void-starting-param-list) to -> [(param-list-prime, 45 (rest-of-void-starting-param-list) (success))]
45 (rest-of-void-starting-param-list) (success)

return-stmt
128 (return-stmt) to -> [(return, 129 (return-stmt))]
129 (return-stmt) to -> [(rest-of-return-stmt, 130 (return-stmt) (success))]
130 (return-stmt) (success)

selection-stmt
96 (selection-stmt) to -> [(if, 97 (selection-stmt))]
97 (selection-stmt) to -> [((, 98 (selection-stmt))]
98 (selection-stmt) to -> [(expression, 99 (selection-stmt))]
99 (selection-stmt) to -> [(), 100 (selection-stmt))]
100 (selection-stmt) to -> [(#IfSave, 101 (selection-stmt))]
101 (selection-stmt) to -> [(statement, 102 (selection-stmt))]
102 (selection-stmt) to -> [(#IfJumpSave, 103 (selection-stmt))]
103 (selection-stmt) to -> [(else, 104 (selection-stmt))]
104 (selection-stmt) to -> [(statement, 105 (selection-stmt))]
105 (selection-stmt) to -> [(#IfJump, 106 (selection-stmt) (success))]
106 (selection-stmt) (success)

simple-expression
196 (simple-expression) to -> [(additive-expression, 197 (simple-expression))]
197 (simple-expression) to -> [(rest-of-simple-expression, 198 (simple-expression) (success))]
198 (simple-expression) (success)

statement
74 (statement) to -> [(expression-stmt, 75 (statement) (success)), (compound-stmt, 76 (statement) (success)), (selection-stmt, 77 (statement) (success)), (iteration-stmt, 78 (statement) (success)), (return-stmt, 79 (statement) (success)), (switch-stmt, 80 (statement) (success))]
75 (statement) (success)
76 (statement) (success)
77 (statement) (success)
78 (statement) (success)
79 (statement) (success)
80 (statement) (success)

statement-list
70 (statement-list) to -> [(statement, 71 (statement-list)), ((), 73 (statement-list) (success))]
71 (statement-list) to -> [(statement-list, 72 (statement-list) (success))]
73 (statement-list) (success)
72 (statement-list) (success)

switch-stmt
135 (switch-stmt) to -> [(switch, 136 (switch-stmt))]
136 (switch-stmt) to -> [(#SwitchSave, 137 (switch-stmt))]
137 (switch-stmt) to -> [((, 138 (switch-stmt))]
138 (switch-stmt) to -> [(expression, 139 (switch-stmt))]
139 (switch-stmt) to -> [(), 140 (switch-stmt))]
140 (switch-stmt) to -> [({, 141 (switch-stmt))]
141 (switch-stmt) to -> [(case-stmts, 142 (switch-stmt))]
142 (switch-stmt) to -> [(default-stmt, 143 (switch-stmt))]
143 (switch-stmt) to -> [(}, 144 (switch-stmt))]
144 (switch-stmt) to -> [(#Switch, 145 (switch-stmt) (success))]
145 (switch-stmt) (success)

term
254 (term) to -> [(factor, 255 (term))]
255 (term) to -> [(term-prime, 256 (term) (success))]
256 (term) (success)

term-prime
260 (term-prime) to -> [(*, 261 (term-prime)), ((), 264 (term-prime) (success))]
261 (term-prime) to -> [(mult-rest, 262 (term-prime))]
264 (term-prime) (success)
262 (term-prime) to -> [(#MultOp, 263 (term-prime) (success))]
263 (term-prime) (success)

type-specifier
28 (type-specifier) to -> [(int, 29 (type-specifier) (success)), (void, 30 (type-specifier) (success))]
29 (type-specifier) (success)
30 (type-specifier) (success)

var-declaration
19 (var-declaration) to -> [(;, 20 (var-declaration) (success)), ([, 21 (var-declaration))]
20 (var-declaration) (success)
21 (var-declaration) to -> [(#ArrayDefinition, 22 (var-declaration))]
22 (var-declaration) to -> [(NUM, 23 (var-declaration))]
23 (var-declaration) to -> [(], 24 (var-declaration))]
24 (var-declaration) to -> [(;, 25 (var-declaration) (success))]
25 (var-declaration) (success)

void-starting-param-list
39 (void-starting-param-list) to -> [(void, 40 (void-starting-param-list))]
40 (void-starting-param-list) to -> [(rest-of-void-starting-param-list, 41 (void-starting-param-list) (success))]
41 (void-starting-param-list) (success)
```
## First and Follow
|Non-terminal|First|Follow|
|:----------:|:---:|:----:|
|#AddOp|ε|) + , - ; RELOP ]|
|#ArrayAccess|ε|( ) * + , - ; RELOP ]|
|#ArrayDefinition|ε|NUM|
|#Assign|ε|) , ; ]|
|#AssignArray|ε|) , ; ]|
|#Break|ε|( ; ID NUM break case continue default else if return switch while { }|
|#CaseInsert|ε|NUM|
|#Continue|ε|( ; ID NUM break case continue default else if return switch while { }|
|#DefaultInsert|ε|:|
|#IfJump|ε|( ; ID NUM break case continue default else if return switch while { }|
|#IfJumpSave|ε|else|
|#IfSave|ε|( ; ID NUM break continue if return switch while {|
|#MultOp|ε|) + , - ; RELOP ]|
|#PopID|ε|( ; EOF ID NUM break case continue default else if int return switch void while { }|
|#Print|ε|) * + , - ; RELOP ]|
|#PushAddOp|ε|+|
|#PushID|ε|ID|
|#PushNum|ε|NUM|
|#PushRelOp|ε|RELOP|
|#PushSubOp|ε|-|
|#RelOp|ε|) , ; ]|
|#Switch|ε|( ; ID NUM break case continue default else if return switch while { }|
|#SwitchSave|ε|(|
|#While|ε|( ; ID NUM break case continue default else if return switch while { }|
|#WhileLabel|ε|(|
|#WhileSave|ε|( ; ID NUM break continue if return switch while {|
|additive-expression|( NUM|) , ; RELOP ]|
|additive-expression-prime|+ - ε|) , ; RELOP ]|
|addop-relop-rest|( ID NUM|) , ; RELOP ]|
|addop-relop-rest-reference|( * + - [ ε|) , ; RELOP ]|
|arg-list|( ID NUM|)|
|arg-list-prime|, ε|)|
|args|( ID NUM ε|)|
|bracket-id-expression|( * + - = RELOP ε|) , ; ]|
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
|minus-expr|( ID NUM|) , ; RELOP ]|
|mult-rest|( ID NUM|) + , - ; RELOP ]|
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

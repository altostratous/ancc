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
1. program → declaration-list #CallMain EOF
2. declaration-list → type-specifier #PushID ID declaration #PopID declaration-list | ε
3. declaration → var-declaration | fun-declaration
4. var-declaration → ; | [ #ArrayDefinition NUM ] ;
5. type-specifier → int | void
6. fun-declaration → ( #IncreaseScope params ) #FunctionSave fun-compound-stmt #Function
7. params → int-starting-param-list | void-starting-param-list
8. void-starting-param-list → void rest-of-void-starting-param-list
9. rest-of-void-starting-param-list → ID rest-of-param param-list-prime | ε
10. int-starting-param-list → int #PullID ID rest-of-param param-list-prime
11. param-list-prime → , param param-list-prime | ε
12. param → type-specifier #PullID ID rest-of-param
13. rest-of-param → ε | [ ]
14. compound-stmt → { #IncreaseScope declaration-list statement-list #DecreaseScope }
15. statement-list → statement statement-list | ε
16. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
17. expression-stmt → expression ; #PopID  | continue ; #Continue | break ; #Break | ;
18. selection-stmt → if ( expression ) #IfSave statement #IfJumpSave else statement #IfJump
19. iteration-stmt → while #WhileLabel ( expression ) #WhileSave statement #While
20. return-stmt → return rest-of-return-stmt #Function
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
33. addop-relop-rest-reference → id-additive-expression | [ expression ] #ArrayAccess id-additive-expression
34. additive-expression → term additive-expression-prime
35. id-additive-expression → id-term additive-expression-prime
36. additive-expression-prime → #PushAddOp + addop-relop-rest #AddOp | #PushSubOp - minus-expr | ε
37. minus-expr → term #AddOp additive-expression-prime | #PushID ID id-term #AddOp additive-expression-prime
38. term → factor term-prime
39. id-term → reference term-prime
40. term-prime → * mult-rest #MultOp | ε
41. mult-rest → term | #PushID ID id-term
42. factor → ( expression ) | #PushNum NUM
43. reference → call | ε
44. call → ( args ) #Print
45. args → arg-list | ε
46. arg-list → expression arg-list-prime
47. arg-list-prime → , expression arg-list-prime | ε
48. fun-compound-stmt → { declaration-list statement-list #DecreaseScope }

```
## State Diagram
```

#AddOp
262 (#AddOp) to -> [((), 263 (#AddOp) (success))]
263 (#AddOp) (success)

#ArrayAccess
215 (#ArrayAccess) to -> [((), 216 (#ArrayAccess) (success))]
216 (#ArrayAccess) (success)

#ArrayDefinition
29 (#ArrayDefinition) to -> [((), 30 (#ArrayDefinition) (success))]
30 (#ArrayDefinition) (success)

#Assign
205 (#Assign) to -> [((), 206 (#Assign) (success))]
206 (#Assign) (success)

#AssignArray
213 (#AssignArray) to -> [((), 214 (#AssignArray) (success))]
214 (#AssignArray) (success)

#Break
114 (#Break) to -> [((), 115 (#Break) (success))]
115 (#Break) (success)

#CallMain
5 (#CallMain) to -> [((), 6 (#CallMain) (success))]
6 (#CallMain) (success)

#CaseInsert
181 (#CaseInsert) to -> [((), 182 (#CaseInsert) (success))]
182 (#CaseInsert) (success)

#Continue
112 (#Continue) to -> [((), 113 (#Continue) (success))]
113 (#Continue) (success)

#DecreaseScope
88 (#DecreaseScope) to -> [((), 89 (#DecreaseScope) (success))]
89 (#DecreaseScope) (success)

#DefaultInsert
189 (#DefaultInsert) to -> [((), 190 (#DefaultInsert) (success))]
190 (#DefaultInsert) (success)

#Function
46 (#Function) to -> [((), 47 (#Function) (success))]
47 (#Function) (success)

#FunctionSave
44 (#FunctionSave) to -> [((), 45 (#FunctionSave) (success))]
45 (#FunctionSave) (success)

#IfJump
131 (#IfJump) to -> [((), 132 (#IfJump) (success))]
132 (#IfJump) (success)

#IfJumpSave
129 (#IfJumpSave) to -> [((), 130 (#IfJumpSave) (success))]
130 (#IfJumpSave) (success)

#IfSave
127 (#IfSave) to -> [((), 128 (#IfSave) (success))]
128 (#IfSave) (success)

#IncreaseScope
42 (#IncreaseScope) to -> [((), 43 (#IncreaseScope) (success))]
43 (#IncreaseScope) (success)

#MultOp
286 (#MultOp) to -> [((), 287 (#MultOp) (success))]
287 (#MultOp) (success)

#PopID
17 (#PopID) to -> [((), 18 (#PopID) (success))]
18 (#PopID) (success)

#Print
309 (#Print) to -> [((), 310 (#Print) (success))]
310 (#Print) (success)

#PullID
65 (#PullID) to -> [((), 66 (#PullID) (success))]
66 (#PullID) (success)

#PushAddOp
260 (#PushAddOp) to -> [((), 261 (#PushAddOp) (success))]
261 (#PushAddOp) (success)

#PushID
15 (#PushID) to -> [((), 16 (#PushID) (success))]
16 (#PushID) (success)

#PushNum
299 (#PushNum) to -> [((), 300 (#PushNum) (success))]
300 (#PushNum) (success)

#PushRelOp
229 (#PushRelOp) to -> [((), 230 (#PushRelOp) (success))]
230 (#PushRelOp) (success)

#PushSubOp
264 (#PushSubOp) to -> [((), 265 (#PushSubOp) (success))]
265 (#PushSubOp) (success)

#RelOp
231 (#RelOp) to -> [((), 232 (#RelOp) (success))]
232 (#RelOp) (success)

#Switch
169 (#Switch) to -> [((), 170 (#Switch) (success))]
170 (#Switch) (success)

#SwitchSave
167 (#SwitchSave) to -> [((), 168 (#SwitchSave) (success))]
168 (#SwitchSave) (success)

#While
146 (#While) to -> [((), 147 (#While) (success))]
147 (#While) (success)

#WhileLabel
142 (#WhileLabel) to -> [((), 143 (#WhileLabel) (success))]
143 (#WhileLabel) (success)

#WhileSave
144 (#WhileSave) to -> [((), 145 (#WhileSave) (success))]
145 (#WhileSave) (success)

additive-expression
245 (additive-expression) to -> [(term, 246 (additive-expression))]
246 (additive-expression) to -> [(additive-expression-prime, 247 (additive-expression) (success))]
247 (additive-expression) (success)

additive-expression-prime
251 (additive-expression-prime) to -> [(#PushAddOp, 252 (additive-expression-prime)), (#PushSubOp, 256 (additive-expression-prime)), ((), 259 (additive-expression-prime) (success))]
252 (additive-expression-prime) to -> [(+, 253 (additive-expression-prime))]
256 (additive-expression-prime) to -> [(-, 257 (additive-expression-prime))]
259 (additive-expression-prime) (success)
253 (additive-expression-prime) to -> [(addop-relop-rest, 254 (additive-expression-prime))]
257 (additive-expression-prime) to -> [(minus-expr, 258 (additive-expression-prime) (success))]
254 (additive-expression-prime) to -> [(#AddOp, 255 (additive-expression-prime) (success))]
258 (additive-expression-prime) (success)
255 (additive-expression-prime) (success)

addop-relop-rest
233 (addop-relop-rest) to -> [(additive-expression, 234 (addop-relop-rest) (success)), (#PushID, 235 (addop-relop-rest))]
234 (addop-relop-rest) (success)
235 (addop-relop-rest) to -> [(ID, 236 (addop-relop-rest))]
236 (addop-relop-rest) to -> [(addop-relop-rest-reference, 237 (addop-relop-rest) (success))]
237 (addop-relop-rest) (success)

addop-relop-rest-reference
238 (addop-relop-rest-reference) to -> [(id-additive-expression, 239 (addop-relop-rest-reference) (success)), ([, 240 (addop-relop-rest-reference))]
239 (addop-relop-rest-reference) (success)
240 (addop-relop-rest-reference) to -> [(expression, 241 (addop-relop-rest-reference))]
241 (addop-relop-rest-reference) to -> [(], 242 (addop-relop-rest-reference))]
242 (addop-relop-rest-reference) to -> [(#ArrayAccess, 243 (addop-relop-rest-reference))]
243 (addop-relop-rest-reference) to -> [(id-additive-expression, 244 (addop-relop-rest-reference) (success))]
244 (addop-relop-rest-reference) (success)

arg-list
314 (arg-list) to -> [(expression, 315 (arg-list))]
315 (arg-list) to -> [(arg-list-prime, 316 (arg-list) (success))]
316 (arg-list) (success)

arg-list-prime
317 (arg-list-prime) to -> [(,, 318 (arg-list-prime)), ((), 321 (arg-list-prime) (success))]
318 (arg-list-prime) to -> [(expression, 319 (arg-list-prime))]
321 (arg-list-prime) (success)
319 (arg-list-prime) to -> [(arg-list-prime, 320 (arg-list-prime) (success))]
320 (arg-list-prime) (success)

args
311 (args) to -> [(arg-list, 312 (args) (success)), ((), 313 (args) (success))]
312 (args) (success)
313 (args) (success)

bracket-id-expression
207 (bracket-id-expression) to -> [(=, 208 (bracket-id-expression)), (#ArrayAccess, 211 (bracket-id-expression))]
208 (bracket-id-expression) to -> [(expression, 209 (bracket-id-expression))]
211 (bracket-id-expression) to -> [(id-simple-expression, 212 (bracket-id-expression) (success))]
209 (bracket-id-expression) to -> [(#AssignArray, 210 (bracket-id-expression) (success))]
212 (bracket-id-expression) (success)
210 (bracket-id-expression) (success)

call
304 (call) to -> [((, 305 (call))]
305 (call) to -> [(args, 306 (call))]
306 (call) to -> [(), 307 (call))]
307 (call) to -> [(#Print, 308 (call) (success))]
308 (call) (success)

case-stmt
175 (case-stmt) to -> [(case, 176 (case-stmt))]
176 (case-stmt) to -> [(#CaseInsert, 177 (case-stmt))]
177 (case-stmt) to -> [(NUM, 178 (case-stmt))]
178 (case-stmt) to -> [(:, 179 (case-stmt))]
179 (case-stmt) to -> [(statement-list, 180 (case-stmt) (success))]
180 (case-stmt) (success)

case-stmts
171 (case-stmts) to -> [(case-stmt, 172 (case-stmts)), ((), 174 (case-stmts) (success))]
172 (case-stmts) to -> [(case-stmts, 173 (case-stmts) (success))]
174 (case-stmts) (success)
173 (case-stmts) (success)

compound-stmt
81 (compound-stmt) to -> [({, 82 (compound-stmt))]
82 (compound-stmt) to -> [(#IncreaseScope, 83 (compound-stmt))]
83 (compound-stmt) to -> [(declaration-list, 84 (compound-stmt))]
84 (compound-stmt) to -> [(statement-list, 85 (compound-stmt))]
85 (compound-stmt) to -> [(#DecreaseScope, 86 (compound-stmt))]
86 (compound-stmt) to -> [(}, 87 (compound-stmt) (success))]
87 (compound-stmt) (success)

declaration
19 (declaration) to -> [(var-declaration, 20 (declaration) (success)), (fun-declaration, 21 (declaration) (success))]
20 (declaration) (success)
21 (declaration) (success)

declaration-list
7 (declaration-list) to -> [(type-specifier, 8 (declaration-list)), ((), 14 (declaration-list) (success))]
8 (declaration-list) to -> [(#PushID, 9 (declaration-list))]
14 (declaration-list) (success)
9 (declaration-list) to -> [(ID, 10 (declaration-list))]
10 (declaration-list) to -> [(declaration, 11 (declaration-list))]
11 (declaration-list) to -> [(#PopID, 12 (declaration-list))]
12 (declaration-list) to -> [(declaration-list, 13 (declaration-list) (success))]
13 (declaration-list) (success)

default-stmt
183 (default-stmt) to -> [(default, 184 (default-stmt)), ((), 188 (default-stmt) (success))]
184 (default-stmt) to -> [(#DefaultInsert, 185 (default-stmt))]
188 (default-stmt) (success)
185 (default-stmt) to -> [(:, 186 (default-stmt))]
186 (default-stmt) to -> [(statement-list, 187 (default-stmt) (success))]
187 (default-stmt) (success)

expression
191 (expression) to -> [(simple-expression, 192 (expression) (success)), (#PushID, 193 (expression))]
192 (expression) (success)
193 (expression) to -> [(ID, 194 (expression))]
194 (expression) to -> [(id-expression, 195 (expression) (success))]
195 (expression) (success)

expression-stmt
101 (expression-stmt) to -> [(expression, 102 (expression-stmt)), (continue, 105 (expression-stmt)), (break, 108 (expression-stmt)), (;, 111 (expression-stmt) (success))]
102 (expression-stmt) to -> [(;, 103 (expression-stmt))]
105 (expression-stmt) to -> [(;, 106 (expression-stmt))]
108 (expression-stmt) to -> [(;, 109 (expression-stmt))]
111 (expression-stmt) (success)
103 (expression-stmt) to -> [(#PopID, 104 (expression-stmt) (success))]
106 (expression-stmt) to -> [(#Continue, 107 (expression-stmt) (success))]
109 (expression-stmt) to -> [(#Break, 110 (expression-stmt) (success))]
104 (expression-stmt) (success)
107 (expression-stmt) (success)
110 (expression-stmt) (success)

factor
293 (factor) to -> [((, 294 (factor)), (#PushNum, 297 (factor))]
294 (factor) to -> [(expression, 295 (factor))]
297 (factor) to -> [(NUM, 298 (factor) (success))]
295 (factor) to -> [(), 296 (factor) (success))]
298 (factor) (success)
296 (factor) (success)

fun-compound-stmt
322 (fun-compound-stmt) to -> [({, 323 (fun-compound-stmt))]
323 (fun-compound-stmt) to -> [(declaration-list, 324 (fun-compound-stmt))]
324 (fun-compound-stmt) to -> [(statement-list, 325 (fun-compound-stmt))]
325 (fun-compound-stmt) to -> [(#DecreaseScope, 326 (fun-compound-stmt))]
326 (fun-compound-stmt) to -> [(}, 327 (fun-compound-stmt) (success))]
327 (fun-compound-stmt) (success)

fun-declaration
34 (fun-declaration) to -> [((, 35 (fun-declaration))]
35 (fun-declaration) to -> [(#IncreaseScope, 36 (fun-declaration))]
36 (fun-declaration) to -> [(params, 37 (fun-declaration))]
37 (fun-declaration) to -> [(), 38 (fun-declaration))]
38 (fun-declaration) to -> [(#FunctionSave, 39 (fun-declaration))]
39 (fun-declaration) to -> [(fun-compound-stmt, 40 (fun-declaration))]
40 (fun-declaration) to -> [(#Function, 41 (fun-declaration) (success))]
41 (fun-declaration) (success)

id-additive-expression
248 (id-additive-expression) to -> [(id-term, 249 (id-additive-expression))]
249 (id-additive-expression) to -> [(additive-expression-prime, 250 (id-additive-expression) (success))]
250 (id-additive-expression) (success)

id-expression
196 (id-expression) to -> [(=, 197 (id-expression)), (id-simple-expression, 200 (id-expression) (success)), ([, 201 (id-expression))]
197 (id-expression) to -> [(expression, 198 (id-expression))]
200 (id-expression) (success)
201 (id-expression) to -> [(expression, 202 (id-expression))]
198 (id-expression) to -> [(#Assign, 199 (id-expression) (success))]
202 (id-expression) to -> [(], 203 (id-expression))]
199 (id-expression) (success)
203 (id-expression) to -> [(bracket-id-expression, 204 (id-expression) (success))]
204 (id-expression) (success)

id-simple-expression
220 (id-simple-expression) to -> [(id-additive-expression, 221 (id-simple-expression))]
221 (id-simple-expression) to -> [(rest-of-simple-expression, 222 (id-simple-expression) (success))]
222 (id-simple-expression) (success)

id-term
278 (id-term) to -> [(reference, 279 (id-term))]
279 (id-term) to -> [(term-prime, 280 (id-term) (success))]
280 (id-term) (success)

int-starting-param-list
59 (int-starting-param-list) to -> [(int, 60 (int-starting-param-list))]
60 (int-starting-param-list) to -> [(#PullID, 61 (int-starting-param-list))]
61 (int-starting-param-list) to -> [(ID, 62 (int-starting-param-list))]
62 (int-starting-param-list) to -> [(rest-of-param, 63 (int-starting-param-list))]
63 (int-starting-param-list) to -> [(param-list-prime, 64 (int-starting-param-list) (success))]
64 (int-starting-param-list) (success)

iteration-stmt
133 (iteration-stmt) to -> [(while, 134 (iteration-stmt))]
134 (iteration-stmt) to -> [(#WhileLabel, 135 (iteration-stmt))]
135 (iteration-stmt) to -> [((, 136 (iteration-stmt))]
136 (iteration-stmt) to -> [(expression, 137 (iteration-stmt))]
137 (iteration-stmt) to -> [(), 138 (iteration-stmt))]
138 (iteration-stmt) to -> [(#WhileSave, 139 (iteration-stmt))]
139 (iteration-stmt) to -> [(statement, 140 (iteration-stmt))]
140 (iteration-stmt) to -> [(#While, 141 (iteration-stmt) (success))]
141 (iteration-stmt) (success)

minus-expr
266 (minus-expr) to -> [(term, 267 (minus-expr)), (#PushID, 270 (minus-expr))]
267 (minus-expr) to -> [(#AddOp, 268 (minus-expr))]
270 (minus-expr) to -> [(ID, 271 (minus-expr))]
268 (minus-expr) to -> [(additive-expression-prime, 269 (minus-expr) (success))]
271 (minus-expr) to -> [(id-term, 272 (minus-expr))]
269 (minus-expr) (success)
272 (minus-expr) to -> [(#AddOp, 273 (minus-expr))]
273 (minus-expr) to -> [(additive-expression-prime, 274 (minus-expr) (success))]
274 (minus-expr) (success)

mult-rest
288 (mult-rest) to -> [(term, 289 (mult-rest) (success)), (#PushID, 290 (mult-rest))]
289 (mult-rest) (success)
290 (mult-rest) to -> [(ID, 291 (mult-rest))]
291 (mult-rest) to -> [(id-term, 292 (mult-rest) (success))]
292 (mult-rest) (success)

param
72 (param) to -> [(type-specifier, 73 (param))]
73 (param) to -> [(#PullID, 74 (param))]
74 (param) to -> [(ID, 75 (param))]
75 (param) to -> [(rest-of-param, 76 (param) (success))]
76 (param) (success)

param-list-prime
67 (param-list-prime) to -> [(,, 68 (param-list-prime)), ((), 71 (param-list-prime) (success))]
68 (param-list-prime) to -> [(param, 69 (param-list-prime))]
71 (param-list-prime) (success)
69 (param-list-prime) to -> [(param-list-prime, 70 (param-list-prime) (success))]
70 (param-list-prime) (success)

params
48 (params) to -> [(int-starting-param-list, 49 (params) (success)), (void-starting-param-list, 50 (params) (success))]
49 (params) (success)
50 (params) (success)

program
1 (program) to -> [(declaration-list, 2 (program))]
2 (program) to -> [(#CallMain, 3 (program))]
3 (program) to -> [(EOF, 4 (program) (success))]
4 (program) (success)

reference
301 (reference) to -> [(call, 302 (reference) (success)), ((), 303 (reference) (success))]
302 (reference) (success)
303 (reference) (success)

rest-of-param
77 (rest-of-param) to -> [((), 78 (rest-of-param) (success)), ([, 79 (rest-of-param))]
78 (rest-of-param) (success)
79 (rest-of-param) to -> [(], 80 (rest-of-param) (success))]
80 (rest-of-param) (success)

rest-of-return-stmt
152 (rest-of-return-stmt) to -> [(;, 153 (rest-of-return-stmt) (success)), (expression, 154 (rest-of-return-stmt))]
153 (rest-of-return-stmt) (success)
154 (rest-of-return-stmt) to -> [(;, 155 (rest-of-return-stmt) (success))]
155 (rest-of-return-stmt) (success)

rest-of-simple-expression
223 (rest-of-simple-expression) to -> [(#PushRelOp, 224 (rest-of-simple-expression)), ((), 228 (rest-of-simple-expression) (success))]
224 (rest-of-simple-expression) to -> [(RELOP, 225 (rest-of-simple-expression))]
228 (rest-of-simple-expression) (success)
225 (rest-of-simple-expression) to -> [(addop-relop-rest, 226 (rest-of-simple-expression))]
226 (rest-of-simple-expression) to -> [(#RelOp, 227 (rest-of-simple-expression) (success))]
227 (rest-of-simple-expression) (success)

rest-of-void-starting-param-list
54 (rest-of-void-starting-param-list) to -> [(ID, 55 (rest-of-void-starting-param-list)), ((), 58 (rest-of-void-starting-param-list) (success))]
55 (rest-of-void-starting-param-list) to -> [(rest-of-param, 56 (rest-of-void-starting-param-list))]
58 (rest-of-void-starting-param-list) (success)
56 (rest-of-void-starting-param-list) to -> [(param-list-prime, 57 (rest-of-void-starting-param-list) (success))]
57 (rest-of-void-starting-param-list) (success)

return-stmt
148 (return-stmt) to -> [(return, 149 (return-stmt))]
149 (return-stmt) to -> [(rest-of-return-stmt, 150 (return-stmt))]
150 (return-stmt) to -> [(#Function, 151 (return-stmt) (success))]
151 (return-stmt) (success)

selection-stmt
116 (selection-stmt) to -> [(if, 117 (selection-stmt))]
117 (selection-stmt) to -> [((, 118 (selection-stmt))]
118 (selection-stmt) to -> [(expression, 119 (selection-stmt))]
119 (selection-stmt) to -> [(), 120 (selection-stmt))]
120 (selection-stmt) to -> [(#IfSave, 121 (selection-stmt))]
121 (selection-stmt) to -> [(statement, 122 (selection-stmt))]
122 (selection-stmt) to -> [(#IfJumpSave, 123 (selection-stmt))]
123 (selection-stmt) to -> [(else, 124 (selection-stmt))]
124 (selection-stmt) to -> [(statement, 125 (selection-stmt))]
125 (selection-stmt) to -> [(#IfJump, 126 (selection-stmt) (success))]
126 (selection-stmt) (success)

simple-expression
217 (simple-expression) to -> [(additive-expression, 218 (simple-expression))]
218 (simple-expression) to -> [(rest-of-simple-expression, 219 (simple-expression) (success))]
219 (simple-expression) (success)

statement
94 (statement) to -> [(expression-stmt, 95 (statement) (success)), (compound-stmt, 96 (statement) (success)), (selection-stmt, 97 (statement) (success)), (iteration-stmt, 98 (statement) (success)), (return-stmt, 99 (statement) (success)), (switch-stmt, 100 (statement) (success))]
95 (statement) (success)
96 (statement) (success)
97 (statement) (success)
98 (statement) (success)
99 (statement) (success)
100 (statement) (success)

statement-list
90 (statement-list) to -> [(statement, 91 (statement-list)), ((), 93 (statement-list) (success))]
91 (statement-list) to -> [(statement-list, 92 (statement-list) (success))]
93 (statement-list) (success)
92 (statement-list) (success)

switch-stmt
156 (switch-stmt) to -> [(switch, 157 (switch-stmt))]
157 (switch-stmt) to -> [(#SwitchSave, 158 (switch-stmt))]
158 (switch-stmt) to -> [((, 159 (switch-stmt))]
159 (switch-stmt) to -> [(expression, 160 (switch-stmt))]
160 (switch-stmt) to -> [(), 161 (switch-stmt))]
161 (switch-stmt) to -> [({, 162 (switch-stmt))]
162 (switch-stmt) to -> [(case-stmts, 163 (switch-stmt))]
163 (switch-stmt) to -> [(default-stmt, 164 (switch-stmt))]
164 (switch-stmt) to -> [(}, 165 (switch-stmt))]
165 (switch-stmt) to -> [(#Switch, 166 (switch-stmt) (success))]
166 (switch-stmt) (success)

term
275 (term) to -> [(factor, 276 (term))]
276 (term) to -> [(term-prime, 277 (term) (success))]
277 (term) (success)

term-prime
281 (term-prime) to -> [(*, 282 (term-prime)), ((), 285 (term-prime) (success))]
282 (term-prime) to -> [(mult-rest, 283 (term-prime))]
285 (term-prime) (success)
283 (term-prime) to -> [(#MultOp, 284 (term-prime) (success))]
284 (term-prime) (success)

type-specifier
31 (type-specifier) to -> [(int, 32 (type-specifier) (success)), (void, 33 (type-specifier) (success))]
32 (type-specifier) (success)
33 (type-specifier) (success)

var-declaration
22 (var-declaration) to -> [(;, 23 (var-declaration) (success)), ([, 24 (var-declaration))]
23 (var-declaration) (success)
24 (var-declaration) to -> [(#ArrayDefinition, 25 (var-declaration))]
25 (var-declaration) to -> [(NUM, 26 (var-declaration))]
26 (var-declaration) to -> [(], 27 (var-declaration))]
27 (var-declaration) to -> [(;, 28 (var-declaration) (success))]
28 (var-declaration) (success)

void-starting-param-list
51 (void-starting-param-list) to -> [(void, 52 (void-starting-param-list))]
52 (void-starting-param-list) to -> [(rest-of-void-starting-param-list, 53 (void-starting-param-list) (success))]
53 (void-starting-param-list) (success)
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
|#CallMain|ε|EOF|
|#CaseInsert|ε|NUM|
|#Continue|ε|( ; ID NUM break case continue default else if return switch while { }|
|#DecreaseScope|ε|}|
|#DefaultInsert|ε|:|
|#Function|ε|( ; EOF ID NUM break case continue default else if int return switch void while { }|
|#FunctionSave|ε|{|
|#IfJump|ε|( ; ID NUM break case continue default else if return switch while { }|
|#IfJumpSave|ε|else|
|#IfSave|ε|( ; ID NUM break continue if return switch while {|
|#IncreaseScope|ε|( ; ID NUM break continue if int return switch void while { }|
|#MultOp|ε|) + , - ; RELOP ]|
|#PopID|ε|( ; EOF ID NUM break case continue default else if int return switch void while { }|
|#Print|ε|) * + , - ; RELOP ]|
|#PullID|ε|ID|
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
|compound-stmt|{|( ; ID NUM break case continue default else if return switch while { }|
|declaration|( ; [|( ; EOF ID NUM break continue if int return switch void while { }|
|declaration-list|int void ε|( ; EOF ID NUM break continue if return switch while { }|
|default-stmt|default ε|}|
|expression|( ID NUM|) , ; ]|
|expression-stmt|( ; ID NUM break continue|( ; ID NUM break case continue default else if return switch while { }|
|factor|( NUM|) * + , - ; RELOP ]|
|fun-compound-stmt|{|( ; EOF ID NUM break continue if int return switch void while { }|
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

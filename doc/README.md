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
1. program → #DefinePrint declaration-list #CallMain EOF
2. declaration-list → type-specifier #PushID ID declaration #PopID declaration-list | ε
3. declaration → var-declaration | fun-declaration
4. var-declaration → #VarDefinition ; | [ #ArrayDefinition NUM ] ;
5. type-specifier → int | void
6. fun-declaration → #FunctionSave ( #IncreaseScope params ) fun-compound-stmt
7. params → int-starting-param-list | void-starting-param-list
8. void-starting-param-list → void rest-of-void-starting-param-list
9. rest-of-void-starting-param-list → #NewParam ID rest-of-param param-list-prime | ε
10. int-starting-param-list → int #PullID #NewParam ID rest-of-param param-list-prime
11. param-list-prime → , param param-list-prime | ε
12. param → type-specifier #PullID #NewParam ID rest-of-param
13. rest-of-param → ε | [ #ArrayParam ]
14. compound-stmt → { #IncreaseScope declaration-list statement-list #DecreaseScope }
15. statement-list → statement statement-list | ε
16. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt | switch-stmt
17. expression-stmt → expression ; #PopID  | continue ; #Continue | break ; #Break | ;
18. selection-stmt → if ( expression ) #IfSave statement #IfJumpSave else statement #IfJump
19. iteration-stmt → while #WhileLabel ( expression ) #WhileSave statement #While
20. return-stmt → return rest-of-return-stmt #FunctionReturn
21. rest-of-return-stmt → #NoReturn ; | expression #PushReturnValue ;
22. switch-stmt → switch #SwitchPushTest ( expression ) { case-stmts default-stmt } #SwitchPop
23. case-stmts → case-stmt case-stmts | ε
24. case-stmt → case #SwitchTest NUM : #SwitchSave statement-list #SwitchPatchJumpOnNotTest
25. default-stmt → default : #SwitchSave statement-list #SwitchPatchJumpOnTest | ε
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
44. call → #CallBefore ( args ) #Call
45. args → arg-list | ε
46. arg-list → expression arg-list-prime #PushParameter
47. arg-list-prime → , expression arg-list-prime #PushParameter | ε
48. fun-compound-stmt → { declaration-list statement-list #Function #DecreaseScope }
```
## State Diagram
```

#AddOp
288 (#AddOp) to -> [((), 289 (#AddOp) (success))]
289 (#AddOp) (success)

#ArrayAccess
241 (#ArrayAccess) to -> [((), 242 (#ArrayAccess) (success))]
242 (#ArrayAccess) (success)

#ArrayDefinition
35 (#ArrayDefinition) to -> [((), 36 (#ArrayDefinition) (success))]
36 (#ArrayDefinition) (success)

#ArrayParam
90 (#ArrayParam) to -> [((), 91 (#ArrayParam) (success))]
91 (#ArrayParam) (success)

#Assign
231 (#Assign) to -> [((), 232 (#Assign) (success))]
232 (#Assign) (success)

#AssignArray
239 (#AssignArray) to -> [((), 240 (#AssignArray) (success))]
240 (#AssignArray) (success)

#Break
125 (#Break) to -> [((), 126 (#Break) (success))]
126 (#Break) (success)

#Call
338 (#Call) to -> [((), 339 (#Call) (success))]
339 (#Call) (success)

#CallBefore
336 (#CallBefore) to -> [((), 337 (#CallBefore) (success))]
337 (#CallBefore) (success)

#CallMain
8 (#CallMain) to -> [((), 9 (#CallMain) (success))]
9 (#CallMain) (success)

#Continue
123 (#Continue) to -> [((), 124 (#Continue) (success))]
124 (#Continue) (success)

#DecreaseScope
99 (#DecreaseScope) to -> [((), 100 (#DecreaseScope) (success))]
100 (#DecreaseScope) (success)

#DefinePrint
6 (#DefinePrint) to -> [((), 7 (#DefinePrint) (success))]
7 (#DefinePrint) (success)

#Function
362 (#Function) to -> [((), 363 (#Function) (success))]
363 (#Function) (success)

#FunctionReturn
163 (#FunctionReturn) to -> [((), 164 (#FunctionReturn) (success))]
164 (#FunctionReturn) (success)

#FunctionSave
47 (#FunctionSave) to -> [((), 48 (#FunctionSave) (success))]
48 (#FunctionSave) (success)

#IfJump
142 (#IfJump) to -> [((), 143 (#IfJump) (success))]
143 (#IfJump) (success)

#IfJumpSave
140 (#IfJumpSave) to -> [((), 141 (#IfJumpSave) (success))]
141 (#IfJumpSave) (success)

#IfSave
138 (#IfSave) to -> [((), 139 (#IfSave) (success))]
139 (#IfSave) (success)

#IncreaseScope
49 (#IncreaseScope) to -> [((), 50 (#IncreaseScope) (success))]
50 (#IncreaseScope) (success)

#MultOp
312 (#MultOp) to -> [((), 313 (#MultOp) (success))]
313 (#MultOp) (success)

#NewParam
63 (#NewParam) to -> [((), 64 (#NewParam) (success))]
64 (#NewParam) (success)

#NoReturn
171 (#NoReturn) to -> [((), 172 (#NoReturn) (success))]
172 (#NoReturn) (success)

#PopID
20 (#PopID) to -> [((), 21 (#PopID) (success))]
21 (#PopID) (success)

#PullID
72 (#PullID) to -> [((), 73 (#PullID) (success))]
73 (#PullID) (success)

#PushAddOp
286 (#PushAddOp) to -> [((), 287 (#PushAddOp) (success))]
287 (#PushAddOp) (success)

#PushID
18 (#PushID) to -> [((), 19 (#PushID) (success))]
19 (#PushID) (success)

#PushNum
325 (#PushNum) to -> [((), 326 (#PushNum) (success))]
326 (#PushNum) (success)

#PushParameter
347 (#PushParameter) to -> [((), 348 (#PushParameter) (success))]
348 (#PushParameter) (success)

#PushRelOp
255 (#PushRelOp) to -> [((), 256 (#PushRelOp) (success))]
256 (#PushRelOp) (success)

#PushReturnValue
173 (#PushReturnValue) to -> [((), 174 (#PushReturnValue) (success))]
174 (#PushReturnValue) (success)

#PushSubOp
290 (#PushSubOp) to -> [((), 291 (#PushSubOp) (success))]
291 (#PushSubOp) (success)

#RelOp
257 (#RelOp) to -> [((), 258 (#RelOp) (success))]
258 (#RelOp) (success)

#SwitchPatchJumpOnNotTest
206 (#SwitchPatchJumpOnNotTest) to -> [((), 207 (#SwitchPatchJumpOnNotTest) (success))]
207 (#SwitchPatchJumpOnNotTest) (success)

#SwitchPatchJumpOnTest
215 (#SwitchPatchJumpOnTest) to -> [((), 216 (#SwitchPatchJumpOnTest) (success))]
216 (#SwitchPatchJumpOnTest) (success)

#SwitchPop
188 (#SwitchPop) to -> [((), 189 (#SwitchPop) (success))]
189 (#SwitchPop) (success)

#SwitchPushTest
186 (#SwitchPushTest) to -> [((), 187 (#SwitchPushTest) (success))]
187 (#SwitchPushTest) (success)

#SwitchSave
204 (#SwitchSave) to -> [((), 205 (#SwitchSave) (success))]
205 (#SwitchSave) (success)

#SwitchTest
202 (#SwitchTest) to -> [((), 203 (#SwitchTest) (success))]
203 (#SwitchTest) (success)

#VarDefinition
33 (#VarDefinition) to -> [((), 34 (#VarDefinition) (success))]
34 (#VarDefinition) (success)

#While
157 (#While) to -> [((), 158 (#While) (success))]
158 (#While) (success)

#WhileLabel
153 (#WhileLabel) to -> [((), 154 (#WhileLabel) (success))]
154 (#WhileLabel) (success)

#WhileSave
155 (#WhileSave) to -> [((), 156 (#WhileSave) (success))]
156 (#WhileSave) (success)

additive-expression
271 (additive-expression) to -> [(term, 272 (additive-expression))]
272 (additive-expression) to -> [(additive-expression-prime, 273 (additive-expression) (success))]
273 (additive-expression) (success)

additive-expression-prime
277 (additive-expression-prime) to -> [(#PushAddOp, 278 (additive-expression-prime)), (#PushSubOp, 282 (additive-expression-prime)), ((), 285 (additive-expression-prime) (success))]
278 (additive-expression-prime) to -> [(+, 279 (additive-expression-prime))]
282 (additive-expression-prime) to -> [(-, 283 (additive-expression-prime))]
285 (additive-expression-prime) (success)
279 (additive-expression-prime) to -> [(addop-relop-rest, 280 (additive-expression-prime))]
283 (additive-expression-prime) to -> [(minus-expr, 284 (additive-expression-prime) (success))]
280 (additive-expression-prime) to -> [(#AddOp, 281 (additive-expression-prime) (success))]
284 (additive-expression-prime) (success)
281 (additive-expression-prime) (success)

addop-relop-rest
259 (addop-relop-rest) to -> [(additive-expression, 260 (addop-relop-rest) (success)), (#PushID, 261 (addop-relop-rest))]
260 (addop-relop-rest) (success)
261 (addop-relop-rest) to -> [(ID, 262 (addop-relop-rest))]
262 (addop-relop-rest) to -> [(addop-relop-rest-reference, 263 (addop-relop-rest) (success))]
263 (addop-relop-rest) (success)

addop-relop-rest-reference
264 (addop-relop-rest-reference) to -> [(id-additive-expression, 265 (addop-relop-rest-reference) (success)), ([, 266 (addop-relop-rest-reference))]
265 (addop-relop-rest-reference) (success)
266 (addop-relop-rest-reference) to -> [(expression, 267 (addop-relop-rest-reference))]
267 (addop-relop-rest-reference) to -> [(], 268 (addop-relop-rest-reference))]
268 (addop-relop-rest-reference) to -> [(#ArrayAccess, 269 (addop-relop-rest-reference))]
269 (addop-relop-rest-reference) to -> [(id-additive-expression, 270 (addop-relop-rest-reference) (success))]
270 (addop-relop-rest-reference) (success)

arg-list
343 (arg-list) to -> [(expression, 344 (arg-list))]
344 (arg-list) to -> [(arg-list-prime, 345 (arg-list))]
345 (arg-list) to -> [(#PushParameter, 346 (arg-list) (success))]
346 (arg-list) (success)

arg-list-prime
349 (arg-list-prime) to -> [(,, 350 (arg-list-prime)), ((), 354 (arg-list-prime) (success))]
350 (arg-list-prime) to -> [(expression, 351 (arg-list-prime))]
354 (arg-list-prime) (success)
351 (arg-list-prime) to -> [(arg-list-prime, 352 (arg-list-prime))]
352 (arg-list-prime) to -> [(#PushParameter, 353 (arg-list-prime) (success))]
353 (arg-list-prime) (success)

args
340 (args) to -> [(arg-list, 341 (args) (success)), ((), 342 (args) (success))]
341 (args) (success)
342 (args) (success)

bracket-id-expression
233 (bracket-id-expression) to -> [(=, 234 (bracket-id-expression)), (#ArrayAccess, 237 (bracket-id-expression))]
234 (bracket-id-expression) to -> [(expression, 235 (bracket-id-expression))]
237 (bracket-id-expression) to -> [(id-simple-expression, 238 (bracket-id-expression) (success))]
235 (bracket-id-expression) to -> [(#AssignArray, 236 (bracket-id-expression) (success))]
238 (bracket-id-expression) (success)
236 (bracket-id-expression) (success)

call
330 (call) to -> [(#CallBefore, 331 (call))]
331 (call) to -> [((, 332 (call))]
332 (call) to -> [(args, 333 (call))]
333 (call) to -> [(), 334 (call))]
334 (call) to -> [(#Call, 335 (call) (success))]
335 (call) (success)

case-stmt
194 (case-stmt) to -> [(case, 195 (case-stmt))]
195 (case-stmt) to -> [(#SwitchTest, 196 (case-stmt))]
196 (case-stmt) to -> [(NUM, 197 (case-stmt))]
197 (case-stmt) to -> [(:, 198 (case-stmt))]
198 (case-stmt) to -> [(#SwitchSave, 199 (case-stmt))]
199 (case-stmt) to -> [(statement-list, 200 (case-stmt))]
200 (case-stmt) to -> [(#SwitchPatchJumpOnNotTest, 201 (case-stmt) (success))]
201 (case-stmt) (success)

case-stmts
190 (case-stmts) to -> [(case-stmt, 191 (case-stmts)), ((), 193 (case-stmts) (success))]
191 (case-stmts) to -> [(case-stmts, 192 (case-stmts) (success))]
193 (case-stmts) (success)
192 (case-stmts) (success)

compound-stmt
92 (compound-stmt) to -> [({, 93 (compound-stmt))]
93 (compound-stmt) to -> [(#IncreaseScope, 94 (compound-stmt))]
94 (compound-stmt) to -> [(declaration-list, 95 (compound-stmt))]
95 (compound-stmt) to -> [(statement-list, 96 (compound-stmt))]
96 (compound-stmt) to -> [(#DecreaseScope, 97 (compound-stmt))]
97 (compound-stmt) to -> [(}, 98 (compound-stmt) (success))]
98 (compound-stmt) (success)

declaration
22 (declaration) to -> [(var-declaration, 23 (declaration) (success)), (fun-declaration, 24 (declaration) (success))]
23 (declaration) (success)
24 (declaration) (success)

declaration-list
10 (declaration-list) to -> [(type-specifier, 11 (declaration-list)), ((), 17 (declaration-list) (success))]
11 (declaration-list) to -> [(#PushID, 12 (declaration-list))]
17 (declaration-list) (success)
12 (declaration-list) to -> [(ID, 13 (declaration-list))]
13 (declaration-list) to -> [(declaration, 14 (declaration-list))]
14 (declaration-list) to -> [(#PopID, 15 (declaration-list))]
15 (declaration-list) to -> [(declaration-list, 16 (declaration-list) (success))]
16 (declaration-list) (success)

default-stmt
208 (default-stmt) to -> [(default, 209 (default-stmt)), ((), 214 (default-stmt) (success))]
209 (default-stmt) to -> [(:, 210 (default-stmt))]
214 (default-stmt) (success)
210 (default-stmt) to -> [(#SwitchSave, 211 (default-stmt))]
211 (default-stmt) to -> [(statement-list, 212 (default-stmt))]
212 (default-stmt) to -> [(#SwitchPatchJumpOnTest, 213 (default-stmt) (success))]
213 (default-stmt) (success)

expression
217 (expression) to -> [(simple-expression, 218 (expression) (success)), (#PushID, 219 (expression))]
218 (expression) (success)
219 (expression) to -> [(ID, 220 (expression))]
220 (expression) to -> [(id-expression, 221 (expression) (success))]
221 (expression) (success)

expression-stmt
112 (expression-stmt) to -> [(expression, 113 (expression-stmt)), (continue, 116 (expression-stmt)), (break, 119 (expression-stmt)), (;, 122 (expression-stmt) (success))]
113 (expression-stmt) to -> [(;, 114 (expression-stmt))]
116 (expression-stmt) to -> [(;, 117 (expression-stmt))]
119 (expression-stmt) to -> [(;, 120 (expression-stmt))]
122 (expression-stmt) (success)
114 (expression-stmt) to -> [(#PopID, 115 (expression-stmt) (success))]
117 (expression-stmt) to -> [(#Continue, 118 (expression-stmt) (success))]
120 (expression-stmt) to -> [(#Break, 121 (expression-stmt) (success))]
115 (expression-stmt) (success)
118 (expression-stmt) (success)
121 (expression-stmt) (success)

factor
319 (factor) to -> [((, 320 (factor)), (#PushNum, 323 (factor))]
320 (factor) to -> [(expression, 321 (factor))]
323 (factor) to -> [(NUM, 324 (factor) (success))]
321 (factor) to -> [(), 322 (factor) (success))]
324 (factor) (success)
322 (factor) (success)

fun-compound-stmt
355 (fun-compound-stmt) to -> [({, 356 (fun-compound-stmt))]
356 (fun-compound-stmt) to -> [(declaration-list, 357 (fun-compound-stmt))]
357 (fun-compound-stmt) to -> [(statement-list, 358 (fun-compound-stmt))]
358 (fun-compound-stmt) to -> [(#Function, 359 (fun-compound-stmt))]
359 (fun-compound-stmt) to -> [(#DecreaseScope, 360 (fun-compound-stmt))]
360 (fun-compound-stmt) to -> [(}, 361 (fun-compound-stmt) (success))]
361 (fun-compound-stmt) (success)

fun-declaration
40 (fun-declaration) to -> [(#FunctionSave, 41 (fun-declaration))]
41 (fun-declaration) to -> [((, 42 (fun-declaration))]
42 (fun-declaration) to -> [(#IncreaseScope, 43 (fun-declaration))]
43 (fun-declaration) to -> [(params, 44 (fun-declaration))]
44 (fun-declaration) to -> [(), 45 (fun-declaration))]
45 (fun-declaration) to -> [(fun-compound-stmt, 46 (fun-declaration) (success))]
46 (fun-declaration) (success)

id-additive-expression
274 (id-additive-expression) to -> [(id-term, 275 (id-additive-expression))]
275 (id-additive-expression) to -> [(additive-expression-prime, 276 (id-additive-expression) (success))]
276 (id-additive-expression) (success)

id-expression
222 (id-expression) to -> [(=, 223 (id-expression)), (id-simple-expression, 226 (id-expression) (success)), ([, 227 (id-expression))]
223 (id-expression) to -> [(expression, 224 (id-expression))]
226 (id-expression) (success)
227 (id-expression) to -> [(expression, 228 (id-expression))]
224 (id-expression) to -> [(#Assign, 225 (id-expression) (success))]
228 (id-expression) to -> [(], 229 (id-expression))]
225 (id-expression) (success)
229 (id-expression) to -> [(bracket-id-expression, 230 (id-expression) (success))]
230 (id-expression) (success)

id-simple-expression
246 (id-simple-expression) to -> [(id-additive-expression, 247 (id-simple-expression))]
247 (id-simple-expression) to -> [(rest-of-simple-expression, 248 (id-simple-expression) (success))]
248 (id-simple-expression) (success)

id-term
304 (id-term) to -> [(reference, 305 (id-term))]
305 (id-term) to -> [(term-prime, 306 (id-term) (success))]
306 (id-term) (success)

int-starting-param-list
65 (int-starting-param-list) to -> [(int, 66 (int-starting-param-list))]
66 (int-starting-param-list) to -> [(#PullID, 67 (int-starting-param-list))]
67 (int-starting-param-list) to -> [(#NewParam, 68 (int-starting-param-list))]
68 (int-starting-param-list) to -> [(ID, 69 (int-starting-param-list))]
69 (int-starting-param-list) to -> [(rest-of-param, 70 (int-starting-param-list))]
70 (int-starting-param-list) to -> [(param-list-prime, 71 (int-starting-param-list) (success))]
71 (int-starting-param-list) (success)

iteration-stmt
144 (iteration-stmt) to -> [(while, 145 (iteration-stmt))]
145 (iteration-stmt) to -> [(#WhileLabel, 146 (iteration-stmt))]
146 (iteration-stmt) to -> [((, 147 (iteration-stmt))]
147 (iteration-stmt) to -> [(expression, 148 (iteration-stmt))]
148 (iteration-stmt) to -> [(), 149 (iteration-stmt))]
149 (iteration-stmt) to -> [(#WhileSave, 150 (iteration-stmt))]
150 (iteration-stmt) to -> [(statement, 151 (iteration-stmt))]
151 (iteration-stmt) to -> [(#While, 152 (iteration-stmt) (success))]
152 (iteration-stmt) (success)

minus-expr
292 (minus-expr) to -> [(term, 293 (minus-expr)), (#PushID, 296 (minus-expr))]
293 (minus-expr) to -> [(#AddOp, 294 (minus-expr))]
296 (minus-expr) to -> [(ID, 297 (minus-expr))]
294 (minus-expr) to -> [(additive-expression-prime, 295 (minus-expr) (success))]
297 (minus-expr) to -> [(id-term, 298 (minus-expr))]
295 (minus-expr) (success)
298 (minus-expr) to -> [(#AddOp, 299 (minus-expr))]
299 (minus-expr) to -> [(additive-expression-prime, 300 (minus-expr) (success))]
300 (minus-expr) (success)

mult-rest
314 (mult-rest) to -> [(term, 315 (mult-rest) (success)), (#PushID, 316 (mult-rest))]
315 (mult-rest) (success)
316 (mult-rest) to -> [(ID, 317 (mult-rest))]
317 (mult-rest) to -> [(id-term, 318 (mult-rest) (success))]
318 (mult-rest) (success)

param
79 (param) to -> [(type-specifier, 80 (param))]
80 (param) to -> [(#PullID, 81 (param))]
81 (param) to -> [(#NewParam, 82 (param))]
82 (param) to -> [(ID, 83 (param))]
83 (param) to -> [(rest-of-param, 84 (param) (success))]
84 (param) (success)

param-list-prime
74 (param-list-prime) to -> [(,, 75 (param-list-prime)), ((), 78 (param-list-prime) (success))]
75 (param-list-prime) to -> [(param, 76 (param-list-prime))]
78 (param-list-prime) (success)
76 (param-list-prime) to -> [(param-list-prime, 77 (param-list-prime) (success))]
77 (param-list-prime) (success)

params
51 (params) to -> [(int-starting-param-list, 52 (params) (success)), (void-starting-param-list, 53 (params) (success))]
52 (params) (success)
53 (params) (success)

program
1 (program) to -> [(#DefinePrint, 2 (program))]
2 (program) to -> [(declaration-list, 3 (program))]
3 (program) to -> [(#CallMain, 4 (program))]
4 (program) to -> [(EOF, 5 (program) (success))]
5 (program) (success)

reference
327 (reference) to -> [(call, 328 (reference) (success)), ((), 329 (reference) (success))]
328 (reference) (success)
329 (reference) (success)

rest-of-param
85 (rest-of-param) to -> [((), 86 (rest-of-param) (success)), ([, 87 (rest-of-param))]
86 (rest-of-param) (success)
87 (rest-of-param) to -> [(#ArrayParam, 88 (rest-of-param))]
88 (rest-of-param) to -> [(], 89 (rest-of-param) (success))]
89 (rest-of-param) (success)

rest-of-return-stmt
165 (rest-of-return-stmt) to -> [(#NoReturn, 166 (rest-of-return-stmt)), (expression, 168 (rest-of-return-stmt))]
166 (rest-of-return-stmt) to -> [(;, 167 (rest-of-return-stmt) (success))]
168 (rest-of-return-stmt) to -> [(#PushReturnValue, 169 (rest-of-return-stmt))]
167 (rest-of-return-stmt) (success)
169 (rest-of-return-stmt) to -> [(;, 170 (rest-of-return-stmt) (success))]
170 (rest-of-return-stmt) (success)

rest-of-simple-expression
249 (rest-of-simple-expression) to -> [(#PushRelOp, 250 (rest-of-simple-expression)), ((), 254 (rest-of-simple-expression) (success))]
250 (rest-of-simple-expression) to -> [(RELOP, 251 (rest-of-simple-expression))]
254 (rest-of-simple-expression) (success)
251 (rest-of-simple-expression) to -> [(addop-relop-rest, 252 (rest-of-simple-expression))]
252 (rest-of-simple-expression) to -> [(#RelOp, 253 (rest-of-simple-expression) (success))]
253 (rest-of-simple-expression) (success)

rest-of-void-starting-param-list
57 (rest-of-void-starting-param-list) to -> [(#NewParam, 58 (rest-of-void-starting-param-list)), ((), 62 (rest-of-void-starting-param-list) (success))]
58 (rest-of-void-starting-param-list) to -> [(ID, 59 (rest-of-void-starting-param-list))]
62 (rest-of-void-starting-param-list) (success)
59 (rest-of-void-starting-param-list) to -> [(rest-of-param, 60 (rest-of-void-starting-param-list))]
60 (rest-of-void-starting-param-list) to -> [(param-list-prime, 61 (rest-of-void-starting-param-list) (success))]
61 (rest-of-void-starting-param-list) (success)

return-stmt
159 (return-stmt) to -> [(return, 160 (return-stmt))]
160 (return-stmt) to -> [(rest-of-return-stmt, 161 (return-stmt))]
161 (return-stmt) to -> [(#FunctionReturn, 162 (return-stmt) (success))]
162 (return-stmt) (success)

selection-stmt
127 (selection-stmt) to -> [(if, 128 (selection-stmt))]
128 (selection-stmt) to -> [((, 129 (selection-stmt))]
129 (selection-stmt) to -> [(expression, 130 (selection-stmt))]
130 (selection-stmt) to -> [(), 131 (selection-stmt))]
131 (selection-stmt) to -> [(#IfSave, 132 (selection-stmt))]
132 (selection-stmt) to -> [(statement, 133 (selection-stmt))]
133 (selection-stmt) to -> [(#IfJumpSave, 134 (selection-stmt))]
134 (selection-stmt) to -> [(else, 135 (selection-stmt))]
135 (selection-stmt) to -> [(statement, 136 (selection-stmt))]
136 (selection-stmt) to -> [(#IfJump, 137 (selection-stmt) (success))]
137 (selection-stmt) (success)

simple-expression
243 (simple-expression) to -> [(additive-expression, 244 (simple-expression))]
244 (simple-expression) to -> [(rest-of-simple-expression, 245 (simple-expression) (success))]
245 (simple-expression) (success)

statement
105 (statement) to -> [(expression-stmt, 106 (statement) (success)), (compound-stmt, 107 (statement) (success)), (selection-stmt, 108 (statement) (success)), (iteration-stmt, 109 (statement) (success)), (return-stmt, 110 (statement) (success)), (switch-stmt, 111 (statement) (success))]
106 (statement) (success)
107 (statement) (success)
108 (statement) (success)
109 (statement) (success)
110 (statement) (success)
111 (statement) (success)

statement-list
101 (statement-list) to -> [(statement, 102 (statement-list)), ((), 104 (statement-list) (success))]
102 (statement-list) to -> [(statement-list, 103 (statement-list) (success))]
104 (statement-list) (success)
103 (statement-list) (success)

switch-stmt
175 (switch-stmt) to -> [(switch, 176 (switch-stmt))]
176 (switch-stmt) to -> [(#SwitchPushTest, 177 (switch-stmt))]
177 (switch-stmt) to -> [((, 178 (switch-stmt))]
178 (switch-stmt) to -> [(expression, 179 (switch-stmt))]
179 (switch-stmt) to -> [(), 180 (switch-stmt))]
180 (switch-stmt) to -> [({, 181 (switch-stmt))]
181 (switch-stmt) to -> [(case-stmts, 182 (switch-stmt))]
182 (switch-stmt) to -> [(default-stmt, 183 (switch-stmt))]
183 (switch-stmt) to -> [(}, 184 (switch-stmt))]
184 (switch-stmt) to -> [(#SwitchPop, 185 (switch-stmt) (success))]
185 (switch-stmt) (success)

term
301 (term) to -> [(factor, 302 (term))]
302 (term) to -> [(term-prime, 303 (term) (success))]
303 (term) (success)

term-prime
307 (term-prime) to -> [(*, 308 (term-prime)), ((), 311 (term-prime) (success))]
308 (term-prime) to -> [(mult-rest, 309 (term-prime))]
311 (term-prime) (success)
309 (term-prime) to -> [(#MultOp, 310 (term-prime) (success))]
310 (term-prime) (success)

type-specifier
37 (type-specifier) to -> [(int, 38 (type-specifier) (success)), (void, 39 (type-specifier) (success))]
38 (type-specifier) (success)
39 (type-specifier) (success)

var-declaration
25 (var-declaration) to -> [(#VarDefinition, 26 (var-declaration)), ([, 28 (var-declaration))]
26 (var-declaration) to -> [(;, 27 (var-declaration) (success))]
28 (var-declaration) to -> [(#ArrayDefinition, 29 (var-declaration))]
27 (var-declaration) (success)
29 (var-declaration) to -> [(NUM, 30 (var-declaration))]
30 (var-declaration) to -> [(], 31 (var-declaration))]
31 (var-declaration) to -> [(;, 32 (var-declaration) (success))]
32 (var-declaration) (success)

void-starting-param-list
54 (void-starting-param-list) to -> [(void, 55 (void-starting-param-list))]
55 (void-starting-param-list) to -> [(rest-of-void-starting-param-list, 56 (void-starting-param-list) (success))]
56 (void-starting-param-list) (success)
```
## First and Follow
|Non-terminal|First|Follow|
|:----------:|:---:|:----:|
|#AddOp|ε|) + , - ; RELOP ]|
|#ArrayAccess|ε|( ) * + , - ; RELOP ]|
|#ArrayDefinition|ε|NUM|
|#ArrayParam|ε|]|
|#Assign|ε|) , ; ]|
|#AssignArray|ε|) , ; ]|
|#Break|ε|( ; ID NUM break case continue default else if return switch while { }|
|#Call|ε|) * + , - ; RELOP ]|
|#CallBefore|ε|(|
|#CallMain|ε|EOF|
|#Continue|ε|( ; ID NUM break case continue default else if return switch while { }|
|#DecreaseScope|ε|}|
|#DefinePrint|ε|EOF int void|
|#Function|ε|}|
|#FunctionReturn|ε|( ; ID NUM break case continue default else if return switch while { }|
|#FunctionSave|ε|(|
|#IfJump|ε|( ; ID NUM break case continue default else if return switch while { }|
|#IfJumpSave|ε|else|
|#IfSave|ε|( ; ID NUM break continue if return switch while {|
|#IncreaseScope|ε|( ; ID NUM break continue if int return switch void while { }|
|#MultOp|ε|) + , - ; RELOP ]|
|#NewParam|ε|ID|
|#NoReturn|ε|;|
|#PopID|ε|( ; EOF ID NUM break case continue default else if int return switch void while { }|
|#PullID|ε|ID|
|#PushAddOp|ε|+|
|#PushID|ε|ID|
|#PushNum|ε|NUM|
|#PushParameter|ε|)|
|#PushRelOp|ε|RELOP|
|#PushReturnValue|ε|;|
|#PushSubOp|ε|-|
|#RelOp|ε|) , ; ]|
|#SwitchPatchJumpOnNotTest|ε|case default }|
|#SwitchPatchJumpOnTest|ε|}|
|#SwitchPop|ε|( ; ID NUM break case continue default else if return switch while { }|
|#SwitchPushTest|ε|(|
|#SwitchSave|ε|( ; ID NUM break case continue default if return switch while { }|
|#SwitchTest|ε|NUM|
|#VarDefinition|ε|;|
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

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
20. return-stmt → return rest-of-return-stmt #FunctionReturn
21. rest-of-return-stmt → ; | expression #PushReturnValue ;
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
44. call → ( args ) #Call
45. args → arg-list | ε
46. arg-list → expression arg-list-prime #PushParameter
47. arg-list-prime → , expression arg-list-prime #PushParameter | ε
48. fun-compound-stmt → { declaration-list statement-list #Function #DecreaseScope }
```
## State Diagram
```

#AddOp
277 (#AddOp) to -> [((), 278 (#AddOp) (success))]
278 (#AddOp) (success)

#ArrayAccess
230 (#ArrayAccess) to -> [((), 231 (#ArrayAccess) (success))]
231 (#ArrayAccess) (success)

#ArrayDefinition
35 (#ArrayDefinition) to -> [((), 36 (#ArrayDefinition) (success))]
36 (#ArrayDefinition) (success)

#Assign
220 (#Assign) to -> [((), 221 (#Assign) (success))]
221 (#Assign) (success)

#AssignArray
228 (#AssignArray) to -> [((), 229 (#AssignArray) (success))]
229 (#AssignArray) (success)

#Break
117 (#Break) to -> [((), 118 (#Break) (success))]
118 (#Break) (success)

#Call
324 (#Call) to -> [((), 325 (#Call) (success))]
325 (#Call) (success)

#CallMain
8 (#CallMain) to -> [((), 9 (#CallMain) (success))]
9 (#CallMain) (success)

#Continue
115 (#Continue) to -> [((), 116 (#Continue) (success))]
116 (#Continue) (success)

#DecreaseScope
91 (#DecreaseScope) to -> [((), 92 (#DecreaseScope) (success))]
92 (#DecreaseScope) (success)

#DefinePrint
6 (#DefinePrint) to -> [((), 7 (#DefinePrint) (success))]
7 (#DefinePrint) (success)

#Function
348 (#Function) to -> [((), 349 (#Function) (success))]
349 (#Function) (success)

#FunctionReturn
155 (#FunctionReturn) to -> [((), 156 (#FunctionReturn) (success))]
156 (#FunctionReturn) (success)

#FunctionSave
47 (#FunctionSave) to -> [((), 48 (#FunctionSave) (success))]
48 (#FunctionSave) (success)

#IfJump
134 (#IfJump) to -> [((), 135 (#IfJump) (success))]
135 (#IfJump) (success)

#IfJumpSave
132 (#IfJumpSave) to -> [((), 133 (#IfJumpSave) (success))]
133 (#IfJumpSave) (success)

#IfSave
130 (#IfSave) to -> [((), 131 (#IfSave) (success))]
131 (#IfSave) (success)

#IncreaseScope
49 (#IncreaseScope) to -> [((), 50 (#IncreaseScope) (success))]
50 (#IncreaseScope) (success)

#MultOp
301 (#MultOp) to -> [((), 302 (#MultOp) (success))]
302 (#MultOp) (success)

#PopID
20 (#PopID) to -> [((), 21 (#PopID) (success))]
21 (#PopID) (success)

#PullID
68 (#PullID) to -> [((), 69 (#PullID) (success))]
69 (#PullID) (success)

#PushAddOp
275 (#PushAddOp) to -> [((), 276 (#PushAddOp) (success))]
276 (#PushAddOp) (success)

#PushID
18 (#PushID) to -> [((), 19 (#PushID) (success))]
19 (#PushID) (success)

#PushNum
314 (#PushNum) to -> [((), 315 (#PushNum) (success))]
315 (#PushNum) (success)

#PushParameter
333 (#PushParameter) to -> [((), 334 (#PushParameter) (success))]
334 (#PushParameter) (success)

#PushRelOp
244 (#PushRelOp) to -> [((), 245 (#PushRelOp) (success))]
245 (#PushRelOp) (success)

#PushReturnValue
162 (#PushReturnValue) to -> [((), 163 (#PushReturnValue) (success))]
163 (#PushReturnValue) (success)

#PushSubOp
279 (#PushSubOp) to -> [((), 280 (#PushSubOp) (success))]
280 (#PushSubOp) (success)

#RelOp
246 (#RelOp) to -> [((), 247 (#RelOp) (success))]
247 (#RelOp) (success)

#SwitchPatchJumpOnNotTest
195 (#SwitchPatchJumpOnNotTest) to -> [((), 196 (#SwitchPatchJumpOnNotTest) (success))]
196 (#SwitchPatchJumpOnNotTest) (success)

#SwitchPatchJumpOnTest
204 (#SwitchPatchJumpOnTest) to -> [((), 205 (#SwitchPatchJumpOnTest) (success))]
205 (#SwitchPatchJumpOnTest) (success)

#SwitchPop
177 (#SwitchPop) to -> [((), 178 (#SwitchPop) (success))]
178 (#SwitchPop) (success)

#SwitchPushTest
175 (#SwitchPushTest) to -> [((), 176 (#SwitchPushTest) (success))]
176 (#SwitchPushTest) (success)

#SwitchSave
193 (#SwitchSave) to -> [((), 194 (#SwitchSave) (success))]
194 (#SwitchSave) (success)

#SwitchTest
191 (#SwitchTest) to -> [((), 192 (#SwitchTest) (success))]
192 (#SwitchTest) (success)

#VarDefinition
33 (#VarDefinition) to -> [((), 34 (#VarDefinition) (success))]
34 (#VarDefinition) (success)

#While
149 (#While) to -> [((), 150 (#While) (success))]
150 (#While) (success)

#WhileLabel
145 (#WhileLabel) to -> [((), 146 (#WhileLabel) (success))]
146 (#WhileLabel) (success)

#WhileSave
147 (#WhileSave) to -> [((), 148 (#WhileSave) (success))]
148 (#WhileSave) (success)

additive-expression
260 (additive-expression) to -> [(term, 261 (additive-expression))]
261 (additive-expression) to -> [(additive-expression-prime, 262 (additive-expression) (success))]
262 (additive-expression) (success)

additive-expression-prime
266 (additive-expression-prime) to -> [(#PushAddOp, 267 (additive-expression-prime)), (#PushSubOp, 271 (additive-expression-prime)), ((), 274 (additive-expression-prime) (success))]
267 (additive-expression-prime) to -> [(+, 268 (additive-expression-prime))]
271 (additive-expression-prime) to -> [(-, 272 (additive-expression-prime))]
274 (additive-expression-prime) (success)
268 (additive-expression-prime) to -> [(addop-relop-rest, 269 (additive-expression-prime))]
272 (additive-expression-prime) to -> [(minus-expr, 273 (additive-expression-prime) (success))]
269 (additive-expression-prime) to -> [(#AddOp, 270 (additive-expression-prime) (success))]
273 (additive-expression-prime) (success)
270 (additive-expression-prime) (success)

addop-relop-rest
248 (addop-relop-rest) to -> [(additive-expression, 249 (addop-relop-rest) (success)), (#PushID, 250 (addop-relop-rest))]
249 (addop-relop-rest) (success)
250 (addop-relop-rest) to -> [(ID, 251 (addop-relop-rest))]
251 (addop-relop-rest) to -> [(addop-relop-rest-reference, 252 (addop-relop-rest) (success))]
252 (addop-relop-rest) (success)

addop-relop-rest-reference
253 (addop-relop-rest-reference) to -> [(id-additive-expression, 254 (addop-relop-rest-reference) (success)), ([, 255 (addop-relop-rest-reference))]
254 (addop-relop-rest-reference) (success)
255 (addop-relop-rest-reference) to -> [(expression, 256 (addop-relop-rest-reference))]
256 (addop-relop-rest-reference) to -> [(], 257 (addop-relop-rest-reference))]
257 (addop-relop-rest-reference) to -> [(#ArrayAccess, 258 (addop-relop-rest-reference))]
258 (addop-relop-rest-reference) to -> [(id-additive-expression, 259 (addop-relop-rest-reference) (success))]
259 (addop-relop-rest-reference) (success)

arg-list
329 (arg-list) to -> [(expression, 330 (arg-list))]
330 (arg-list) to -> [(arg-list-prime, 331 (arg-list))]
331 (arg-list) to -> [(#PushParameter, 332 (arg-list) (success))]
332 (arg-list) (success)

arg-list-prime
335 (arg-list-prime) to -> [(,, 336 (arg-list-prime)), ((), 340 (arg-list-prime) (success))]
336 (arg-list-prime) to -> [(expression, 337 (arg-list-prime))]
340 (arg-list-prime) (success)
337 (arg-list-prime) to -> [(arg-list-prime, 338 (arg-list-prime))]
338 (arg-list-prime) to -> [(#PushParameter, 339 (arg-list-prime) (success))]
339 (arg-list-prime) (success)

args
326 (args) to -> [(arg-list, 327 (args) (success)), ((), 328 (args) (success))]
327 (args) (success)
328 (args) (success)

bracket-id-expression
222 (bracket-id-expression) to -> [(=, 223 (bracket-id-expression)), (#ArrayAccess, 226 (bracket-id-expression))]
223 (bracket-id-expression) to -> [(expression, 224 (bracket-id-expression))]
226 (bracket-id-expression) to -> [(id-simple-expression, 227 (bracket-id-expression) (success))]
224 (bracket-id-expression) to -> [(#AssignArray, 225 (bracket-id-expression) (success))]
227 (bracket-id-expression) (success)
225 (bracket-id-expression) (success)

call
319 (call) to -> [((, 320 (call))]
320 (call) to -> [(args, 321 (call))]
321 (call) to -> [(), 322 (call))]
322 (call) to -> [(#Call, 323 (call) (success))]
323 (call) (success)

case-stmt
183 (case-stmt) to -> [(case, 184 (case-stmt))]
184 (case-stmt) to -> [(#SwitchTest, 185 (case-stmt))]
185 (case-stmt) to -> [(NUM, 186 (case-stmt))]
186 (case-stmt) to -> [(:, 187 (case-stmt))]
187 (case-stmt) to -> [(#SwitchSave, 188 (case-stmt))]
188 (case-stmt) to -> [(statement-list, 189 (case-stmt))]
189 (case-stmt) to -> [(#SwitchPatchJumpOnNotTest, 190 (case-stmt) (success))]
190 (case-stmt) (success)

case-stmts
179 (case-stmts) to -> [(case-stmt, 180 (case-stmts)), ((), 182 (case-stmts) (success))]
180 (case-stmts) to -> [(case-stmts, 181 (case-stmts) (success))]
182 (case-stmts) (success)
181 (case-stmts) (success)

compound-stmt
84 (compound-stmt) to -> [({, 85 (compound-stmt))]
85 (compound-stmt) to -> [(#IncreaseScope, 86 (compound-stmt))]
86 (compound-stmt) to -> [(declaration-list, 87 (compound-stmt))]
87 (compound-stmt) to -> [(statement-list, 88 (compound-stmt))]
88 (compound-stmt) to -> [(#DecreaseScope, 89 (compound-stmt))]
89 (compound-stmt) to -> [(}, 90 (compound-stmt) (success))]
90 (compound-stmt) (success)

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
197 (default-stmt) to -> [(default, 198 (default-stmt)), ((), 203 (default-stmt) (success))]
198 (default-stmt) to -> [(:, 199 (default-stmt))]
203 (default-stmt) (success)
199 (default-stmt) to -> [(#SwitchSave, 200 (default-stmt))]
200 (default-stmt) to -> [(statement-list, 201 (default-stmt))]
201 (default-stmt) to -> [(#SwitchPatchJumpOnTest, 202 (default-stmt) (success))]
202 (default-stmt) (success)

expression
206 (expression) to -> [(simple-expression, 207 (expression) (success)), (#PushID, 208 (expression))]
207 (expression) (success)
208 (expression) to -> [(ID, 209 (expression))]
209 (expression) to -> [(id-expression, 210 (expression) (success))]
210 (expression) (success)

expression-stmt
104 (expression-stmt) to -> [(expression, 105 (expression-stmt)), (continue, 108 (expression-stmt)), (break, 111 (expression-stmt)), (;, 114 (expression-stmt) (success))]
105 (expression-stmt) to -> [(;, 106 (expression-stmt))]
108 (expression-stmt) to -> [(;, 109 (expression-stmt))]
111 (expression-stmt) to -> [(;, 112 (expression-stmt))]
114 (expression-stmt) (success)
106 (expression-stmt) to -> [(#PopID, 107 (expression-stmt) (success))]
109 (expression-stmt) to -> [(#Continue, 110 (expression-stmt) (success))]
112 (expression-stmt) to -> [(#Break, 113 (expression-stmt) (success))]
107 (expression-stmt) (success)
110 (expression-stmt) (success)
113 (expression-stmt) (success)

factor
308 (factor) to -> [((, 309 (factor)), (#PushNum, 312 (factor))]
309 (factor) to -> [(expression, 310 (factor))]
312 (factor) to -> [(NUM, 313 (factor) (success))]
310 (factor) to -> [(), 311 (factor) (success))]
313 (factor) (success)
311 (factor) (success)

fun-compound-stmt
341 (fun-compound-stmt) to -> [({, 342 (fun-compound-stmt))]
342 (fun-compound-stmt) to -> [(declaration-list, 343 (fun-compound-stmt))]
343 (fun-compound-stmt) to -> [(statement-list, 344 (fun-compound-stmt))]
344 (fun-compound-stmt) to -> [(#Function, 345 (fun-compound-stmt))]
345 (fun-compound-stmt) to -> [(#DecreaseScope, 346 (fun-compound-stmt))]
346 (fun-compound-stmt) to -> [(}, 347 (fun-compound-stmt) (success))]
347 (fun-compound-stmt) (success)

fun-declaration
40 (fun-declaration) to -> [(#FunctionSave, 41 (fun-declaration))]
41 (fun-declaration) to -> [((, 42 (fun-declaration))]
42 (fun-declaration) to -> [(#IncreaseScope, 43 (fun-declaration))]
43 (fun-declaration) to -> [(params, 44 (fun-declaration))]
44 (fun-declaration) to -> [(), 45 (fun-declaration))]
45 (fun-declaration) to -> [(fun-compound-stmt, 46 (fun-declaration) (success))]
46 (fun-declaration) (success)

id-additive-expression
263 (id-additive-expression) to -> [(id-term, 264 (id-additive-expression))]
264 (id-additive-expression) to -> [(additive-expression-prime, 265 (id-additive-expression) (success))]
265 (id-additive-expression) (success)

id-expression
211 (id-expression) to -> [(=, 212 (id-expression)), (id-simple-expression, 215 (id-expression) (success)), ([, 216 (id-expression))]
212 (id-expression) to -> [(expression, 213 (id-expression))]
215 (id-expression) (success)
216 (id-expression) to -> [(expression, 217 (id-expression))]
213 (id-expression) to -> [(#Assign, 214 (id-expression) (success))]
217 (id-expression) to -> [(], 218 (id-expression))]
214 (id-expression) (success)
218 (id-expression) to -> [(bracket-id-expression, 219 (id-expression) (success))]
219 (id-expression) (success)

id-simple-expression
235 (id-simple-expression) to -> [(id-additive-expression, 236 (id-simple-expression))]
236 (id-simple-expression) to -> [(rest-of-simple-expression, 237 (id-simple-expression) (success))]
237 (id-simple-expression) (success)

id-term
293 (id-term) to -> [(reference, 294 (id-term))]
294 (id-term) to -> [(term-prime, 295 (id-term) (success))]
295 (id-term) (success)

int-starting-param-list
62 (int-starting-param-list) to -> [(int, 63 (int-starting-param-list))]
63 (int-starting-param-list) to -> [(#PullID, 64 (int-starting-param-list))]
64 (int-starting-param-list) to -> [(ID, 65 (int-starting-param-list))]
65 (int-starting-param-list) to -> [(rest-of-param, 66 (int-starting-param-list))]
66 (int-starting-param-list) to -> [(param-list-prime, 67 (int-starting-param-list) (success))]
67 (int-starting-param-list) (success)

iteration-stmt
136 (iteration-stmt) to -> [(while, 137 (iteration-stmt))]
137 (iteration-stmt) to -> [(#WhileLabel, 138 (iteration-stmt))]
138 (iteration-stmt) to -> [((, 139 (iteration-stmt))]
139 (iteration-stmt) to -> [(expression, 140 (iteration-stmt))]
140 (iteration-stmt) to -> [(), 141 (iteration-stmt))]
141 (iteration-stmt) to -> [(#WhileSave, 142 (iteration-stmt))]
142 (iteration-stmt) to -> [(statement, 143 (iteration-stmt))]
143 (iteration-stmt) to -> [(#While, 144 (iteration-stmt) (success))]
144 (iteration-stmt) (success)

minus-expr
281 (minus-expr) to -> [(term, 282 (minus-expr)), (#PushID, 285 (minus-expr))]
282 (minus-expr) to -> [(#AddOp, 283 (minus-expr))]
285 (minus-expr) to -> [(ID, 286 (minus-expr))]
283 (minus-expr) to -> [(additive-expression-prime, 284 (minus-expr) (success))]
286 (minus-expr) to -> [(id-term, 287 (minus-expr))]
284 (minus-expr) (success)
287 (minus-expr) to -> [(#AddOp, 288 (minus-expr))]
288 (minus-expr) to -> [(additive-expression-prime, 289 (minus-expr) (success))]
289 (minus-expr) (success)

mult-rest
303 (mult-rest) to -> [(term, 304 (mult-rest) (success)), (#PushID, 305 (mult-rest))]
304 (mult-rest) (success)
305 (mult-rest) to -> [(ID, 306 (mult-rest))]
306 (mult-rest) to -> [(id-term, 307 (mult-rest) (success))]
307 (mult-rest) (success)

param
75 (param) to -> [(type-specifier, 76 (param))]
76 (param) to -> [(#PullID, 77 (param))]
77 (param) to -> [(ID, 78 (param))]
78 (param) to -> [(rest-of-param, 79 (param) (success))]
79 (param) (success)

param-list-prime
70 (param-list-prime) to -> [(,, 71 (param-list-prime)), ((), 74 (param-list-prime) (success))]
71 (param-list-prime) to -> [(param, 72 (param-list-prime))]
74 (param-list-prime) (success)
72 (param-list-prime) to -> [(param-list-prime, 73 (param-list-prime) (success))]
73 (param-list-prime) (success)

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
316 (reference) to -> [(call, 317 (reference) (success)), ((), 318 (reference) (success))]
317 (reference) (success)
318 (reference) (success)

rest-of-param
80 (rest-of-param) to -> [((), 81 (rest-of-param) (success)), ([, 82 (rest-of-param))]
81 (rest-of-param) (success)
82 (rest-of-param) to -> [(], 83 (rest-of-param) (success))]
83 (rest-of-param) (success)

rest-of-return-stmt
157 (rest-of-return-stmt) to -> [(;, 158 (rest-of-return-stmt) (success)), (expression, 159 (rest-of-return-stmt))]
158 (rest-of-return-stmt) (success)
159 (rest-of-return-stmt) to -> [(#PushReturnValue, 160 (rest-of-return-stmt))]
160 (rest-of-return-stmt) to -> [(;, 161 (rest-of-return-stmt) (success))]
161 (rest-of-return-stmt) (success)

rest-of-simple-expression
238 (rest-of-simple-expression) to -> [(#PushRelOp, 239 (rest-of-simple-expression)), ((), 243 (rest-of-simple-expression) (success))]
239 (rest-of-simple-expression) to -> [(RELOP, 240 (rest-of-simple-expression))]
243 (rest-of-simple-expression) (success)
240 (rest-of-simple-expression) to -> [(addop-relop-rest, 241 (rest-of-simple-expression))]
241 (rest-of-simple-expression) to -> [(#RelOp, 242 (rest-of-simple-expression) (success))]
242 (rest-of-simple-expression) (success)

rest-of-void-starting-param-list
57 (rest-of-void-starting-param-list) to -> [(ID, 58 (rest-of-void-starting-param-list)), ((), 61 (rest-of-void-starting-param-list) (success))]
58 (rest-of-void-starting-param-list) to -> [(rest-of-param, 59 (rest-of-void-starting-param-list))]
61 (rest-of-void-starting-param-list) (success)
59 (rest-of-void-starting-param-list) to -> [(param-list-prime, 60 (rest-of-void-starting-param-list) (success))]
60 (rest-of-void-starting-param-list) (success)

return-stmt
151 (return-stmt) to -> [(return, 152 (return-stmt))]
152 (return-stmt) to -> [(rest-of-return-stmt, 153 (return-stmt))]
153 (return-stmt) to -> [(#FunctionReturn, 154 (return-stmt) (success))]
154 (return-stmt) (success)

selection-stmt
119 (selection-stmt) to -> [(if, 120 (selection-stmt))]
120 (selection-stmt) to -> [((, 121 (selection-stmt))]
121 (selection-stmt) to -> [(expression, 122 (selection-stmt))]
122 (selection-stmt) to -> [(), 123 (selection-stmt))]
123 (selection-stmt) to -> [(#IfSave, 124 (selection-stmt))]
124 (selection-stmt) to -> [(statement, 125 (selection-stmt))]
125 (selection-stmt) to -> [(#IfJumpSave, 126 (selection-stmt))]
126 (selection-stmt) to -> [(else, 127 (selection-stmt))]
127 (selection-stmt) to -> [(statement, 128 (selection-stmt))]
128 (selection-stmt) to -> [(#IfJump, 129 (selection-stmt) (success))]
129 (selection-stmt) (success)

simple-expression
232 (simple-expression) to -> [(additive-expression, 233 (simple-expression))]
233 (simple-expression) to -> [(rest-of-simple-expression, 234 (simple-expression) (success))]
234 (simple-expression) (success)

statement
97 (statement) to -> [(expression-stmt, 98 (statement) (success)), (compound-stmt, 99 (statement) (success)), (selection-stmt, 100 (statement) (success)), (iteration-stmt, 101 (statement) (success)), (return-stmt, 102 (statement) (success)), (switch-stmt, 103 (statement) (success))]
98 (statement) (success)
99 (statement) (success)
100 (statement) (success)
101 (statement) (success)
102 (statement) (success)
103 (statement) (success)

statement-list
93 (statement-list) to -> [(statement, 94 (statement-list)), ((), 96 (statement-list) (success))]
94 (statement-list) to -> [(statement-list, 95 (statement-list) (success))]
96 (statement-list) (success)
95 (statement-list) (success)

switch-stmt
164 (switch-stmt) to -> [(switch, 165 (switch-stmt))]
165 (switch-stmt) to -> [(#SwitchPushTest, 166 (switch-stmt))]
166 (switch-stmt) to -> [((, 167 (switch-stmt))]
167 (switch-stmt) to -> [(expression, 168 (switch-stmt))]
168 (switch-stmt) to -> [(), 169 (switch-stmt))]
169 (switch-stmt) to -> [({, 170 (switch-stmt))]
170 (switch-stmt) to -> [(case-stmts, 171 (switch-stmt))]
171 (switch-stmt) to -> [(default-stmt, 172 (switch-stmt))]
172 (switch-stmt) to -> [(}, 173 (switch-stmt))]
173 (switch-stmt) to -> [(#SwitchPop, 174 (switch-stmt) (success))]
174 (switch-stmt) (success)

term
290 (term) to -> [(factor, 291 (term))]
291 (term) to -> [(term-prime, 292 (term) (success))]
292 (term) (success)

term-prime
296 (term-prime) to -> [(*, 297 (term-prime)), ((), 300 (term-prime) (success))]
297 (term-prime) to -> [(mult-rest, 298 (term-prime))]
300 (term-prime) (success)
298 (term-prime) to -> [(#MultOp, 299 (term-prime) (success))]
299 (term-prime) (success)

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
|#Assign|ε|) , ; ]|
|#AssignArray|ε|) , ; ]|
|#Break|ε|( ; ID NUM break case continue default else if return switch while { }|
|#Call|ε|) * + , - ; RELOP ]|
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

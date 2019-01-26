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
4. var-declaration → ; | [ #ArrayDefinition NUM ] ;
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
44. call → ( args ) #Call
45. args → arg-list | ε
46. arg-list → expression arg-list-prime #PushParameter
47. arg-list-prime → , expression arg-list-prime #PushParameter | ε
48. fun-compound-stmt → { declaration-list statement-list #Function #DecreaseScope }
```
## State Diagram
```

#AddOp
267 (#AddOp) to -> [((), 268 (#AddOp) (success))]
268 (#AddOp) (success)

#ArrayAccess
220 (#ArrayAccess) to -> [((), 221 (#ArrayAccess) (success))]
221 (#ArrayAccess) (success)

#ArrayDefinition
32 (#ArrayDefinition) to -> [((), 33 (#ArrayDefinition) (success))]
33 (#ArrayDefinition) (success)

#Assign
210 (#Assign) to -> [((), 211 (#Assign) (success))]
211 (#Assign) (success)

#AssignArray
218 (#AssignArray) to -> [((), 219 (#AssignArray) (success))]
219 (#AssignArray) (success)

#Break
114 (#Break) to -> [((), 115 (#Break) (success))]
115 (#Break) (success)

#Call
314 (#Call) to -> [((), 315 (#Call) (success))]
315 (#Call) (success)

#CallMain
8 (#CallMain) to -> [((), 9 (#CallMain) (success))]
9 (#CallMain) (success)

#CaseInsert
186 (#CaseInsert) to -> [((), 187 (#CaseInsert) (success))]
187 (#CaseInsert) (success)

#Continue
112 (#Continue) to -> [((), 113 (#Continue) (success))]
113 (#Continue) (success)

#DecreaseScope
88 (#DecreaseScope) to -> [((), 89 (#DecreaseScope) (success))]
89 (#DecreaseScope) (success)

#DefaultInsert
194 (#DefaultInsert) to -> [((), 195 (#DefaultInsert) (success))]
195 (#DefaultInsert) (success)

#DefinePrint
6 (#DefinePrint) to -> [((), 7 (#DefinePrint) (success))]
7 (#DefinePrint) (success)

#Function
338 (#Function) to -> [((), 339 (#Function) (success))]
339 (#Function) (success)

#FunctionReturn
152 (#FunctionReturn) to -> [((), 153 (#FunctionReturn) (success))]
153 (#FunctionReturn) (success)

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
46 (#IncreaseScope) to -> [((), 47 (#IncreaseScope) (success))]
47 (#IncreaseScope) (success)

#MultOp
291 (#MultOp) to -> [((), 292 (#MultOp) (success))]
292 (#MultOp) (success)

#PopID
20 (#PopID) to -> [((), 21 (#PopID) (success))]
21 (#PopID) (success)

#PullID
65 (#PullID) to -> [((), 66 (#PullID) (success))]
66 (#PullID) (success)

#PushAddOp
265 (#PushAddOp) to -> [((), 266 (#PushAddOp) (success))]
266 (#PushAddOp) (success)

#PushID
18 (#PushID) to -> [((), 19 (#PushID) (success))]
19 (#PushID) (success)

#PushNum
304 (#PushNum) to -> [((), 305 (#PushNum) (success))]
305 (#PushNum) (success)

#PushParameter
323 (#PushParameter) to -> [((), 324 (#PushParameter) (success))]
324 (#PushParameter) (success)

#PushRelOp
234 (#PushRelOp) to -> [((), 235 (#PushRelOp) (success))]
235 (#PushRelOp) (success)

#PushReturnValue
159 (#PushReturnValue) to -> [((), 160 (#PushReturnValue) (success))]
160 (#PushReturnValue) (success)

#PushSubOp
269 (#PushSubOp) to -> [((), 270 (#PushSubOp) (success))]
270 (#PushSubOp) (success)

#RelOp
236 (#RelOp) to -> [((), 237 (#RelOp) (success))]
237 (#RelOp) (success)

#Switch
174 (#Switch) to -> [((), 175 (#Switch) (success))]
175 (#Switch) (success)

#SwitchSave
172 (#SwitchSave) to -> [((), 173 (#SwitchSave) (success))]
173 (#SwitchSave) (success)

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
250 (additive-expression) to -> [(term, 251 (additive-expression))]
251 (additive-expression) to -> [(additive-expression-prime, 252 (additive-expression) (success))]
252 (additive-expression) (success)

additive-expression-prime
256 (additive-expression-prime) to -> [(#PushAddOp, 257 (additive-expression-prime)), (#PushSubOp, 261 (additive-expression-prime)), ((), 264 (additive-expression-prime) (success))]
257 (additive-expression-prime) to -> [(+, 258 (additive-expression-prime))]
261 (additive-expression-prime) to -> [(-, 262 (additive-expression-prime))]
264 (additive-expression-prime) (success)
258 (additive-expression-prime) to -> [(addop-relop-rest, 259 (additive-expression-prime))]
262 (additive-expression-prime) to -> [(minus-expr, 263 (additive-expression-prime) (success))]
259 (additive-expression-prime) to -> [(#AddOp, 260 (additive-expression-prime) (success))]
263 (additive-expression-prime) (success)
260 (additive-expression-prime) (success)

addop-relop-rest
238 (addop-relop-rest) to -> [(additive-expression, 239 (addop-relop-rest) (success)), (#PushID, 240 (addop-relop-rest))]
239 (addop-relop-rest) (success)
240 (addop-relop-rest) to -> [(ID, 241 (addop-relop-rest))]
241 (addop-relop-rest) to -> [(addop-relop-rest-reference, 242 (addop-relop-rest) (success))]
242 (addop-relop-rest) (success)

addop-relop-rest-reference
243 (addop-relop-rest-reference) to -> [(id-additive-expression, 244 (addop-relop-rest-reference) (success)), ([, 245 (addop-relop-rest-reference))]
244 (addop-relop-rest-reference) (success)
245 (addop-relop-rest-reference) to -> [(expression, 246 (addop-relop-rest-reference))]
246 (addop-relop-rest-reference) to -> [(], 247 (addop-relop-rest-reference))]
247 (addop-relop-rest-reference) to -> [(#ArrayAccess, 248 (addop-relop-rest-reference))]
248 (addop-relop-rest-reference) to -> [(id-additive-expression, 249 (addop-relop-rest-reference) (success))]
249 (addop-relop-rest-reference) (success)

arg-list
319 (arg-list) to -> [(expression, 320 (arg-list))]
320 (arg-list) to -> [(arg-list-prime, 321 (arg-list))]
321 (arg-list) to -> [(#PushParameter, 322 (arg-list) (success))]
322 (arg-list) (success)

arg-list-prime
325 (arg-list-prime) to -> [(,, 326 (arg-list-prime)), ((), 330 (arg-list-prime) (success))]
326 (arg-list-prime) to -> [(expression, 327 (arg-list-prime))]
330 (arg-list-prime) (success)
327 (arg-list-prime) to -> [(arg-list-prime, 328 (arg-list-prime))]
328 (arg-list-prime) to -> [(#PushParameter, 329 (arg-list-prime) (success))]
329 (arg-list-prime) (success)

args
316 (args) to -> [(arg-list, 317 (args) (success)), ((), 318 (args) (success))]
317 (args) (success)
318 (args) (success)

bracket-id-expression
212 (bracket-id-expression) to -> [(=, 213 (bracket-id-expression)), (#ArrayAccess, 216 (bracket-id-expression))]
213 (bracket-id-expression) to -> [(expression, 214 (bracket-id-expression))]
216 (bracket-id-expression) to -> [(id-simple-expression, 217 (bracket-id-expression) (success))]
214 (bracket-id-expression) to -> [(#AssignArray, 215 (bracket-id-expression) (success))]
217 (bracket-id-expression) (success)
215 (bracket-id-expression) (success)

call
309 (call) to -> [((, 310 (call))]
310 (call) to -> [(args, 311 (call))]
311 (call) to -> [(), 312 (call))]
312 (call) to -> [(#Call, 313 (call) (success))]
313 (call) (success)

case-stmt
180 (case-stmt) to -> [(case, 181 (case-stmt))]
181 (case-stmt) to -> [(#CaseInsert, 182 (case-stmt))]
182 (case-stmt) to -> [(NUM, 183 (case-stmt))]
183 (case-stmt) to -> [(:, 184 (case-stmt))]
184 (case-stmt) to -> [(statement-list, 185 (case-stmt) (success))]
185 (case-stmt) (success)

case-stmts
176 (case-stmts) to -> [(case-stmt, 177 (case-stmts)), ((), 179 (case-stmts) (success))]
177 (case-stmts) to -> [(case-stmts, 178 (case-stmts) (success))]
179 (case-stmts) (success)
178 (case-stmts) (success)

compound-stmt
81 (compound-stmt) to -> [({, 82 (compound-stmt))]
82 (compound-stmt) to -> [(#IncreaseScope, 83 (compound-stmt))]
83 (compound-stmt) to -> [(declaration-list, 84 (compound-stmt))]
84 (compound-stmt) to -> [(statement-list, 85 (compound-stmt))]
85 (compound-stmt) to -> [(#DecreaseScope, 86 (compound-stmt))]
86 (compound-stmt) to -> [(}, 87 (compound-stmt) (success))]
87 (compound-stmt) (success)

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
188 (default-stmt) to -> [(default, 189 (default-stmt)), ((), 193 (default-stmt) (success))]
189 (default-stmt) to -> [(#DefaultInsert, 190 (default-stmt))]
193 (default-stmt) (success)
190 (default-stmt) to -> [(:, 191 (default-stmt))]
191 (default-stmt) to -> [(statement-list, 192 (default-stmt) (success))]
192 (default-stmt) (success)

expression
196 (expression) to -> [(simple-expression, 197 (expression) (success)), (#PushID, 198 (expression))]
197 (expression) (success)
198 (expression) to -> [(ID, 199 (expression))]
199 (expression) to -> [(id-expression, 200 (expression) (success))]
200 (expression) (success)

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
298 (factor) to -> [((, 299 (factor)), (#PushNum, 302 (factor))]
299 (factor) to -> [(expression, 300 (factor))]
302 (factor) to -> [(NUM, 303 (factor) (success))]
300 (factor) to -> [(), 301 (factor) (success))]
303 (factor) (success)
301 (factor) (success)

fun-compound-stmt
331 (fun-compound-stmt) to -> [({, 332 (fun-compound-stmt))]
332 (fun-compound-stmt) to -> [(declaration-list, 333 (fun-compound-stmt))]
333 (fun-compound-stmt) to -> [(statement-list, 334 (fun-compound-stmt))]
334 (fun-compound-stmt) to -> [(#Function, 335 (fun-compound-stmt))]
335 (fun-compound-stmt) to -> [(#DecreaseScope, 336 (fun-compound-stmt))]
336 (fun-compound-stmt) to -> [(}, 337 (fun-compound-stmt) (success))]
337 (fun-compound-stmt) (success)

fun-declaration
37 (fun-declaration) to -> [(#FunctionSave, 38 (fun-declaration))]
38 (fun-declaration) to -> [((, 39 (fun-declaration))]
39 (fun-declaration) to -> [(#IncreaseScope, 40 (fun-declaration))]
40 (fun-declaration) to -> [(params, 41 (fun-declaration))]
41 (fun-declaration) to -> [(), 42 (fun-declaration))]
42 (fun-declaration) to -> [(fun-compound-stmt, 43 (fun-declaration) (success))]
43 (fun-declaration) (success)

id-additive-expression
253 (id-additive-expression) to -> [(id-term, 254 (id-additive-expression))]
254 (id-additive-expression) to -> [(additive-expression-prime, 255 (id-additive-expression) (success))]
255 (id-additive-expression) (success)

id-expression
201 (id-expression) to -> [(=, 202 (id-expression)), (id-simple-expression, 205 (id-expression) (success)), ([, 206 (id-expression))]
202 (id-expression) to -> [(expression, 203 (id-expression))]
205 (id-expression) (success)
206 (id-expression) to -> [(expression, 207 (id-expression))]
203 (id-expression) to -> [(#Assign, 204 (id-expression) (success))]
207 (id-expression) to -> [(], 208 (id-expression))]
204 (id-expression) (success)
208 (id-expression) to -> [(bracket-id-expression, 209 (id-expression) (success))]
209 (id-expression) (success)

id-simple-expression
225 (id-simple-expression) to -> [(id-additive-expression, 226 (id-simple-expression))]
226 (id-simple-expression) to -> [(rest-of-simple-expression, 227 (id-simple-expression) (success))]
227 (id-simple-expression) (success)

id-term
283 (id-term) to -> [(reference, 284 (id-term))]
284 (id-term) to -> [(term-prime, 285 (id-term) (success))]
285 (id-term) (success)

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
271 (minus-expr) to -> [(term, 272 (minus-expr)), (#PushID, 275 (minus-expr))]
272 (minus-expr) to -> [(#AddOp, 273 (minus-expr))]
275 (minus-expr) to -> [(ID, 276 (minus-expr))]
273 (minus-expr) to -> [(additive-expression-prime, 274 (minus-expr) (success))]
276 (minus-expr) to -> [(id-term, 277 (minus-expr))]
274 (minus-expr) (success)
277 (minus-expr) to -> [(#AddOp, 278 (minus-expr))]
278 (minus-expr) to -> [(additive-expression-prime, 279 (minus-expr) (success))]
279 (minus-expr) (success)

mult-rest
293 (mult-rest) to -> [(term, 294 (mult-rest) (success)), (#PushID, 295 (mult-rest))]
294 (mult-rest) (success)
295 (mult-rest) to -> [(ID, 296 (mult-rest))]
296 (mult-rest) to -> [(id-term, 297 (mult-rest) (success))]
297 (mult-rest) (success)

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
1 (program) to -> [(#DefinePrint, 2 (program))]
2 (program) to -> [(declaration-list, 3 (program))]
3 (program) to -> [(#CallMain, 4 (program))]
4 (program) to -> [(EOF, 5 (program) (success))]
5 (program) (success)

reference
306 (reference) to -> [(call, 307 (reference) (success)), ((), 308 (reference) (success))]
307 (reference) (success)
308 (reference) (success)

rest-of-param
77 (rest-of-param) to -> [((), 78 (rest-of-param) (success)), ([, 79 (rest-of-param))]
78 (rest-of-param) (success)
79 (rest-of-param) to -> [(], 80 (rest-of-param) (success))]
80 (rest-of-param) (success)

rest-of-return-stmt
154 (rest-of-return-stmt) to -> [(;, 155 (rest-of-return-stmt) (success)), (expression, 156 (rest-of-return-stmt))]
155 (rest-of-return-stmt) (success)
156 (rest-of-return-stmt) to -> [(#PushReturnValue, 157 (rest-of-return-stmt))]
157 (rest-of-return-stmt) to -> [(;, 158 (rest-of-return-stmt) (success))]
158 (rest-of-return-stmt) (success)

rest-of-simple-expression
228 (rest-of-simple-expression) to -> [(#PushRelOp, 229 (rest-of-simple-expression)), ((), 233 (rest-of-simple-expression) (success))]
229 (rest-of-simple-expression) to -> [(RELOP, 230 (rest-of-simple-expression))]
233 (rest-of-simple-expression) (success)
230 (rest-of-simple-expression) to -> [(addop-relop-rest, 231 (rest-of-simple-expression))]
231 (rest-of-simple-expression) to -> [(#RelOp, 232 (rest-of-simple-expression) (success))]
232 (rest-of-simple-expression) (success)

rest-of-void-starting-param-list
54 (rest-of-void-starting-param-list) to -> [(ID, 55 (rest-of-void-starting-param-list)), ((), 58 (rest-of-void-starting-param-list) (success))]
55 (rest-of-void-starting-param-list) to -> [(rest-of-param, 56 (rest-of-void-starting-param-list))]
58 (rest-of-void-starting-param-list) (success)
56 (rest-of-void-starting-param-list) to -> [(param-list-prime, 57 (rest-of-void-starting-param-list) (success))]
57 (rest-of-void-starting-param-list) (success)

return-stmt
148 (return-stmt) to -> [(return, 149 (return-stmt))]
149 (return-stmt) to -> [(rest-of-return-stmt, 150 (return-stmt))]
150 (return-stmt) to -> [(#FunctionReturn, 151 (return-stmt) (success))]
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
222 (simple-expression) to -> [(additive-expression, 223 (simple-expression))]
223 (simple-expression) to -> [(rest-of-simple-expression, 224 (simple-expression) (success))]
224 (simple-expression) (success)

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
161 (switch-stmt) to -> [(switch, 162 (switch-stmt))]
162 (switch-stmt) to -> [(#SwitchSave, 163 (switch-stmt))]
163 (switch-stmt) to -> [((, 164 (switch-stmt))]
164 (switch-stmt) to -> [(expression, 165 (switch-stmt))]
165 (switch-stmt) to -> [(), 166 (switch-stmt))]
166 (switch-stmt) to -> [({, 167 (switch-stmt))]
167 (switch-stmt) to -> [(case-stmts, 168 (switch-stmt))]
168 (switch-stmt) to -> [(default-stmt, 169 (switch-stmt))]
169 (switch-stmt) to -> [(}, 170 (switch-stmt))]
170 (switch-stmt) to -> [(#Switch, 171 (switch-stmt) (success))]
171 (switch-stmt) (success)

term
280 (term) to -> [(factor, 281 (term))]
281 (term) to -> [(term-prime, 282 (term) (success))]
282 (term) (success)

term-prime
286 (term-prime) to -> [(*, 287 (term-prime)), ((), 290 (term-prime) (success))]
287 (term-prime) to -> [(mult-rest, 288 (term-prime))]
290 (term-prime) (success)
288 (term-prime) to -> [(#MultOp, 289 (term-prime) (success))]
289 (term-prime) (success)

type-specifier
34 (type-specifier) to -> [(int, 35 (type-specifier) (success)), (void, 36 (type-specifier) (success))]
35 (type-specifier) (success)
36 (type-specifier) (success)

var-declaration
25 (var-declaration) to -> [(;, 26 (var-declaration) (success)), ([, 27 (var-declaration))]
26 (var-declaration) (success)
27 (var-declaration) to -> [(#ArrayDefinition, 28 (var-declaration))]
28 (var-declaration) to -> [(NUM, 29 (var-declaration))]
29 (var-declaration) to -> [(], 30 (var-declaration))]
30 (var-declaration) to -> [(;, 31 (var-declaration) (success))]
31 (var-declaration) (success)

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
|#Call|ε|) * + , - ; RELOP ]|
|#CallMain|ε|EOF|
|#CaseInsert|ε|NUM|
|#Continue|ε|( ; ID NUM break case continue default else if return switch while { }|
|#DecreaseScope|ε|}|
|#DefaultInsert|ε|:|
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

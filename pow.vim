" Vim syntax file
" Language: PowerText
" Maintainer: Stéphane Meyer
" Last change: 2017 Aug 14

if exists("b:current_syntax")
  finish
endif

syn case match

" ============================================================================

syn match powOp  "\v-\s"
syn match powOp  "\v--"
syn match powOp  "++"
syn match powOp  "\v\+\s"
syn match powOp  "\*\*\*\s"
syn match powOp  "\*\*\s"
syn match powOp  "\*\s"
syn match powOp  "\v\="
syn match powOp  "<<"
syn match powOp  ">>"
syn match powOp  "<"
syn match powOp  "<="
syn match powOp  ">"
syn match powOp  ">="
syn match powOp  "!="
syn match powOp  "\v//"
syn match powOp  "\v/"
syn match powOp  "%"

syn keyword powFunc and		cal     char	clear	close	del	echo	expect	filter	getcur	head
syn keyword powFunc lambda	len	map	not	open	or	ord	pause	pop	push	read 
syn keyword powFunc read-file	rnd	scrsize	tail	time	tonum	tostr	type	uses 
syn keyword powFunc write-file	xor

syn keyword powCond for while exit skip
syn match   powCond "??"
syn match   powCond "?"
syn keyword powType bool list null int real frac string

syn keyword powBool true false

syn region powString start='"' skip=/\v\\./ end='"'
syn region powString start="'" skip=/\v\\./ end="'"

syn keyword powTodo todo fixme notes note contained
syn match powComment ";;.*\|#.*" contains=powTodo

syn match   powID "\v[a-zA-Z_(][a-zA-Z0-9-_:)]*" display contained

syn keyword powStatement def  nextgroup=powID skipwhite 
syn keyword powStatement set  nextgroup=powID skipwhite
syn keyword powStatement setg nextgroup=powID skipwhite

syn match   powLambda "\v\@[a-zA-Z_][a-zA-Z0-9-_]*" display contained

syn keyword powLambdaCall @ nextgroup=powLambda skipwhite

syn match powNumber "\<\d\+"
syn match powNumber "[-]\d\+"
syn match powNumber "\<\d\+\.\d*"
syn match powNumber "[-]\d\+\.\d*"

syn match powOp   "\v1\v\+"
syn match powOp   "\v1\v-"

syn sync lines=100

hi def link powFunc       Keyword
hi def link powOp         Operator
hi def link powCond       Conditional
hi def link powType       Type
hi def link powBool       Boolean
hi def link powString     String
hi def link powNumber     Number
hi def link powID         Identifier
hi def link powLambda     Identifier
hi def link powLambdaCall Identifier
hi def link powStatement  Statement
hi def link powComment    Comment
hi def link powTodo       Todo

let b:current_syntax = "pow"

" Vim syntax file
" Language: PowerText
" Maintainer: Stéphane Meyer
" Last change: 2017 Aug 05

if exists("b:current_syntax")
  finish
endif

syn case match

" ============================================================================

syn match powNumber "\d\+"
syn match powNumber "[-]\d\+"
syn match powNumber "\d\+\.\d*"
syn match powNumber "[-]\d\+\.\d*"

syn keyword powFunc and close del def echo filter getcur head input lambda
syn keyword powFunc len map not open or pause pop push read read-file rnd
syn keyword powFunc scrsize set setg tail time type uses write-file xor

syn match powId     "\v[a-zA-Z_][a-zA-Z0-9\-_]*"

syn match   powOp   "\v\+"
syn match   powOp   "++"
syn match   powOp   "\v-"
syn match   powOp   "\v--"
syn match   powOp   "\v\*"
syn match   powOp   "\v/"
syn match   powOp   "\v//"
syn match   powOp   "\v\%"
syn match   powOp   "\v!\="
syn match   powOp   "\v\<"
syn match   powOp   "\v\>"
syn match   powOp   "\v<\="
syn match   powOp   "\v\>\="
syn match   powOp   "\v\="
syn match   powOp   "@"

syn keyword powCond for while exit
syn match   powCond "??"
syn match   powCond "?"
syn keyword powType bool list null number string

syn keyword powBool true false

syn region powString start='"' skip=/\v\\./ end='"'
syn region powString start="'" skip=/\v\\./ end="'"

syn keyword powTodo todo fixme contained
syn match powComment ";;.*\|#.*" contains=powTodo

syn match   powOp   "\v1\v\+"
syn match   powOp   "\v1\v-"

syn sync lines=100

hi def link powFunc       Keyword
hi def link powId         Identifier
hi def link powOp         Operator
hi def link powCond       Conditional
hi def link powType       Type
hi def link powBool       Boolean
hi def link powString     String
hi def link powNumber     Number
hi def link powComment    Comment
hi def link powTodo       Todo

let b:current_syntax = "pow"

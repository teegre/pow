" Vim syntax file
" Language: PowerText
" Maintainer: Stéphane Meyer
" Last change: 2017 Jul 28

if exists("b:current_syntax")
  finish
endif

syn case match

" =======================================================================

syn keyword powFunc and close del def echo getcur head input lambda last
syn keyword powFunc not open or pause push read rnd scrsize set tail time uses write xor
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

syn region  powFuncBlock start=/def/ skip=/def/ end=/:/  contains=powFuncBlock

syn keyword powCond for while exit
syn match   powCond "?"
syn keyword powType bool list null number string

syn keyword powBool true false

syn region powString start='"' skip=/\v\\./ end='"'
syn region powString start="'" skip=/\v\\./ end="'"

syn match powNumber "\d\+"
syn match powNumber "[-]\d\+"
syn match powNumber "\d\+\.\d*"
syn match powNumber "[-]\d\+\.\d*"


syn keyword powTodo todo fixme contained
syn match powComment ";;.*\|#.*" contains=powTodo

syn sync lines=100

hi def link powFunc       Keyword
hi def link powFuncBlock  Statement
hi def link powOp         Operator
hi def link powCond       Conditional
hi def link powType       Type
hi def link powBool       Boolean
hi def link powString     String
hi def link powNumber     Number
hi def link powComment    Comment
hi def link powTodo       Todo

let b:current_syntax = "pow"

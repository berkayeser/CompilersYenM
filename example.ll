; ModuleID = "C_compiler"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i1 @"main"()
{
entry:
  ; constintx=1;
  store i32 1, i32* %"x"
  %"x" = alloca i32
  ret i1 0
}

; ModuleID = "C_compiler"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i1 @"main"()
{
entry:
  ; 5*(3/10+9/10);
  %".2" = sdiv i32 3, 10
  %".3" = sdiv i32 9, 10
  %".4" = add i32 %".2", %".3"
  %".5" = mul i32 5, %".4"
  ; 6*2/(2+1*2/3+6)+8*(8/4);
  %".6" = sdiv i32 2, 3
  %".7" = mul i32 1, %".6"
  %".8" = add i32 %".7", 6
  %".9" = add i32 2, %".8"
  %".10" = sdiv i32 2, %".9"
  %".11" = mul i32 6, %".10"
  %".12" = sdiv i32 8, 4
  %".13" = mul i32 8, %".12"
  %".14" = add i32 %".11", %".13"
  ; (1+1);
  %".15" = add i32 1, 1
  ret i1 0
}

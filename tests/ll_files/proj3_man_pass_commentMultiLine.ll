declare i32 @printf(i8*, ...)
@intFormat = private constant [4 x i8] c"%d\0A\00"@floatFormat = private constant [4 x i8] c"%f\0A\00"
define void @printInt(i32 %a) {
%p = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],
[4 x i8]* @intFormat,i32 0, i32 0), i32 %a)
ret void
}

define void @printFloat(float %a) {
%p = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],
[4 x i8]* @floatFormat,i32 0, i32 0), float %a)
ret void
}

define i1 @"main"()
{
; /*
 * This is a comment
 *
 *
; /**
 * Another Comment
  ***** /

  /**

  *
  *
  **
; intline_of_code=5;
%line_of_code = alloca int
%1 = trunc i32 5 to int
store int %1, int %line_of_code
; /* /// ** ** // // //  *
; floatf=45;
%f = alloca float
%2 = sitofp i32 45 to float
store float %2, float %f
; charc='b';
%c = alloca char
%3 = trunc i8 98 to char
store char %3, char %c
; intx=5;
%x = alloca int
%4 = trunc i32 5 to int
store int %4, int %x
ret i1 0
}

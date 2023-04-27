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
; floatx=251457;
%x = alloca float
%1 = sitofp i32 251457 to float
store float %1, float* %x
; floaty=4587854;
%y = alloca float
%2 = sitofp i32 4587854 to float
store float %2, float* %y
; y=54456456487;
%3 = sitofp i32 544564 to float
store float %3, float* %y
; (64.54879<missing ';'>
; 32328.4897);
ret i1 0
}

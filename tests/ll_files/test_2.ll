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
; constintx=5*(30/10+90/10);
%x = alloca i32
%1 = sdiv i32 30, 10
%2 = sdiv i32 90, 10
%3 = add i32 %1, %2
%4 = mul i32 5, %3
store i32 %4, i32* %x
; printf(x);
%5 = load i32, i32* %x
call void @printInt(i32 %5)
; floaty=x*2*(3*20*3+x)+8*(8*4);
%y = alloca float
%6 = load i32, i32* %x
%7 = mul i32 20, 3
%8 = mul i32 3, %7
%9 = load i32, i32* %x
%10 = add i32 %8, %9
%11 = mul i32 2, %10
%12 = mul i32 %6, %11
%13 = mul i32 8, 4
%14 = mul i32 8, %13
%15 = add i32 %12, %14
%16 = sitofp i32 %15 to float
store float %16, float* %y
; printf(y);
%17 = fadd float %16, 1.0
call void @printFloat(float %17)
; y=x+y;
%18 = load i32, i32* %x
%19 = load float, float* %y
%20 = sitofp i32 %18 to float
%21 = fadd float %20, %19
store float %21, float* %y
; printf(y);
%22 = load float, float* %y
call void @printFloat(float %22)
; intz;
%z = alloca i32
; charch='x';
%ch = alloca i8
store i8 120, i8* %ch
ret i1 0
}

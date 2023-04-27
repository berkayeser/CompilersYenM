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
; intx=5;
%x = alloca i32
store i32 5, i32* %x
; int*y=&x;
%y = alloca i32*
store i32* %x, i32** %y
%".1" = load i32*, i32** %y
store i32 6, i32* %".1"
%".2" = load i32, i32* %x
call void @printInt(i32 %".2")
ret i1 0
}
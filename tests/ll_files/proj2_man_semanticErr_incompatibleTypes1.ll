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
; intx=478;
%x = alloca i32
store i32 478, i32* %x
; intb=-251454;
%b = alloca i32
store i32 -251454, i32* %b
; int*b_ptr=&b;
%b_ptr = alloca i32*
store i32* %b, i32** %b_ptr
; int**x_ptr=&b_ptr;
%x_ptr = alloca i32**
store i32** %b_ptr, i32*** %x_ptr
; x_ptr=&b;
store i32* %b, i32*** %x_ptr
ret i1 0
}

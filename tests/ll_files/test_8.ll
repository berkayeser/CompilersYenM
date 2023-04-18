declare i32 @printf(i8*, ...)
@format = private constant [4 x i8] c"%d\0A\00"
define void @print(i32 %a){%p = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @format,i32 0, i32 0),i32 %a)ret void}
define i1 @"main"()
{
%hey = alloca i32
%hoi = alloca i32*
%b = alloca i32
store i32 7, i32* %b
store i32* %hey, i32** %hoi
store i32 3, i32* %hey
%val = load i32*, i32** %hoi
store i32 5, i32* %val
%val2 = load i32, i32* %val
%val3 = load i32, i32* %hey
store i32* %b, i32* %hey
call void @print(i32 %val2)
call void @print(i32 %val3)
ret i1 0
}
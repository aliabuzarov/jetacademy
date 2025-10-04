def qar_sade(x,y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
        return x
first=int(input())
second=int(input())
if qar_sade(first,second)==1:
    print(f'{first}, {second} qarşılıqlı sadə ədədlərdir.')
else:
    print(f"{first}, {second} qarşılıqlı sadə ədədlər deyil.")
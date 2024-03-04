c1=eval(input('Digite o primeiro numero: '))
c2=eval(input('Digite o segundo numero: '))
if c1+c2==c2+c1:
    print('Vale a comutatividade da soma')

if c1*c2==c2*c1:
    print('Vale a comutatividade do produto')

c3=eval(input('Digite mais 1 numero'))

if (c1+c2)+c3==c1+(c2+c3) and c1*(c2*c3)==(c1*c2)*c3:
    print('Vale a associatividade na soma e multiplicacao')
if c1*(c2+c3)==(c1*c2)+c2*c3:
    print('Vale a distribuitividade')

    
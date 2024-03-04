c1=complex(input('Digite umm numero '))
c2=complex(input('Digite umm numero '))

c1conj=c1.real-c1.imag* 1j
c2conj=c2.real-c2.imag* 1j
c1ouc2conj=(c1+c2).real-(c1+c2).imag* 1j
c1ec2conj=(c1*c2).real -(c1*c2).imag *1j
if c1conj+c2conj==c1ouc2conj:
    print(f'Os valores sao iguais e valem: {c1ouc2conj}')
if c1conj*c2conj==c1ec2conj:
    print(f'Os valores sao iguais e valem{c1ec2conj}')
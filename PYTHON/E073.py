times = ('L. Noris', 'Max Verstapen', 'O. Piastri', 'G. Russell', 'C. Leclerc', 'L. Hamilton',
         'A.K.Antoneli', 'A. Albon', 'C. Sainz', 'F. Alonso', 'N. Hulkenberg', 'I. Hadjar', 'O Bearman',
         'L. Lawson', 'E. Ocon', 'L. Stroll', 'Y. Tsunoda', 'P. Gasly','G. Bortoleto', 'F. Colapinto')
print(f'Os primeiros 5 colocados são: {times[:6]}')
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print(f'Os pilotos em ordem alfabética fica assim:{sorted(times)}')
print(f'O Gabriel Bortoleto ficou na posição:{times.index('G. Bortoleto')+1}')
from django.shortcuts import render

elenco = [
    {'foto': 'jogador1.jpg', 'nome': 'augustin rossi', 'idade': 29, 'posicao': 'goleiro', 'nascimento': 'argentina'},
    {'foto': 'jogador2.jpg', 'nome': 'léo ortiz', 'idade': 29, 'posicao': 'zagueiro', 'nascimento': 'brasil'},
    {'foto': 'jogador3.jpg', 'nome': 'léo pereira', 'idade': 29, 'posicao': 'zagueiro', 'nascimento': 'brasil'}
    {'foto': 'jogador4.jpg', 'nome': 'alex sandro', 'idade': 34, 'posicao': 'lateral esquerdo', 'nascimento': 'brasil'},
    {'foto': 'jogador5.jpg', 'nome': 'wesley frança', 'idade': 21, 'posicao': 'lateral direito', 'nascimento': 'brasil'},
    {'foto': 'jogador6.jpg', 'nome': 'erick pulgar', 'idade': 31, 'posicao': 'volante', 'nascimento': 'chile'},
    {'foto': 'jogador7.jpg', 'nome': 'jorginho', 'idade': 33, 'posicao': 'volante', 'nascimento': 'itália'},
    {'foto': 'jogador8.jpg', 'nome': 'de arrascaeta', 'idade': 31, 'posicao': 'meia atacante', 'nascimento': 'uruguai'},
    {'foto': 'jogador9.jpg', 'nome': 'luiz araújo', 'idade': 29, 'posicao': 'ponta direita', 'nascimento': 'brasil'},
    {'foto': 'jogador10.jpg', 'nome': 'bruno henrique', 'idade': 34, 'posicao': 'ponta esquerda', 'nascimento': 'brasil'},
    {'foto': 'jogador11.jpg', 'nome': 'pedro', 'idade': 28, 'posicao': 'centroavante', 'nascimento': 'brasil'},

    
  
]


info_site = {
    'titulo': 'clubes de regatas do flamengo ',
    'historia': 'O Flamengo foi fundado em 17 de novembro de 1895 para as disputas de remo. A entrada da equipe no futebol aconteceu em 1912. Atualmente, o time rubro-negro é o maior vencedor da história do Campeonato Carioca, com 31 títulos. Segundo diversas pesquisas, é o clube com o maior número de torcedores do País. Os dois principais títulos da história do Flamengo ocorreram em 1981. Comandado pelo ídolo Zico, o time conquistou a Copa Libertadores da América, em final contra o Cobreloa, do Chile, e o Mundial Interclubes, diante do Liverpool, da Inglaterra. Foi na década de 1980, também, que o Flamengo conquistou o seu primeiro Campeonato Brasileiro.

',
    'autores': ['Luiz Felipe', 'carlos eduardo']
}

def inicio(request):
    return render(request, 'inicio.html', info_site)

def equipe(request):
    return render(request, 'equipe.html', {'elenco': elenco})

def sobre(request):
    return render(request, 'sobre.html', info_site)
from django.shortcuts import render

elenco = {
    'atletas': [
        {'foto': 'jogador1.jpg', 'nome': 'augustin rossi', 'idade': 29, 'posicao': 'goleiro', 'nascimento': 'argentina'},
        {'foto': 'jogador2.jpg', 'nome': 'léo ortiz', 'idade': 29, 'posicao': 'zagueiro', 'nascimento': 'brasil'},
        {'foto': 'jogador3.jpg', 'nome': 'léo pereira', 'idade': 29, 'posicao': 'zagueiro', 'nascimento': 'brasil'},
        {'foto': 'jogador4.jpg', 'nome': 'alex sandro', 'idade': 34, 'posicao': 'lateral esquerdo', 'nascimento': 'brasil'},
        {'foto': 'jogador5.jpg', 'nome': 'wesley franca', 'idade': 21, 'posicao': 'lateral direito', 'nascimento': 'brasil'},
        {'foto': 'jogador6.jpg', 'nome': 'erick pulgan', 'idade': 31, 'posicao': 'volante', 'nascimento': 'chile'},
        {'foto': 'jogador7.jpg', 'nome': 'jorginho', 'idade': 33, 'posicao': 'volante', 'nascimento': 'itália'},
        {'foto': 'jogador8.jpg', 'nome': 'de arrascaeta', 'idade': 31, 'posicao': 'meia atacante', 'nascimento': 'uruguai'},
        {'foto': 'jogador9.jpg', 'nome': 'luiz araújo', 'idade': 29, 'posicao': 'ponta direita', 'nascimento': 'brasil'},
        {'foto': 'jogador10.jpg', 'nome': 'bruno henrique', 'idade': 34, 'posicao': 'ponta esquerda', 'nascimento': 'brasil'},
        {'foto': 'jogador11.jpg', 'nome': 'pedro', 'idade': 28, 'posicao': 'centroavante', 'nascimento': 'brasil'}
    ]
}

info_site = {
    'titulo': 'clubes de regatas do flamengo',
    'historia': 'o flamengo foi fundado em 17 de novembro de 1895 para as disputas de remo. A entrada da equipe de futebol só aconteceu em 1912.',
    'autores': ['luiz felipe', 'carlos eduardo']
}

def inicio(request):
    return render(request, 'website/inicio.html', {'info': info_site})

def equipe(request):
    return render(request, 'website/equipe.html', elenco)

def sobre(request):
    return render(request, 'website/sobre.html', {'info': info_site})
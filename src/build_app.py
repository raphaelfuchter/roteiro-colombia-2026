import base64, io, json, os, urllib.parse
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
exec(open('data_M.py').read())

def img(k):
    im = Image.open(f'img/{k}.jpg').convert('RGB'); im.thumbnail((760, 760))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=74)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

DAYS = {
 'Qua 11/11': ('2026-11-11', 'ctg', 'Qua', '11', 'Chegada', []),
 'Qui 12/11': ('2026-11-12', 'ctg', 'Qui', '12', 'Aviário Nacional + Barú', []),
 'Sex 13/11': ('2026-11-13', 'ctg', 'Sex', '13', 'Centro Histórico + Getsemaní', []),
 'Sáb 14/11': ('2026-11-14', 'sai', 'Sáb', '14', 'Voo para San Andrés', []),
 'Dom 15/11': ('2026-11-15', 'sai', 'Dom', '15', 'Praia e Zona Rosa', []),
 'Seg 16/11': ('2026-11-16', 'sai', 'Seg', '16', 'Ilha em ritmo lento', []),
 'Ter 17/11': ('2026-11-17', 'sai', 'Ter', '17', 'Despedida com vista para o mar', []),
}
CITY = {'ctg': ('Cartagena', '🏰'), 'sai': ('San Andrés', '🌴')}
CITY_Q = {'ctg': 'Cartagena Colombia', 'sai': 'San Andres Isla Colombia'}

IG = {'Perú Wok':'peruwok','Aqua Beach Club':'aquabeachclub','Cafeteria Kafih':'cafeteria_kafih','Coral Restobar':'coralrestobarsai',
 'Fondita y Mar Mix':'fonditaymarmix','Raizal Roots':'raizalroots','Sweet Avenue':'sweetavenue_bymarwa','La Marina':'lamarinasai',
 'Espíritu Santo':'espiritusanto.cartagena','La Casa de Socorro':'restaurantelacasadesocorro','El Peruano':'elperuanosai'}
meals = []
for d, h, t, n, c, r, q, f, p, pr, dc, loc, ds in M:
    iso, city = DAYS[d][0], DAYS[d][1]
    meals.append(dict(day=iso, time=h, type=t, name=n, cuisine=c, rating=r, count=q, src=f, price=p,
                      dishes=[x.strip() for x in pr.split('·')], tip=dc, local=bool(loc),
                      photos=[dict(s=img(x), ig=x.startswith(('r_','d_'))) for x in ([loc] if loc else []) + ds],
                      maps='https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(f'{n} {CITY_Q[city]}'), ig=IG.get(n)))

def gm(q): return 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(q)
ACT = [
 ('2026-11-11','18h00','✈️','Chegada a Cartagena','Aeroporto Rafael Núñez, em Crespo, colado à cidade.','Táxi oficial na saída do aeroporto (fila com tabela de preço fixo) ou Uber/DiDi: ~15 min até o centro.','p_aeroporto','Aeropuerto Internacional Rafael Núñez Cartagena'),
 ('2026-11-12','08h30','🦜','Aviário Nacional da Colômbia','Maior aviário do país, com 2 mil aves de ~190 espécies em trilhas pela mata seca, no caminho para Barú. Abre às 9h; reserve ~2h.','Longe: ~50 min de carro. Melhor contratar um táxi/motorista por dia (ida + espera + Playa Blanca + volta) e combinar o preço antes, ou ir de Uber e voltar de táxi local.','p_aviario','Aviario Nacional de Colombia Baru'),
 ('2026-11-12','11h45','🏝️','Playa Blanca (Barú)','Areia branca e mar azul-turquesa; a praia mais famosa de Barú. Cheia de ambulantes: negocie tudo antes.','~10 min de carro do Aviário pela mesma estrada. O motorista deixa na entrada da praia.','p_playablanca','Playa Blanca Barú'),
 ('2026-11-12','13h30','🌊','Playa Tranquila','Ao lado de Playa Blanca, mais calma e com menos vendedores: boa pra passar a tarde depois do almoço.','15–20 min a pé pela areia a partir de Playa Blanca. Volta a Cartagena ~1h de carro: combine o motorista para ~16h30 e chegue antes de escurecer.','p_barubeach','Playa Tranquila Barú'),
 ('2026-11-13','09h00','🏰','Castillo San Felipe de Barajas','A maior fortaleza espanhola das Américas: túneis escuros e um mirante com vista da cidade toda. Vá cedo, por causa do calor.','Do centro: táxi ~5–10 min, ou a pé ~20 min saindo da Torre do Relógio.','p_castillo','Castillo San Felipe de Barajas'),
 ('2026-11-13','10h30','🕰️','Torre do Relógio','Portão de entrada da cidade murada; daqui você caminha por ruas coloniais até o almoço.','Do Castillo: táxi ~5 min ou a pé ~20 min. Tudo no centro histórico se faz a pé.','p_torre','Torre del Reloj Cartagena'),
 ('2026-11-13','14h00','⛪','Plaza de Santo Domingo','Arquitetura colonial, a Gertrudis de Botero, mesas ao ar livre e artistas de rua no fim da tarde.','A pé, ~5 min da Torre do Relógio.','p_stodomingo','Plaza de Santo Domingo Cartagena'),
 ('2026-11-13','18h30','🎨','Getsemaní','O bairro mais vibrante: murais de grafite, bandeirinhas, guarda-chuvas coloridos, bares e galerias. Lindo à noite.','A pé, ~10 min saindo da Torre do Relógio.','p_getsemani','Getsemaní Cartagena'),
 ('2026-11-13','21h00','💃','Plaza de la Trinidad','Coração de Getsemaní: viajantes reunidos, comida de rua e apresentações de dança.','A pé, ~3 min da La Casa de Socorro. Para voltar ao hotel, táxi ou Uber.','p_trinidad','Plaza de la Trinidad Getsemaní Cartagena'),
]
acts = [dict(day=d, time=t, icon=i, name=n, desc=ds, how=h, photo=img(p), maps=gm(q)) for d,t,i,n,ds,h,p,q in ACT]
days = [dict(iso=v[0], city=v[1], wd=v[2], dd=v[3], title=v[4], notes=v[5]) for v in DAYS.values()]
extras = {
 'ctg': [dict(name='La Cocina de Pepina', cuisine='Colombiana · Getsemaní', rating=4.5, count='~1,8 mil', src='Google', price=2, tip='Plano B pro jantar em Getsemaní.'),
         dict(name='Crepes & Waffles', cuisine='Rede colombiana · crepes, waffles, sorvete', rating=None, count='', src='', price=1, tip='Sobremesa barata em qualquer dia.')],
 'sai': [dict(name='Bobaloves', cuisine='Chás gelados e bebidas frutadas', rating=None, count='', src='', price=1, tip='Pausa refrescante numa tarde quente.'),
         dict(name='Barrira Burrito', cuisine='Mexicana', rating=None, count='', src='', price=1, tip='Fome fora de hora, rápido e barato.')],
}
for c, lst in extras.items():
    for e in lst: e['maps'] = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(f"{e['name']} {CITY_Q[c]}")
data = json.dumps(dict(meals=meals, acts=acts, days=days, extras=extras, city={k: list(v) for k, v in CITY.items()}), ensure_ascii=False)

html = open('app_template.html').read().replace('/*DATA*/', data)
open('../index.html', 'w').write(html)

print(len(html) // 1024, 'KB')

import json,re,html
d=json.load(open('raw/landscape/2026-11-26/flipkart-reviews-names-removed.json'))
themes={
 'hair_skin (motive)':r'hair|skin|scalp|itch|dry',
 'scale_stain_appliance (motive)':r'scal(e|ing)|stain|calcium|deposit|pipe|geyser|tile|tap\b|taps\b|bucket|white layer',
 'tds_or_hardness_measure':r'\btds\b|ppm|hardness|test',
 'no_effect':r'no (change|effect|result|difference|use|impact|visible)|waste|useless|not (working|effective|good|work)|does not work|doesn.t work|zer[io]+ effect|0 results|not worth|sham|not producing|not passed|didn.t work|did not work|rubbish|worst',
 'short_life_vs_claim':r'(days|week|month)s?\b.*(stop|work|last|float)|(stop|stopped|didn.t even last|floating)|only one week|just two months|within \d',
 'adverse_after_use (hairfall/itch/dark)':r'(increase|more|too much).{0,20}hair ?(fall|loss)|hair ?(fall|loss) (increase|too much)|hairloss has increased|itching|ittching|darker|dry or',
 'price_value_objection':r'costly|price (is )?(very )?high|expensive|not worth buying for that price|value',
 'salt_or_maintenance':r'\bsalt\b|maintenance|regenerat|refill|manual',
 'fake_review_distrust':r'fake|pay for reviews|fraud|cheat|sham',
 'install_ease (positive)':r'easy to install|no need of plumber|simple to install|easy install|easy to use|fit(ted)? instantly',
}
tot=0
per={}
for k,v in d.items():
    for r in v['rev']:
        t=html.unescape((r['title']+' '+r['text']).lower()); tot+=1
        for th,rx in themes.items():
            if re.search(rx,t): per.setdefault(th,{}).setdefault(k,0); per[th][k]+=1
print('listings:',{k:len(v['rev']) for k,v in d.items()},'total',tot)
for th in themes:
    s=sum(per.get(th,{}).values()); print(f'{th}: {s}  {per.get(th,{})}')
lows=[(k,r) for k,v in d.items() for r in v['rev'] if r['stars']<=2]
print('1-2 star reviews in sample:',len(lows))
for th in ['no_effect','short_life_vs_claim','adverse_after_use (hairfall/itch/dark)','price_value_objection','tds_or_hardness_measure']:
    c=sum(1 for k,r in lows if re.search(themes[th],html.unescape((r['title']+' '+r['text']).lower())))
    print(' low-star with',th,':',c)

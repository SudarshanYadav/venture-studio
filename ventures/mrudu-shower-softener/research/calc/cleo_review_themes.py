"""CLEO tap listing (Flipkart, 4,384 ratings on 2026-11-27): rating histogram and keyword theme counts.
Histogram is read from the page header (O). Themes are keyword matches on review text (approximate; sort-biased sample)."""
import json, glob, re, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
hist = {1: 599, 2: 220, 3: 495, 4: 1076, 5: 1994}   # Flipkart product-reviews page, 2026-11-27
tot = sum(hist.values())
print('Rating histogram (O, Flipkart 2026-11-27):', hist, 'total', tot)
print('1-2 star share: %.1f%%  (1 star %.1f%%)  4-5 star share: %.1f%%' % (100*(hist[1]+hist[2])/tot, 100*hist[1]/tot, 100*(hist[4]+hist[5])/tot))
mean = sum(k*v for k, v in hist.items())/tot
print('Mean from histogram: %.2f' % mean)
rated = [x for x in json.load(open(os.path.join(R,'raw/flipkart/2026-11-26/reviews-parsed-names-removed.json'))) if x['src'].startswith('fkr_cleotap')]
allrev = {}
for f in glob.glob(os.path.join(R,'raw/flipkart/2026-11-27/cleotap-*.json')):
    for x in json.load(open(f)): allrev[(x['title'].lower(), x['text'].lower()[:80])] = x['title']+' || '+x['text']
for x in rated: allrev[(x['title'].lower(), x['text'].lower()[:80])] = x['title']+' || '+x['text']
texts = list(allrev.values())
low = [x['title']+' || '+x['text'] for x in rated if float(x['rating']) <= 2]
THEMES = {
 'Breakage / crack / leak / loose fit / poor plastic': r'broke|broken|crack|leak|plastic|loose|fall|damag|thread|tighten|cheap|built|build quality|material|neck|holder|knob|nob|groove|clip|fitting',
 'No visible change / not effective / waste': r'no (change|difference|effect|improvement)|not (effective|working|work|useful|help|much)|doesn.t (work|solve|help)|did not|didn.t (observe|notice|work|help)|waste|useless|worthless|not worth|no use|not satisf|tds',
 'Short life / stopped working': r'week|month|days|stopped|life',
 'Hair / skin motive mentioned': r'hair|skin|itch|dry|rough|frizz|scalp',
 'Positive: works / good / value': r'good|great|nice|works|working well|worth|effective|best|happy|satisf|useful|perfect|excellent|amazing|awesome|love',
 'Hot water / flow / pressure': r'hot water|pressure|flow|slow',
 'Install: easy / fit trouble': r'install|easy|fit|plumber|adapter|adaptor',
}
def count(ts, label):
    print('\n%s: n=%d' % (label, len(ts)))
    for k, p in THEMES.items():
        n = sum(1 for t in ts if re.search(p, t, re.I))
        print('  %-52s %3d  %4.1f%%' % (k, n, 100*n/len(ts)))
count(texts, 'All unique CLEO tap review texts captured (sort-mixed; negative-first over-weighted)')
count(low, 'Rated 1-2 star subset (from 2026-11-26 capture)')
print('\nBreakage-type phrases in 1-2 star subset (strict: broke/crack/leak/loose/plastic/quality):',
      sum(1 for t in low if re.search(r'broke|broken|crack|leak|plastic|loose|keeps falling|poor (quality|durability|product)|quality|cheap', t, re.I)), 'of', len(low))

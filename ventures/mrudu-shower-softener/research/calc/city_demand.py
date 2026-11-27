"""Reviewer-city tally for Flipkart reviews already captured (2026-11-26) plus CLEO tap pages captured 2026-11-27.
Run: python3 -I city_demand.py  (from this folder). Output: city_demand_output.txt
City = the place string Flipkart shows beside a review (delivery/reviewer location, sometimes a district/division).
It shows where reviewers are, NOT market share, and the samples are sort-biased (negative-first, helpful, recent)."""
import json, glob, collections, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
STATE = {}
def S(state, names):
    for n in names.split('|'): STATE[n.strip().lower()] = state
S('Karnataka','Bengaluru|Bangalore|Bangalore Division|Bengaluru Rural District|Hoskote.|Mysuru|Kolar|Hassan|Hubli|Hubballi|Ilkal|Chitradurga|Chitradurga District|Bijapur|Bijapur District|Dakshina Kannada|Uttara Kannada|Udupi')
S('Delhi NCR','New Delhi|Delhi|Noida|Greater Noida|Gautam Buddha Nagar|Ghaziabad|Faridabad|Gurugram|Gurgaon|Gurgaon Division|Sonipat|Sohna|Bulandshahr')
S('Maharashtra','Mumbai|Thane|Navi Mumbai|Mira Bhayandar|Kalyan|Bhiwandi|Vasai Virar|Palghar|Raigad|Konkan Division|Pune|Pune Division|Pimpri Chinchwad|Lonavala|Karad|Sangli|Sangli District|Solapur|Sholapur|Pandharpur|Shrirampur|Ahmadnagar|Jalna|Jalgaon|Nashik|Amravati District|Bhusawal|Yavatmal|Gondiya|Savner|Selu|Jawhar|Utekhol|Overi')
S('Telangana','Hyderabad|Secunderabad|Rangareddy|Rangareddy District|Medchal Malkajgiri|Kamareddy|Karimnagar|Karimnagar District|Mahabubnagar|Mahabubabad|Medak District|Hanamkonda|Vemulawada|Thatipaka|Kothaguda')
S('Tamil Nadu','Chennai|Chengalpattu|Chengalpattu District|Madurapakkam|Tiruchirappalli|Coimbatore|Hosur|Krishnagiri|Vellore|Erode District|Namakkal District|Mettur|Panruti|Thoothukkudi District|Kanniyakumari District|Tirupathur District|Alangulam Virudhunagar District|Thiruvarur|Sriramapuram')
S('Andhra Pradesh','Visakhapatnam|Anakapalle|East Godavari|East Godavari District|Kakinada|Krishna District|Tenali|Tadepalligudem|Tadpatri|Kurnool|Chittoor|Ananthapuramu|Annamayya|Sri Sathya Sai|Bapatla|Payakaraopeta')
S('Gujarat','Ahmedabad|Ahmadabad District|Gandhinagar|Rajkot|Jamnagar|Vadodara|Valsad|Bharuch|Surat|Kachchh|Anand|Dahod|Porbandar|Vijapura')
S('Rajasthan','Jaipur|Jodhpur|Kota|Bikaner|Chomu|Jalor|Pali|Pali District|Baran District|Banswara|Udaipur District|Sri Ganganagar|Nasirabad')
S('West Bengal','Kolkata|Howrah|Barrackpore|North 24 Parganas|North Twenty Four Parganas District|Asansol|Burdwan|Bardhaman|Kharagpur|Medinipur|Medinipur Division|Siliguri|Jalpaiguri|Berhampore|Jangipur|Murshidabad District|Gobardanga|Raghunathpur Hugli District|Hijuli|Teleni Para|Uttar Dinajpur District')
S('Madhya Pradesh','Indore|Bhopal|Gwalior|Ujjain|Khandwa|Itarsi|Chhindwara|Chhatarpur|Khajuraho|Seoni Malwa|Shahdol|Harsud|Mandla District|Rau|Umarkote')
S('Uttar Pradesh','Lucknow|Kanpur|Agra|Varanasi|Saharanpur|Unnao|Barabanki|Bara Banki District|Azamgarh|Jaunpur|Pratapgarh District|Mau|Shohratgarh|Shahgarh|Pusaur|Lakhimpur|Desaiganj')
S('Odisha','Bhubaneswar|Cuttack|Sambalpur|Berhampur|Bhadrak|Khordha|Jajpur|Deogarh|Boudh|Ganjam District|Baleshwar|Badagada')
S('Kerala','Ernakulam|Kochi|Kottayam|Kanjirappally|Thrissur|Palakkad|Kannur|Thiruvananthapuram District|Malappuram District')
S('Punjab/Haryana/Chandigarh/HP/UK','Chandigarh|Ludhiana|Zirakpur|Bhatinda|Nakodar|Kapurthala District|Panipat District|Jind District|Dehradun|Haridwar|Haldwani|Kotdwara|Mandi Division|Tilda|Tilloi Industrial Area')
S('Chhattisgarh/Jharkhand/Bihar/NE/other','Raigarh|Raigarh District|Bilaspur|Bhilai|Durg|Kanker|Charama|Ranchi|Jamshedpur|Bokaro Steel City|Seraikela Kharsawan|Patna|Begusarai|Katihar|Saran District|Agartala|West Tripura|Jorhat|Dimapur|Sribhumi|Margao|Karaikal|Nit Karaikal')
CLUSTER = {}
def C(c, states_or_names):
    for n in states_or_names.split('|'): CLUSTER[n.strip().lower()] = c
C('Bengaluru metro','Bengaluru|Bangalore|Bangalore Division|Bengaluru Rural District|Hoskote.')
C('Delhi NCR','New Delhi|Delhi|Noida|Greater Noida|Gautam Buddha Nagar|Ghaziabad|Faridabad|Gurugram|Gurgaon|Gurgaon Division|Sonipat|Sohna')
C('Mumbai MMR','Mumbai|Thane|Navi Mumbai|Mira Bhayandar|Kalyan|Bhiwandi|Vasai Virar|Palghar')
C('Pune','Pune|Pune Division|Pimpri Chinchwad')
C('Hyderabad metro','Hyderabad|Secunderabad|Rangareddy|Rangareddy District|Medchal Malkajgiri')
C('Chennai metro','Chennai|Chengalpattu|Chengalpattu District|Madurapakkam')
C('Kolkata metro','Kolkata|Howrah|Barrackpore|North 24 Parganas|North Twenty Four Parganas District')
C('Ahmedabad-Gandhinagar','Ahmedabad|Ahmadabad District|Gandhinagar')
C('Jaipur','Jaipur|Chomu')

def load():
    seen = set(); rows = []
    def add(city, title, text, grp):
        city = (city or '').strip()
        k = (city.lower(), (title or '').strip().lower(), (text or '').strip().lower()[:80])
        if k in seen: return
        seen.add(k); rows.append((city, grp))
    for f in sorted(glob.glob(os.path.join(R, 'raw/flipkart/2026-11-27/cleotap-*.json'))):
        for x in json.load(open(f)): add(x['city'], x['title'], x['text'], 'CLEO tap (4,381-rating listing)')
    for x in json.load(open(os.path.join(R, 'raw/flipkart/2026-11-26/reviews-parsed-names-removed.json'))):
        g = 'CLEO tap (4,381-rating listing)' if x['src'].startswith('fkr_cleotap') else 'Other hard-water listings'
        add(x['city'], x['title'], x['text'], g)
    for k, v in json.load(open(os.path.join(R, 'raw/landscape/2026-11-26/flipkart-reviews-names-removed.json'))).items():
        for r in v['rev']: add(r['city'], r['title'], r['text'], 'Other hard-water listings')
    return rows

def report(rows, label):
    n = len(rows); known = [r for r in rows if r[0]]
    print(f'\n=== {label}: {n} unique reviews, {len(known)} with a city shown ===')
    cl = collections.Counter(CLUSTER.get(c.lower(), 'Other / long tail') for c, _ in known)
    print('Metro cluster share (of reviews with a city):')
    for k, v in cl.most_common(): print(f'  {k:26s} {v:4d}  {100*v/len(known):5.1f}%')
    st = collections.Counter(STATE.get(c.lower(), 'UNMAPPED') for c, _ in known)
    print('State/region share:')
    for k, v in st.most_common(): print(f'  {k:42s} {v:4d}  {100*v/len(known):5.1f}%')
    # Wilson 95% interval for Bengaluru metro
    b = cl['Bengaluru metro']; p = b/len(known); z = 1.96
    den = 1 + z*z/len(known); ctr = (p + z*z/(2*len(known)))/den
    half = z*((p*(1-p)/len(known) + z*z/(4*len(known)**2))**.5)/den
    print(f'Bengaluru metro: {b}/{len(known)} = {100*p:.1f}%  (95% Wilson interval {100*(ctr-half):.1f} to {100*(ctr+half):.1f}%)')

rows = load()
report(rows, 'ALL captured Flipkart hard-water reviews')
report([r for r in rows if r[1].startswith('CLEO')], 'CLEO tap listing only')
report([r for r in rows if r[1].startswith('Other')], 'Other listings (RiverSoft, Purifit, Snix, Avimee, Scale-O, D\'Cal, etc.)')
unm = sorted({c for c, _ in rows if c and c.lower() not in STATE})
print('\nUnmapped city strings:', unm)

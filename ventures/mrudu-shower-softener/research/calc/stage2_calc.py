"""Mrudu Stage 2 arithmetic. Run: python3 -I stage2_calc.py  (no inputs; all assumptions inline)."""
G_PER_EQ_CACO3 = 50.0            # g CaCO3 per equivalent
GRAIN_G = 0.0648                  # g per grain
FT3_L = 28.317

print("== 1. Resin capacity per litre of resin")
total = 1.9 * G_PER_EQ_CACO3      # Purolite C100E total capacity 1.9 eq/L (datasheet, opened)
pwp = 32000 * GRAIN_G / FT3_L     # Pure Water Products: 32,000 grains/ft3 for new resin (opened)
print(f"total capacity (datasheet) = {total:.1f} g CaCO3/L resin; PWP working figure = {pwp:.1f} g/L")

print("== 2. Litres softened by a shower-arm cartridge before exhaustion")
vols = [0.10, 0.20, 0.35]          # L of resin in cartridge: ASSUMPTION (bench test measures)
hards = [200, 350, 600]            # mg/L as CaCO3: Bengaluru borewell band (DMG 48-1540; 8.5% >600)
caps = [pwp, total]
shower_L = (50, 80)                # L per shower: ASSUMPTION 7-10 L/min x 7-8 min
for v in vols:
    for h in hards:
        lo = v*caps[0]*1000/h; hi = v*caps[1]*1000/h
        print(f"resin {v:.2f} L, hardness {h}: {lo:5.0f}-{hi:5.0f} L softened = {lo/shower_L[1]:.1f}-{hi/shower_L[0]:.1f} showers")

print("== 3. Flow check: service-flow limit 8-40 BV/h (Purolite, Resinex, Lewatit sheets via search; Purolite C100 text)")
for v in vols:
    for q in (6, 10):              # L/min shower flow: ASSUMPTION
        bvh = q*60/v
        print(f"resin {v:.2f} L at {q} L/min = {bvh:,.0f} BV/h = {bvh/40:.0f}x the 40 BV/h maximum")
print("resin volume needed for 40 BV/h at 8 L/min:", 8*60/40, "L")

print("== 4. Cross-check vs Pure Water Products 2.5x9.75in cartridge (opened): 15 gal @ 40 gpg, 45 gal @ 15 gpg")
import math
vin3 = math.pi*(1.25-0.125)**2*9.5   # ASSUMPTION: ~0.125in wall, 9.5in fill
vL = vin3*0.016387
for gal, gpg in ((15,40),(45,15),(105,7)):
    L = gal*3.785; h = gpg*17.1
    print(f"{gal} gal @ {gpg} gpg = {L:.0f} L @ {h:.0f} mg/L -> implied {L*h/1000/vL:.0f} g/L over ~{vL:.2f} L resin")

print("== 5. Bathroom-scale regenerable unit sizing (pivot idea)")
for ppl in (2,3,4):
    for h in (250,350,500):
        g_day = ppl*60*h/1000
        for opcap in (40,60):     # g CaCO3/L operating capacity at modest salt dose: ASSUMPTION
            pass
        print(f"{ppl} people x 60 L at {h} mg/L = {g_day:.0f} g/day -> resin for 7-day regen: {g_day*7/60:.1f}-{g_day*7/40:.1f} L")

print("== 6. Bengaluru TAM/SAM (households)")
hh = (3.0e6, 3.8e6)              # ASSUMPTION; BBMP 20-22 lakh properties (snippet) is a floor
gw = (0.45, 0.62)                # DH 2016: 45% depend on borewell (opened); SEI 26%+36% (snippet)
hard = (0.45, 0.60)              # DMG 2011: 45% within desirable 200 mg/L -> ~55% above (snippet+opened page); range
tam = (hh[0]*gw[0]*hard[0], hh[1]*gw[1]*hard[1])
print(f"TAM households = {tam[0]:,.0f} - {tam[1]:,.0f}; at Rs1,999 = Rs {tam[0]*1999/1e7:,.0f}-{tam[1]*1999/1e7:,.0f} crore (one-time)")
reach = (0.6,0.8)
sam = (tam[0]*reach[0], tam[1]*reach[1])
print(f"SAM households = {sam[0]:,.0f} - {sam[1]:,.0f}")
own = (0.35,0.50)                 # owner share ASSUMPTION (Census HL-04 not opened) -> pivot product SAM
print(f"Owner-occupier SAM (pivot) = {sam[0]*own[0]:,.0f} - {sam[1]*own[1]:,.0f}")

print("== 7. Competitor-led (India, Flipkart ratings as a demand proxy)")
ratings = {'CLEO tap (municipal)':4381,'RiverSoft SF-15':924,'RiverSoft DIVA PRO':442,'Purifit shower head':356,'Snix':308,'CLEO SFU-423 HHC':226,'RiverSoft DIVA-01':87,'RiverSoft DIVA-03':80,'Purifit Atom':75}
tot = sum(ratings.values())
for r in (0.01,0.03,0.05):        # ratings per unit sold: ASSUMPTION
    print(f"ratings/unit {r:.0%}: lifetime Flipkart units of top 9 = {tot/r:,.0f}")
print("top-9 rating total", tot)
ws = 1.5e6                        # WaterScience on-site claim 'Trusted by 1.5 million customers' (all products, years unknown)
for yrs in (4,6,8):
    print(f"WaterScience claim spread over {yrs} yrs = {ws/yrs:,.0f} customers/yr ~ Rs {ws/yrs*2000/1e7:,.0f} crore/yr at Rs2,000")

print("== 8. Star distribution, share of 1-2 star")
dist = {'CLEO tap':(599,219,495,1076,1992),'RiverSoft SF-15':(102,59,91,218,454),'DIVA PRO':(49,21,46,104,222),'Purifit':(20,12,23,65,236),'Snix':(49,21,35,71,132),'CLEO 423 HHC':(28,11,26,57,104)}
for k,d in dist.items():
    n=sum(d); print(f"{k}: n={n} 1-2 star {100*(d[0]+d[1])/n:.1f}%  mean {sum((i+1)*x for i,x in enumerate(d))/n:.2f}")

print("== 9. Channel-led SOM and side-income gap (India, Bangalore)")
for spend in (2e5,4e5):
    for cpo in (450,730):
        for uplift in (1.2,1.5):
            pass
lo = 2e5/730*1.2; hi = 4e5/450*1.5
print(f"12-month SOM orders = {lo:,.0f}-{hi:,.0f}; revenue Rs {lo*1999/1e5:.1f}-{hi*1999/1e5:.1f} lakh")
P1=730.36
for cpo in (450,511,600):
    per = P1-cpo
    print(f"CPO {cpo}: net per order Rs{per:.0f}; orders/month for Rs50k = {50000/per:,.0f}")

print("== 10. UAE price check")
aed_inr = 85/3.6725
for aed in (229,339,380):
    print(f"AED {aed} = Rs {aed*aed_inr:,.0f}")
for cpc_usd in (1.0,1.65):
    for cvr in (0.01,0.02,0.03):
        print(f"UAE CPC ${cpc_usd} CVR {cvr:.0%}: CPO AED {cpc_usd*3.6725/cvr:,.0f}")

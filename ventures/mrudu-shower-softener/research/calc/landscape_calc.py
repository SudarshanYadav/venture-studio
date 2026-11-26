# Landscape calc, 2026-11-26. Resin capacity scaling and salt cost for bathroom-scale softeners.
# Inputs are the makers' own published figures (opened 2026-11-26) except where marked ASSUMPTION.
specs = {  # name: (resin_L, litres_between_regen, at_hardness_ppm_CaCO3, salt_kg_per_regen)
  "Kent Bathroom 5.5 L (kent.co.in)": (5.5, 1500, 200, 0.88),
  "Kent Auto 8 L (kent.co.in)":       (8.0, 2200, 200, 1.28),
}
print("Implied resin working capacity (eq per L resin) = L x ppm/50 / resin_L")
for n,(r,l,h,s) in specs.items():
    print(f"  {n}: {l*h/50/1000/r:.2f} eq/L")
# ZeroB POU: 300 L @500 ppm, 600 L @250 ppm (resin volume not published) -> 3.0 eq per recharge
print("  ZeroB POU: 300 L x 500/50 = 3.0 eq per recharge; 600 L x 250/50 = 3.0 eq (consistent)")
EQ_PER_L=1.1  # from Kent figures
def litres(resin_L, ppm): return resin_L*EQ_PER_L*1000/(ppm/50)
# ASSUMPTION: 4-person home, 8-min shower at 9 L/min each = 288 L/day through the softener (bathroom only)
daily=4*8*9
print(f"\nASSUMPTION daily shower water, 4 people: {daily} L/day")
SALT_LOW, SALT_HIGH = 834/15, 680/5   # Rs/kg: 15 kg bag Rs 834 (aquatech naturals) ; 5 kg Rs 680 (Greendrop), Flipkart 2026-11-26
print(f"Salt price Rs/kg: {SALT_LOW:.0f} (15 kg bag) to {SALT_HIGH:.0f} (5 kg bag)")
for ppm in (200,350,500):
    cap=litres(5.5,ppm); days=cap/daily; regen=365/days; salt=regen*0.88
    print(f"Kent-bath-size 5.5 L resin @ {ppm} ppm: {cap:.0f} L per regen, every {days:.1f} days, {regen:.0f} regens/yr, {salt:.0f} kg salt/yr, salt Rs {salt*SALT_LOW:,.0f} to {salt*SALT_HIGH:,.0f}")
for ppm in (200,350,500):
    cap=litres(8,ppm); days=cap/daily; regen=365/days; salt=regen*1.28
    print(f"Kent-8L-size 8 L resin @ {ppm} ppm: {cap:.0f} L per regen, every {days:.1f} days, {regen:.0f} regens/yr, {salt:.0f} kg salt/yr, salt Rs {salt*SALT_LOW:,.0f} to {salt*SALT_HIGH:,.0f}")
# 12-month cost of conditioner shower filters (unit + replacement cartridges, 1 or 2 in year one)
print("\n12-month cost, conditioners (unit + 1 to 2 replacement cartridges; life 4-6 months claimed)")
for n,unit,cart in [("WaterScience CLEO SFM-419",2795,845),("RiverSoft SF-15",1549,684),("Purifit (Flipkart head)",999,699),("Purifit Ultra",1499,849)]:
    print(f"  {n}: Rs {unit+cart:,} to Rs {unit+2*cart:,}")
print("  WaterScience 2-pack cartridge 1,595 -> unit+2-pack =", 2795+1595)
print("  Scale-O Mini 1-year plan Rs 5,000; Semi 7,000; Centi 8,000 (scale-o.com)")
# bucket-bath liquid: ASSUMPTION one 400 ml bottle per month
print("  Avimee 400 ml Rs 410 -> Rs", 410*12, "per year IF one bottle/month (ASSUMPTION; dose per bucket '3 caps' per a reviewer, bottle yield unknown)")
# Ratings
import math
dist={"D'Cal":(150,57,105,208,412),"Avimee":(294,188,516,1156,2651)}
for k,(a,b,c,d,e) in dist.items():
    n=a+b+c+d+e; mean=(a+2*b+3*c+4*d+5*e)/n
    print(f"{k}: n={n}, mean={mean:.2f}, 1-2 star share={(a+b)/n*100:.1f}%")

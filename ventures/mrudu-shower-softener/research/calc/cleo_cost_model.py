"""Landed-cost and contribution model for a CLEO-class tap/shower filter (HSN 8421), India, D2C.
Every input is tagged O (observed on an opened page), S (search snippet) or I (inferred/assumption) with its source key.
Rate: Rs 85/USD (studio rate, 2026-11-26). Prices to customers are GST-inclusive; GST 18% is stripped before margin.
IGST paid on import is treated as recoverable input credit for a GST-registered seller (cash-flow cost only, shown separately).
Run: python3 -I cleo_cost_model.py > cleo_cost_model_output.txt
Source keys (URLs in sources.md section N):
 MIC1 made-in-china.com/products-search/hot-china-products/Kdf_Shower_Filter.html  (O, 2026-11-27)
 MIC2 .../Tap_Shower_Filter.html (O)   MIC3 .../Kdf55.html (O)   MIC4 .../Faucet_Water_Filter_Hard_Water.html (O)
 IM1  dir.indiamart.com/search.mp?ss=kdf+shower+filter (O, trader listings)   IM2 dir.indiamart.com/search.mp?ss=tap+filter+hard+water (O)
 TX1  taxclue.in/hsn-code/84212120 and /84212190 (O): BCD 10% / 7.5%; 8421 99 heading 7.5/10/15% (O); SWS 10% of BCD; GST 5%/18% by description
 RZP  razorpay.com/blog (S): 2% + 18% GST = 2.36%      SR shiprocket.in (S): from Rs 20 per 500 g, excl GST
 WS   waterscience.in/products.json (O, 2026-11-27): unit shipping weight 520 g, cartridge 230 g, cartridge Rs 845
"""
USD = 85.0
GST = 0.18
CASES = ['low', 'base', 'high']

def row(name, vals, tag, src):
    print('  %-58s %8s %8s %8s  [%s] %s' % (name, *[('%.1f' % v if isinstance(v, float) else str(v)) for v in vals], tag, src))

# ---------- A. Cartridge bottom-up (media + parts), Rs per cartridge ----------
print('=== A. Cartridge bottom-up bill of materials (Rs per cartridge, before conversion margin) ===')
kdf_g   = (30, 45, 60);   kdf_usd_kg = (8, 14, 20)       # MIC3: generic Cu-Zn KDF55-type media US$8-20/kg (MOQ 5-100 kg). I: grams per cartridge
casulf_g= (10, 20, 30);   casulf_usd_kg = (10, 15, 20)    # MIC (calcium sulfite lister US$10-20/kg, MOQ 1 kg; single supplier, low confidence)
carbon_g= (20, 30, 40);   carbon_rs_kg = (150, 275, 400)  # I: no source opened for Indian activated-carbon price
other   = (30, 50, 70)                                    # I: vitamin C/ceramic/nonwoven mesh, o-rings, body and caps, assembly
cart_bom = []
for i in range(3):
    c = kdf_g[i]/1000*kdf_usd_kg[i]*USD + casulf_g[i]/1000*casulf_usd_kg[i]*USD + carbon_g[i]/1000*carbon_rs_kg[i] + other[i]
    cart_bom.append(c)
row('KDF-type media', [kdf_g[i]/1000*kdf_usd_kg[i]*USD for i in range(3)], 'O/I', 'MIC3 price; grams I')
row('Calcium sulfite', [casulf_g[i]/1000*casulf_usd_kg[i]*USD for i in range(3)], 'S/I', 'MIC price; grams I')
row('Activated carbon', [carbon_g[i]/1000*carbon_rs_kg[i] for i in range(3)], 'I', 'no source')
row('Other media, body, caps, o-rings, assembly', other, 'I', 'no source')
row('Cartridge bottom-up total (Rs)', cart_bom, 'I', 'sum')
print('  Cross-check, bought-in cartridge prices: IndiaMART Rs 170 (MOQ 100), Rs 320 (MOQ 50) [O, IM1]; Made-in-China US$3.50 = Rs %.0f (MOQ 10) [O, MIC1]' % (3.5*USD))
print('  WaterScience sells its cartridge at Rs 845 [O, WS]; ratio of its price to our bottom-up base = %.1fx' % (845/cart_bom[1]))
cart_buy = (170.0, 250.0, 320.0)   # purchase price of a finished cartridge, India trader/OEM (IM1) low/base/high

# ---------- B. Unit landed cost, two routes ----------
print('\n=== B1. Route A: import finished tap/shower filter from China (white-label) ===')
fob_usd   = (2.5, 4.5, 6.0)       # MIC2 US$2.00-4.00 (MOQ 500), MIC1 US$2.5-3.6 (MOQ 100-1000), US$7.85-12.9 metal/vitamin C (MOQ 1-50); high = branded-grade factory with QC (I); metal-adapter units list at US$7.85-12.9 (MIC1)
freight   = (0.10, 0.15, 0.20)    # I: sea LCL or mixed air, share of FOB
bcd       = (0.075, 0.10, 0.15)   # TX1: 7.5% (8421 21 90), 10% (8421 21 20), up to 15% on some 8421 99 parts
sws       = 0.10                  # TX1: 10% of BCD
lot_units = (1000, 500, 300)      # I: units per shipment (MIC MOQs 100-1,000)
lot_fixed = (15000, 25000, 30000) # I: CHA, port, inland haulage, third-party QC per shipment, Rs
tooling   = (0, 0, 0)             # base cases use the supplier's existing mould. Own mould is modelled in section H only
tool_units= 3000
landed_A = []
for i in range(3):
    fob = fob_usd[i]*USD
    cif = fob*(1+freight[i])
    duty = cif*bcd[i]*(1+sws)
    fixed = lot_fixed[i]/lot_units[i]
    tool = tooling[i]/tool_units
    landed_A.append(cif+duty+fixed+tool)
row('FOB (Rs)', [fob_usd[i]*USD for i in range(3)], 'O/I', 'MIC1/MIC2')
row('+ freight and insurance', [fob_usd[i]*USD*freight[i] for i in range(3)], 'I', '')
row('+ BCD and SWS', [fob_usd[i]*USD*(1+freight[i])*bcd[i]*(1+sws) for i in range(3)], 'S', 'TX1')
row('+ clearing, port, QC per unit', [lot_fixed[i]/lot_units[i] for i in range(3)], 'I', '')
row('+ tooling per unit (3,000 units)', [tooling[i]/tool_units for i in range(3)], 'I', 'no source')
row('LANDED UNIT COST, Route A (Rs, ex GST)', landed_A, 'mixed', '')
print('  IGST on import (18% of CIF+duty) is creditable; cash tied up per unit (Rs):', ['%.0f' % ((fob_usd[i]*USD*(1+freight[i])*(1+bcd[i]*(1+sws)))*GST) for i in range(3)])

print('\n=== B2. Route B: buy white-label unit from an Indian trader/OEM ===')
landed_B = (360.0, 500.0, 1190.0)   # IM1: WaterLabs HL-2 Rs 360 (MOQ 50), HL-29 Rs 500, 15-stage KDF 55 Rs 1,190 (MOQ 300). GST status unknown, treated as ex-GST
row('Trader quote, unit (Rs)', landed_B, 'O', 'IM1 (listing prices, not quotes; GST status unknown)')

# choose the model: low = Route A low, base = mean-ish Route A base, high = Route A high (own tooling, better build)
unit_cost = landed_A
cart_cost = cart_buy

# ---------- C. Variable cost per order ----------
pack   = (25.0, 40.0, 70.0)     # I: retail box, manual, adapters, PTFE tape
ship   = (55.0, 75.0, 100.0)    # S/I: SR 'from Rs 20 / 500 g' excl GST; national average 0.7 kg parcel; GST creditable so ex-GST
strip  = (0.0, 6.0, 12.0)       # I: hardness test strip per order (optional)
pg     = 0.0236                 # RZP
ret_rate = (0.05, 0.10, 0.15)   # I: returns + warranty replacements. Evidence: 18.7% of ratings are 1-2 star [O]; 19 to 23 of 44 sampled low-star reviews cite breakage/leak [O]; Flipkart 7-day return [O]
def contribution(price, i, with_cart_extra=False):
    net = price/(1+GST)
    pgfee = price*pg/(1+GST)               # fee on gross, GST on fee creditable; approx ex-GST value
    retcost = ret_rate[i]*(unit_cost[i] + ship[i]*2)   # replacement unit + two-way freight
    var = unit_cost[i] + pack[i] + ship[i] + strip[i] + pgfee + retcost
    return net, var, net-var

print('\n=== C. Unit contribution per order, D2C prepaid, before ads (Rs, ex-GST) ===')
res = {}
for price in (1495, 1999):
    print('  -- price Rs %d GST-incl --' % price)
    nets, vars_, cons = zip(*[contribution(price, i) for i in range(3)])
    row('Net revenue after 18% GST', nets, 'I', 'GST rule')
    row('Variable cost (unit+pack+ship+strip+PG+returns)', vars_, 'mixed', '')
    row('CONTRIBUTION per order before ads', cons, 'mixed', '')
    row('Contribution margin on net revenue (%)', [100*cons[i]/nets[i] for i in range(3)], '', '')
    res[price] = cons

print('\n  NOTE: low/base/high pair low cost with low return rate and high cost with high return rate (a deliberately wide band).')
print('  Return-rate sensitivity at BASE cost (returns+warranty as % of orders):')
for rr in (0.05, 0.10, 0.15, 0.20):
    for price in (1495, 1999):
        net = price/(1+GST); pgf = price*pg/(1+GST)
        con = net - (unit_cost[1]+pack[1]+ship[1]+strip[1]+pgf+rr*(unit_cost[1]+ship[1]*2))
        print('    returns %2d%%  price %d  contribution Rs %.0f' % (rr*100, price, con))

# ---------- D. Cartridge ----------
print('\n=== D. Cartridge contribution (Rs, ex-GST), shipped alone ===')
cship = (45.0, 60.0, 80.0)      # I: 230 g parcel (WS weight)
cpack = (8.0, 12.0, 20.0)       # I
cret  = (0.02, 0.04, 0.08)      # I
for price in (695, 845):
    net = price/(1+GST)
    cons = [net - cart_cost[i] - cpack[i] - cship[i] - price*pg/(1+GST) - cret[i]*(cart_cost[i]+cship[i]*2) for i in range(3)]
    print('  -- cartridge price Rs %d --' % price)
    row('Net revenue', [net]*3, 'I', '')
    row('Cartridge cost (bought-in)', cart_cost, 'O/I', 'IM1 Rs 170-320')
    row('CONTRIBUTION per cartridge', cons, 'mixed', '')
    row('Margin on net (%)', [100*cons[i]/net for i in range(3)], '', '')
    res[('c', price)] = cons

# ---------- E. Year-1 value per customer and orders needed ----------
print('\n=== E. Year-1 contribution per customer and orders/month for Rs 50,000/month net ===')
for price in (1495, 1999):
    for rep in (0.0, 0.3, 0.6):
        cart_con = res[('c', 845)]
        y1 = [res[price][i] + rep*cart_con[i] for i in range(3)]
        print('  price %d, cartridge repeat %.0f%% (assumption; no observed repeat rate): year-1 contribution Rs %s' % (price, rep*100, ['%.0f' % v for v in y1]))
print('  Orders per month to net Rs 50,000/month after ads, base-case contribution, by cost per order (CPO, I; implied range from REPORT section 7: Rs 267-2,800, central 800):')
for price in (1495, 1999):
    base = res[price][1]
    out = []
    for cpo in (400, 600, 800, 1000):
        m = base - cpo
        out.append('CPO %d: %s' % (cpo, ('%.0f orders' % (50000/m)) if m > 0 else 'never (contribution <= CPO)'))
    print('   price %d (base contribution Rs %.0f):' % (price, base), '; '.join(out))
print('  Break-even CPO (= base contribution before ads): price 1,495 Rs %.0f; price 1,999 Rs %.0f' % (res[1495][1], res[1999][1]))

# ---------- F. Capital to start ----------
print('\n=== F. First-order capital (Route A base, 500 units + 500 cartridges), Rs ===')
n = 500
inv = n*landed_A[1] + n*cart_buy[1]
igst_cash = n*((fob_usd[1]*USD*(1+freight[1])*(1+bcd[1]*(1+sws)))*GST)
print('  Inventory at landed cost: %.0f; IGST cash held until credit: %.0f; samples/pre-production (5 vendors x US$30 incl air, I): %.0f; lab test of hardness/flow (I, 2 x Rs 6,000): 12000' % (inv, igst_cash, 5*30*USD))
print('  Total ~ Rs %.0f against the Rs 8.5 lakh ceiling, before ads' % (inv+igst_cash+5*30*USD+12000))

# ---------- G. Marketplace sensitivity (commission UNKNOWN) ----------
print('\n=== G. Marketplace sensitivity at Rs 1,495 (Flipkart category commission NOT found; all figures I) ===')
for comm in (0.08, 0.12, 0.16):
    net = 1495/(1+GST); fee = comm*net + 30 + 70   # commission + fixed fee + marketplace shipping fee, ex GST, I
    cons = [net - (unit_cost[i]+pack[i]) - fee - ret_rate[i]*(unit_cost[i]+ship[i]*2) for i in range(3)]
    print('  commission %.0f%%: contribution before ads Rs %s' % (comm*100, ['%.0f' % c for c in cons]))

# ---------- H. Wedge build: better housing than the Rs 1,495 incumbent (our own mould, metal-reinforced neck) ----------
print('\n=== H. Wedge build "CLEO-class but does not break" (all I; no supplier quote) ===')
for tool in (200000, 400000, 800000):
    for units in (3000, 6000):
        fob = 6.0*USD; cif = fob*1.20; duty = cif*0.15*(1+sws); fixed = 30000/500
        landed = cif+duty+fixed+tool/units
        for price in (1499, 1999):
            net = price/(1+GST); pgf = price*pg/(1+GST)
            con = net - (landed+pack[2]+ship[1]+strip[1]+pgf+0.04*(landed+ship[1]*2))
            print('  mould Rs %6d over %d units: landed Rs %4.0f; price %d contribution Rs %4.0f (returns 4%% assumed if the build fix works)' % (tool, units, landed, price, con))
print('  Mould cost range Rs 2-8 lakh is an assumption; no source opened. Ask two OEMs for a mould quote before relying on it (needs founder OK to contact).')

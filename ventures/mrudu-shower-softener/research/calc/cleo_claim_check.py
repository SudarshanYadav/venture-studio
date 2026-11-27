"""Sanity check of WaterScience's published cartridge life (25,000 L, SFU-717 listing, captured 2026-11-26) against ion-exchange capacity.
If the cartridge removed hardness by exchange, 25,000 L would carry this much hardness (as CaCO3) onto the media.
Resin capacity: 95 g CaCO3 per L resin (Purolite C100E, REPORT section 8, High)."""
for ppm in (200, 300, 550):
    load_kg = 25000*ppm/1e6
    resin_L = load_kg*1000/95
    print('hardness %3d mg/L: %.1f kg CaCO3 in 25,000 L -> %.0f L of fresh softening resin (cartridge total weight is 230 g)' % (ppm, load_kg, resin_L))
print('Conclusion: the cartridge cannot be an exchange softener at that life; any hardness effect would have to come from something other than removal (WaterScience calls it conditioning). Whether conditioning works was not tested here.')

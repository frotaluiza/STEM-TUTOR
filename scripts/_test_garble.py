import sys
sys.path.insert(0, 'scripts')
from format_textbook import is_garbled_block

tests = ['R1 47', 'C3', 'L1', 'U1 SBL-1 Mixer', '10 k', '7 MHz C6', 'Antenna', 'Oscillator']
for t in tests:
    s = is_garbled_block(t)
    label = "GARBLE" if s > 0.4 else "clean"
    print(f"{t:30s} score={s:.2f} [{label}] len={len(t)}")

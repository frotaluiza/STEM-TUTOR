import re

CIRCUIT_COMP_RE = re.compile(r"\b[RCLEFUQ]\d+\b")
tests = ['R1 47', 'C3', 'L1', 'U1 SBL-1 Mixer', '10 k', '7 MHz C6', 'Antenna', 'Oscillator']
for t in tests:
    matches = CIRCUIT_COMP_RE.findall(t)
    words = t.split() if t.split() else [t]
    density = len(matches) / max(len(words), 1)
    print(f"{t:25s} matches={matches} words={words} density={density:.2f}")
